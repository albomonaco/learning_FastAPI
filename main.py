from typing_extensions import ParamSpecArgs
from fastapi import FastAPI, datastructures
from typing import Optional
from pydantic import BaseModel
import uvicorn

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
    published: bool


@app.post("/myblogs")
def create_blog(request:Blog):
    if request.published:
        return {'data':{'title':request.title,'body': request.body,'published': "Your blog was published"}}
    else:
        return {'data':{'title':request.title,'body': request.body,'published': "Your blog was not published"}}





if __name__ == "__main__":
    uvicorn.run(app,host="127.0.0.1",port=9000)