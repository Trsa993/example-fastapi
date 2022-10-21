from fastapi import FastAPI
from random import randrange
# import psycopg2
# from psycopg2.extras import RealDictCursor
from . import models
from .database import engine
from .routers import user, post, auth, vote
from .config import settings
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
) 

# while True:
#     try:
#         conn = psycopg2.connect(host="localhost", database="fastapi", user="postgres", password="password", cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection was succesful")
#         break
#     except Exception as error:
#         print("Connectiong to database failed!")
#         print("Error", error)
#         time.sleep(2)


# my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, {
#     "title": "title of post 2", "content": "content of post 2", "id": 2}]


# def find_post(id):
#     for p in my_posts:
#         if p["id"] == id:
#             return p


# def find_index(id):
#     for i, p in enumerate(my_posts):
#         if p["id"] == id:
#             return i

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

def generate_html_response():
    html_content = """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

@app.get("/")
def root():
    return {"message": "Hello World!!!"}


