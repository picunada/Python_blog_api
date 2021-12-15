from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True


@app.get("/")
async def root():
    return {"message": "hello world"}


@app.get("/posts")
def get_posts():
    return {"data": "This is your post"}


@app.post("/create_post")
def create_post(post: Post):
    print(post)
    return {"new_post": f"title {post.title} content: {post.content}"}
