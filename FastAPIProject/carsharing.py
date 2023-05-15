from datetime import datetime
from fastapi import FastAPI
app = FastAPI()


db = [
    {
        "size": "s",
        "fuel": "gasoline",
        "doors": 3,
        "transmission": "auto",
        "trips": [
            {
                "start": 0,
                "end": 5,
                "description": "Groceries",
                "id": 1
            },
            {
                "start": 5,
                "end": 218,
                "description": "Commute Amsterdam-Rotterdam",
                "id": 2
            },
            {
                "start": 218,
                "end": 257,
                "description": "Weekend beach trip",
                "id": 3
            }
        ],
        "id": 1
    },
    {
        "size": "s",
        "fuel": "electric",
        "doors": 3,
        "transmission": "auto",
        "trips": [
            {
                "start": 0,
                "end": 34,
                "description": "Taking dog to the vet",
                "id": 4
            },
            {
                "start": 34,
                "end": 125,
                "description": "Meeting Customer in Utrecht",
                "id": 5
            }
        ],
        "id": 2
    },
    {
        "size": "s",
        "fuel": "gasoline",
        "doors": 5,
        "transmission": "manual",
        "trips": [],
        "id": 3
    },
    {
        "size": "m",
        "fuel": "electric",
        "doors": 3,
        "transmission": "auto",
        "trips": [
            {
                "start": 0,
                "end": 100,
                "description": "Visiting mom",
                "id": 6
            }
        ],
        "id": 4
    },
    {
        "size": "m",
        "fuel": "gasoline",
        "doors": 5,
        "transmission": "manual",
        "trips": [],
        "id": 6
    },
    {
        "size": "l",
        "fuel": "diesel",
        "doors": 5,
        "transmission": "manual",
        "trips": [],
        "id": 7
    },
    {
        "size": "l",
        "fuel": "electric",
        "doors": 5,
        "transmission": "auto",
        "trips": [],
        "id": 8
    },
    {
        "size": "l",
        "fuel": "hybrid",
        "doors": 5,
        "transmission": "auto",
        "trips": [
            {
                "start": 0,
                "end": 55,
                "description": "Forest walk",
                "id": 7
            }
        ],
        "id": 9
    },
    {
        "size": "xl",
        "fuel": "electric",
        "doors": 5,
        "transmission": "auto",
        "trips": [],
        "id": 10
    }
]



@app.get("/")
def welcome():
    return {"message":"Welcome to car sharing service"}

# get by query parameter
# example : http://localhost:8000/helloquery?name=Tanvir
@app.get("/helloquery")
def hello(name):
    return {"message":f"Hello {name}"}
# get by path parameter
@app.get("/date")
def getDate():
    return {"date":datetime.now()}







@app.get("/api/cars")
def get_cars():
    return db

@app.get("/api/getcarbysize")
def getCarBySize(size):
    return [car for car in db if car['size']==size]


# we can combine two function into one

@app.get("/api/getcars")
def cars(size: str|None = None,doors:int|None = None)-> list:
    result  = db
    if size:
        result =  [car for car in db if car['size']==size]
    if doors:
        result =  [car for car in db if car['doors']== doors]    
    return result

@app.get("/api/cars/{id}")
def car_by_id(id:int) -> dict:
    result = [car for car in db if car['id'] == id]
    return result[0] ## first or default