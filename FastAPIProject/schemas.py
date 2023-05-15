import json
from pydantic import BaseModel


# just like c# model
# this is a pyhon model
class Car(BaseModel):
    id:int
    size:str
    fuel:str| None = "electric"
    doors:int
    transmission:str | None = "auto"


# output is the list of car object
def load_db() -> list[Car]:
    """load a list of car objects from a JSON File"""
    with open("car.json") as f:
        return [Car.parse_obj(obj) for obj in json.load(f)]
     
    
def save_db(cars:list[Car]):
    """ it will take all the car as an input with the new car that you added
    then write it to the file car.json"""
    with open('car.json','w') as f:
        all_car = [car.dict() for car in cars]
        json.dump(all_car,f,indent=4)
        
    