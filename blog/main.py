from fastapi import FastAPI
from . import models, schemas
from .database import engine
from sqlalchemy import Session

app = FastAPI()

models.Base.metadata.create_all(engine)

@app.post('/al')
def create(request:schemas.Blog, db:Session):
    return 1