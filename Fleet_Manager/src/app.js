import { Car } from "./classes/Car.js";
import { Drone } from "./classes/Drone.js";
import { fleet } from "./fleet-data.js";
import { FleetDataService } from "./services/fleetDataService.js";
let url = "https://raw.githubusercontent.com/tanvircse123/ECMASCRIPT/main/Fleet_Manager/src/data.json";
let response;
fetch(url)
.then(res =>res.json()
)
.then(data=>{ 
    this.response = data;
    let dataService = new FleetDataService();
    dataService.loadData(data);
    //console.log(dataService.cars);
    //console.log(dataService.drones);
})
console.log(this.response);
// let dataService = new FleetDataService();
// dataService.loadData(fleet);
