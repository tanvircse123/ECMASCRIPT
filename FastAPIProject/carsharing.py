from datetime import datetime
from fastapi import FastAPI,HTTPException
from  schemas import Car, load_db,save_db,CarOutputDTO,Trip,TripOutputDTO,CarNested
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
    return [car for car in db if car.size==size]


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
def car_by_id(id:int):
    result = [car for car in db if car.id== id]
    if result:
        return result[0]
    else:
        raise HTTPException(status_code=404,detail="Item not Found")
    


@app.post("/api/cars",response_model=CarOutputDTO)
def add_car(car:Car)-> CarOutputDTO:
    new_car = CarOutputDTO(size=car.size,doors=car.doors,fuel=car.fuel,transmission=car.transmission,id=len(db)+1)
    db.append(new_car) # add the car in the list with the append
    save_db(db) ## then save the entire list into json/remember entire list
    return new_car
    



@app.delete("/api/cars/{id}",status_code=204)
def remove_car(id:int)->None:
    matches = [car for car in db if car.id == id];
    if matches:
        car = matches[0]
        db.remove(car)
        save_db(db)
    else:
        raise HTTPException(status_code=404,detail="car not found")

@app.put("/api/cars/{id}",response_model=CarOutputDTO)
def update_car(id:int,new_car:Car) -> CarOutputDTO:
    matches = [car for car in db if car.id == id];
    if matches:
        car = matches[0]
        car.fuel = new_car.fuel
        car.size = new_car.size
        car.doors = new_car.doors
        car.transmission = new_car.transmission
        save_db(db)
        return car
    else:
        raise HTTPException(status_code=404,detail="Car not Found")
    

# adding nested information 
@app.post("/api/cars/{car_id}/trips",response_model=TripOutputDTO)
def add_trip(car_id:int,trip:Trip)-> TripOutputDTO:
    #find the car first
    matches = [car for car in db if car.id == car_id]
    if matches:
        car = matches[0]
        new_trip = TripOutputDTO(id=len(car.trips)+1,start=trip.start,end=trip.end,description=trip.description)
        car.trips.append(new_trip)
        save_db(db)
        return new_trip
    else:
        raise HTTPException(status_code=404,detail="car not Found")
    
# nested post
@app.post("/api/nestedcarpost")
def add_nested_trip(carnested:CarNested)->CarOutputDTO:
    new_car = CarOutputDTO(id=len(db)+1,size=carnested.size,fuel=carnested.fuel,transmission=carnested.transmission,doors=carnested.doors)
    
    trip_id = 1
    for trip in carnested.trips:
        new_trip = TripOutputDTO(id=trip_id,start=trip.start,end=trip.end,description=trip.description)
        new_car.trips.append(new_trip)
        trip_id+=1
    db.append(new_car)
    save_db(db)
    return new_car
    
#delete trip
@app.delete("/api/car/{car_id}/trips/{trip_id}")
def delete_trip(car_id:int,trip_id:int):
    matches = [car for car in db if car.id == car_id]
    if matches:
        # in the database there will be unique key
        car = matches[0]
        trip = [item for item in car.trips if item.id == trip_id]
        if trip:
            t = trip[0]
            car.trips.remove(t)
            save_db(db);
        else:
            raise HTTPException(status_code=404,detail="trip not found")
    else:
        raise HTTPException(status_code=404,detail="car not Found")
    

    