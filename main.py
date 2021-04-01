from fastapi import FastAPI
from pydantic import BaseModel


class Parameters(BaseModel):
    firstName: str
    lastName: str

app = FastAPI()


@app.get('/')
def shivamani():
    return "Hello world"


@app.post('/uploadProfile')
def nextFunc(params: Parameters):
    first_name = params.firstName
    last_name = params.lastName
    return f"Hello {first_name} {last_name}"