from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Input(BaseModel):
    a: int
    b: int

@app.post("/sum")
def add_numbers(input: Input):
    return {"result": input.a + input.b}
