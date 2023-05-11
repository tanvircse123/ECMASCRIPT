import { Car } from "./classes/Car.js";
import { Drone } from "./classes/Drone.js";
import { fleet } from "./fleet-data.js";
import { FleetDataService } from "./services/fleetDataService.js";
import axios from '../node_modules/axios/dist/axios.js';
let dataService = new FleetDataService();
dataService.loadData(fleet);
console.log(dataService.cars);
console.log(dataService.drones);