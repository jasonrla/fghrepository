#Python
from typing import Optional
from fastapi.datastructures import Default
from fastapi.param_functions import Query

#Pydantic
from pydantic import BaseModel

#FastAPI
from fastapi import FastAPI, Body, Query

app = FastAPI()

class Person(BaseModel):
    first_name: str
    last_name: str
    age: int
    hair_color: Optional[str] = None
    is_married: Optional[bool] = None

@app.get("/")
def home():
    return {"hello":"world"}

#Request and Response Body

@app.post("/person/new")
def create_person(person:Person = Body(...)):
    return person

#Validaciones: Query Parameters
@app.get("/person/detail")
def show_person(
    name: Optional[str] = Query(None, min_length = 1, max_length = 50),
    age: Optional[int] = Query(None, ge=18)
):
    return {name: age}