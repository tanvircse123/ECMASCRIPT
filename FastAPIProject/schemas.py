import json
from pydantic import BaseModel


# just like c# model
# this is a pyhon model
class Car(BaseModel):
    size:str
    fuel:str| None = "electric"
    doors:int
    transmission:str | None = "auto"



class Trip(BaseModel):
    start:int
    end:int
    description:str

class CarNested(Car):
    trips : list[Trip] = []

class TripOutputDTO(Trip):
    id:int

class CarOutputDTO(Car):
    id:int
    trips:list[TripOutputDTO] = []




# output is the list of car object
def load_db() -> list[CarOutputDTO]:
    """load a list of car objects from a JSON File
        we use the CarOutput because we need the Car id in the database
    """
    with open("car.json") as f:
        return [CarOutputDTO.parse_obj(obj) for obj in json.load(f)]
     
    
def save_db(cars:list[CarOutputDTO]):
    """ it will take all the car as an input with the new car that you added
    then write it to the file car.json"""
    with open('car.json','w') as f:
        all_car = [car.dict() for car in cars]
        # dump the dictionary it will be saved as a json
        json.dump(all_car,f,indent=4)
        
    