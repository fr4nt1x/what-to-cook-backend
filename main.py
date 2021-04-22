from fastapi import FastAPI
from database.db import DB
from schemas.meal import Meal

app = FastAPI()
db = DB('test.json')


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/all_meals")
def read_all_meals():
    return {"meals": db.get_all_meals()}


@app.post("/add_meal")
def add_meal(meal: Meal):
    return {"meals": db.add_meal(meal)}
