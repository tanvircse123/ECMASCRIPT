import { Car }   from "../classes/Car.js";
import { Drone } from "../classes/Drone.js";
import { DataError } from "./DataError.js";
export class FleetDataService{
    constructor(){
        this.cars = [];
        this.drones = [];
        this.errors = [];
    }
    loadData(fleet){
        for(let data of fleet){
            if(data.type == 'car'){
                let car = this.loadCar(data);
                this.cars.push(car);
            }else if(data.type == 'drone') {
                let drone = this.loadDrone(data);
                this.drones.push(drone);
            }else{
                let e = new DataError('Invalid data Type',data);
                this.errors.push(e);
            }
        }
    }
    
    
    loadCar(data){
        try{
            let c   = new Car(data.license,data.model,data.latLong);
            c.miles = data.miles;
            c.make  = data.make;
            return c;
        }catch(e){
            this.errors.push(new DataError('Error Loading Car',data));
        }
        return null;
    }

    loadDrone(data){
        let d = new Drone(data.license,data.model,data.latLong);
        d.airTimeHours = data.airTimeHours;
        d.base = data.base;
        return d;
    }

    getCarByLicense(license){
        return this.cars.find(c => c.license == license);
    }

    filterCarsByMake(character){
        // if the character found /IndexOf character in string is greater than 0
        // then return the car
        return this.cars.filter(car=>car.make.indexOf(character)>=0);

    }
}