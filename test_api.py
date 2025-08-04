from fastapi import FastAPI
from enum import Enum

app = FastAPI()

@app.get("/hello/{name}")
async def root(name):
    return f"Welcome to my api server: {name}"


class data_check(str,Enum):
    indian = "indian",
    american ="american",
    chinese ="chinese"


data={
    "indian":["samosa","pani puri","jalebi"],
    "american":["hotdog","pizza","burger"],
    "chinese":["chawmin","spring roll"]
}


@app.get("/food/{type}")
async def food_data(type:data_check):
    #return data.get(type) if type in data else {"error": "given type is not available in the menu"}
    return data.get(type)


offer={
        1:"20%",
        2:"40%",
        3:"60%"
       }

@ app.get("/offer/{number}")

async def offer_function(number:int):
    return offer.get(number)
# # create  do to list 
# list =[]

# @app.post("/list")

# def post_create(item:str):
#     list.append(item)
#     return item


