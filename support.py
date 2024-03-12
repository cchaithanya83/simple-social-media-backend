
import fastapi as _fastapi
from fastapi.templating import Jinja2Templates
from fastapi import Form
from sqlalchemy import create_engine, Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from starlette.requests import Request
from starlette.responses import RedirectResponse
Base = declarative_base()
from datetime import datetime


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, index=True)
    password = Column(String, index=True)

class Post(Base):
    __tablename__ = "posts"
    datetime = Column(String, index=True)
    name = Column(String, index=True)
    post_id = Column(Integer, primary_key=True, index=True)
    uid = Column(Integer, index=True)
    post = Column(String, index=True)
    like= Column(String, index=True)

class Like(Base):
    __tablename__ = "likes"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    post_id = Column(Integer, index=True)


