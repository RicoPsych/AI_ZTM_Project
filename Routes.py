#Route and Routes Classes

from BusStop import BusStop 

class Route:
    pass

class Route:
    def __init__(self,route_dict: dict) -> None :  
        self._nr = route_dict["Nr"]
        self._id = route_dict["ID"]
        self._direction = route_dict["Direction"]
        self._route = route_dict["Route"]
        self._other_routes = []
        self.addRouteToBusStop()
        self.setConnectedRoutes()

    def addRouteToBusStop(self):
        for stopid in range(len(self._route)):  
            self._route[stopid].addRoute(self)

    def setConnectedRoutes(self):
        for busStop in self._route:                                                 #for all bus Stops in route
            for route in busStop._routes:                              #test v             #for all routes in each bus stops
                if route not in self._other_routes and route != self and route._nr != self._nr:               #if not in list add to list
                    self._other_routes.append(route)
                    route._other_routes.append(self)                                #add to this route to the other route
    
    def getConnectedRoutes(self) -> list[Route]:
        return self._other_routes          

    def getCommonStops(self,otherRoute) -> list[BusStop]:
        if self not in otherRoute._other_routes:    return []
        else:                                       return [stop for stop in self._route if stop in otherRoute._route ]
    
    def toStringNR(self):
        txt = "Route nr: " + str(self._nr) + "\n"
        return txt
    def toString(self):
        txt = "Route nr: " + str(self._nr) + "\nBus Stops:\n"
        for stop in self._route:
            txt += stop.toString() + "\n"
        txt += "Connected With:\n"
        for route in self._other_routes:
            txt += str(route._nr) + "\n"
        return txt

    def getStops(self) -> list[BusStop]:
        return self._route

class Routes:
    def __init__(self) -> None:
        self._list = []

    def add(self,route_dict: dict):
        # #test
        if self.contains_NR(route_dict["Nr"]):
            new_trip = Route(route_dict)
            existing_trip = self.get_Nr(route_dict["Nr"]).pop()
            if len(new_trip._route) > len(existing_trip._route):
                self._list.remove(existing_trip)
                self._list.append(new_trip)       
        #test
        elif not ( self.contains(route_dict["Nr"],route_dict["ID"]) ):
            self._list.append(Route(route_dict))

    def addList(self,routes_dict: list):
        for route_dict in routes_dict:
            self.add(route_dict)

    def contains(self,route_nr,route_id) -> bool:
        for route in self._list:
            if route_nr == route._nr and route_id == route._id:
                return True
        return False

    def contains_NR(self,route_nr) -> bool:
        for route in self._list:
            if route_nr == route._nr:
                return True
        return False

    def contains_ID(self,route_id) -> bool:
        for route in self._list:
            if route_id == route._id:
                return True
        return False

    def get_Nr(self,route_Nr) -> list[Route]:
        trips = []   
        for id in range(len(self._list)):
            if route_Nr == self._list[id]._nr:
                trips.append(self._list[id])
        return trips

    def get_ID(self,route_ID) -> Route:   
        for id in range(len(self._list)):
            if route_ID == self._list[id]._id:
                return self._list[id]

    def printRoutes(self):
        for route in self._list:
            print(route.toString())

