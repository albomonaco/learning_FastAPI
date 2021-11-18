from fastapi import FastAPI, datastructures
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


@app.get("/blog")
def show(): 
   return {"data":"{} blogs from my blog list".format(1)}


@app.get("/blog/{id}")
def show(id: int):
    return {"data":id}


@app.get("/blog/unpublished")
def unpublished():
    return {"data":"all the unpublished posts"}


@app.get("/blog/{id}/comments")
def comments(id,limit:int):
    return {"data": {"1","2", limit}}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

