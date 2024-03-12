import fastapi as _fastapi
from fastapi.templating import Jinja2Templates
from sqlalchemy import create_engine, Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from starlette.requests import Request
from starlette.responses import RedirectResponse
from support import User,Post,Like
from fastapi import Form, Depends, Response,HTTPException
from datetime import datetime
from sqlalchemy import or_
from sqlalchemy.exc import IntegrityError

app= _fastapi.FastAPI()  #instance 
templates = Jinja2Templates(directory="html")  #

# SQLite database setup
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Create tables
metadata = MetaData()
Base.metadata.create_all(bind=engine)

@app.get("/")
def main(request: Request):
    return templates.TemplateResponse(
        name="index.html",
        context={"request":request}
    )


@app.get("/signin")
def signin(request: Request):
    return templates.TemplateResponse(
        name="signin.html",
        context={"request":request}
    )

@app.post("/signinaction")
def signinaction(request: Request, name: str= _fastapi.Form(...),email : str= _fastapi.Form(...),password: str= _fastapi.Form(...)):
    db = SessionLocal()
    new_user = User(name=name, email=email, password=password)
    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)   
    except :
        return("Email already exits or try later")
    finally:
        db.close()
    return RedirectResponse(url="/", status_code=303)

@app.get("/login")
def login(request: Request):
    return templates.TemplateResponse(
        name="login.html",
        context={"request":request}
    )

@app.post("/loginaction")
def loginaction(request: Request, email: str= Form(...), password: str=Form(...)):
    db = SessionLocal()
    user = db.query(User).filter(User.email == email, User.password == password).first()
    if user is None:
        return "User not found"
    else:
        uid=user.id
        name=user.name
        response = RedirectResponse(url="/viewposts", status_code=303)
        response.set_cookie(key='name', value= name)
        response.set_cookie(key="uid", value=uid)        
        return response
        
    
@app.get("/createpost")
def createpost(request: Request):
    return templates.TemplateResponse(
        name="createpost.html",
        context={"request":request}
    )
    

@app.post("/createpostaction")
def createpostaction(request: Request, post: str= Form(...)):
    db = SessionLocal()
    uid = request.cookies.get("uid")
    name= request.cookies.get("name")
    current_datetime = datetime.now()
    date_time = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    new_post= Post(uid= uid, post= post,datetime= date_time,name=name, like=0)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    db.close()
    return RedirectResponse(url="/viewposts", status_code=303)




@app.get("/myposts")
def list_myposts(request: Request):
    db = SessionLocal()
    uid = request.cookies.get("uid")
    print(uid)
    posts = db.query(Post).all()
    db.close()
    return templates.TemplateResponse(
        name="mypost.html",
        context={"request": request, "posts": posts, "uid":int(uid) }
    )




@app.get("/viewposts")
def view_posts(request: Request):
    db = SessionLocal()
    posts = db.query(Post).all()
    db.close()
    return templates.TemplateResponse(
        name="viewpost.html",
        context={"request": request, "posts": posts}
    )




@app.post("/like/{post_id}")
def like_post(request: Request, post_id: int):
    db = SessionLocal()
    user_id = int(request.cookies.get("uid"))
    
    # Check if the user has already liked the post
    existing_like = db.query(Like).filter(Like.user_id == user_id, Like.post_id == post_id).first()
    if existing_like:
        db.close()
        return RedirectResponse(url="/viewposts", status_code=303)

    # If not, add a new like record
    new_like = Like(user_id=user_id, post_id=post_id)
    db.add(new_like)

    # Update the post's like count
    post = db.query(Post).filter(Post.post_id == post_id).first()
    if post:
        post.like += 1

    try:
        db.commit()
        db.close()
    except IntegrityError:
        db.rollback()
        return "Integrity Error"

    return RedirectResponse(url="/viewposts", status_code=303)

@app.get("/delete_post/{post_id}")
def delete_post(request: Request, post_id: int):
    db = SessionLocal()
    post = db.query(Post).filter(Post.post_id == post_id).first()

    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    # Delete associated likes
    db.query(Like).filter(Like.post_id == post_id).delete()

    # Delete the post
    db.delete(post)
    db.commit()

    return RedirectResponse(url="/myposts", status_code=303)


if __name__ == "__main__":
        import uvicorn
        uvicorn.run("main:app", host="127.0.0.1",
        port=8000,
        log_level="info", reload=True)