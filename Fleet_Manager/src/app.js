import { Car } from "./classes/Car.js";
import { Drone } from "./classes/Drone.js";
import { fleet } from "./fleet-data.js";
import { FleetDataService } from "./services/fleetDataService.js";
let url = "https://raw.githubusercontent.com/tanvircse123/ECMASCRIPT/main/Fleet_Manager/src/data.json";
fetch(url)
.then(res =>res.json()
)
.then(data=>{ 
    let dataService = new FleetDataService();
    dataService.loadData(data);
    console.log(dataService.cars);
    console.log(dataService.drones);
})

// let dataService = new FleetDataService();
// dataService.loadData(fleet);
