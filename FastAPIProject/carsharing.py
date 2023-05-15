from datetime import datetime
from fastapi import FastAPI,HTTPException
from  schemas import load_db
app = FastAPI()


db = load_db()


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
        result =  [car for car in db if car.size==size]
    if doors:
        result =  [car for car in db if car.doors== doors]    
    return result

@app.get("/api/cars/{id}")
def car_by_id(id:int) -> dict:
    result = [car for car in db if car.id== id]
    if result:
        return result[0]
    else:
        raise HTTPException(status_code=404,detail="Item not Found")
    return result[0] ## first or default