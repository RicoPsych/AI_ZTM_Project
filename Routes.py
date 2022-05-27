#Route and Routes Classes

from BusStop import BusStop, BusStops 

class Route:
    pass

class Route:
    def __init__(self,route_dict: dict) -> None :  
        self._nr = route_dict["Nr"]
        self._id = route_dict["ID"]
        self._direction = route_dict["Direction"]
        self._route = route_dict["Route"] #ID's of Bus stops
        self._other_routes = []
        #connectToBusStops

    def connectToBusStops(self,busStops: BusStops):
        self._route = busStops.getRoute_ID(self._route) #change ID's to reference to BusStops
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
    
    def NR(self):
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

    def getRoute(self) -> list[BusStop]:
        return self._route
    
    def getRestOfRouteFromStop(self,stops: list[BusStop]) -> list[BusStop]:
        for stop in stops:
            if stop in self._route: 
               return self._route[self._route.index(stop):] #get route from stop to end

    def getPartOfRoute(self,stops1: list[BusStop],stops2: list[BusStop]):
        for stop in stops1:
            if stop in self._route:
                stop1 = stop
                break
        for stop in stops2:
            if stop in self._route: 
                stop2 = stop
                break
        return self._route[self._route.index(stop1) : self._route.index(stop2)+1]

class Routes:
    def __init__(self) -> None:
        self._list = []

    def add(self,route_dict: dict):
        # #test----------------------------------------------------------------------------------------
        if self.contains_NR(route_dict["Nr"]):
            if not self.contains_NR_Direction(route_dict["Nr"],route_dict["Direction"]):
                self._list.append(Route(route_dict))
            else:
                new_trip = Route(route_dict)
                for existing_trip in self.get_Nr(route_dict["Nr"]):
                    #if direction equal check length
                    if new_trip._direction == existing_trip._direction: 
                        if len(new_trip._route) > len(existing_trip._route):
                            self._list.remove(existing_trip)
                            self._list.append(new_trip)       
        # #test----------------------------------------------------------------------------------------
        elif not ( self.contains(route_dict["Nr"],route_dict["ID"]) ):
            self._list.append(Route(route_dict))

    def addList(self,routes_dict: list,busStops: BusStops):
        for route_dict in routes_dict:
            self.add(route_dict)
        for route in self._list:
            route.connectToBusStops(busStops)

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

    def contains_NR_Direction(self,route_nr,direction) -> bool:
        for route in self._list:
            if route_nr == route._nr and direction == route._direction:
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

    def get_Nr_Direction(self,route_Nr,direction) -> list[Route]:
        trips = []   
        for id in range(len(self._list)):
            if route_Nr == self._list[id]._nr and direction == self._list[id]._direction:
                trips.append(self._list[id])
        return trips


    def get_ID(self,route_ID) -> Route:   
        for id in range(len(self._list)):
            if route_ID == self._list[id]._id:
                return self._list[id]

    def printRoutes(self):
        for route in self._list:
            print(route.toString())

