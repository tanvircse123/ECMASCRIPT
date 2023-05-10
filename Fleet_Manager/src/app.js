import { Car } from "./classes/Car.js";
import { Drone } from "./classes/Drone.js";
import { fleet } from "./fleet-data.js";
import { FleetDataService } from "./services/fleetDataService.js";

let dataService = new FleetDataService();
dataService.loadData(fleet);

let cars = dataService.filterCarsByMake('U');
console.log(cars);
