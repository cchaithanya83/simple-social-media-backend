
# Social Media Backend - FastAPI Project

This repository contains a social media backend API built using FastAPI, an asynchronous web framework for building APIs with Python. The application allows users to sign up, log in, create posts, view posts, and like posts. It also supports SQLite for database operations.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the App](#running-the-app)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

This project is a social media backend that supports user authentication, post creation, viewing posts, and liking posts. The backend is built with FastAPI and uses SQLite for data storage. It also includes HTML templates rendered with Jinja2.

## Features

- User registration and login
- Post creation and viewing
- Liking posts
- Database integration with SQLite
- Template rendering with Jinja2

## Getting Started

### Prerequisites

- Python 3.7+
- FastAPI
- SQLAlchemy
- Jinja2
- Uvicorn

### Installation

1. **Clone the repository**:

   ```bash
   git clone <repository-url>
   cd social-media-backend
   ```

2. **Create a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

### Running the App

1. **Start the application**:

   ```bash
   uvicorn main:app --reload
   ```

2. **Access the app**:

   Open your browser and navigate to `http://127.0.0.1:8000`.

## Usage

- **Home Page**: Navigate to the home page to see the available options.
- **Sign In**: Register a new account.
- **Login**: Log in with your existing account.
- **Create Post**: Create a new post once logged in.
- **View Posts**: View all posts and like them if you wish.
- **My Posts**: View and manage your posts.

## API Endpoints

- **GET /**: Main page.
- **GET /signin**: Sign-in page.
- **POST /signinaction**: Action for signing in.
- **GET /login**: Login page.
- **POST /loginaction**: Action for logging in.
- **GET /createpost**: Create post page.
- **POST /createpostaction**: Action for creating a post.
- **GET /myposts**: View user's posts.
- **GET /viewposts**: View all posts.
- **POST /like/{post_id}**: Like a post.
- **GET /delete_post/{post_id}**: Delete a post.



## Note

- Ensure the directory `html` contains your HTML templates (`index.html`, `signin.html`, `login.html`, `createpost.html`, `mypost.html`, `viewpost.html`).
- Ensure the `support.py` file contains your SQLAlchemy models `User`, `Post`, and `Like`.

Feel
