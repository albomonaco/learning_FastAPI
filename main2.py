from fastapi import FastAPI

#uvicorn name_file:name_of_FastApi()

app = FastAPI()

#@app.operation("path")
#the function (in this case "index") is called path operation function.
#app = path operation decorator.

@app.get("/")
def index():
    return {"data": "blog list"}

@app.get("/blog/{id}")
def show():
    return {"data": "1"}

@app.get("/blog/{id}/{comments}")
def comments():
    return {"data": {"1","2"}}

