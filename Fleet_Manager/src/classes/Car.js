import { Vehicle } from "./Vehicle.js";
export class Car extends Vehicle{
    constructor(lisense,model,latlong){
        super(lisense,model,latlong);
        this.miles = null;
        this.make = null;
    }
}