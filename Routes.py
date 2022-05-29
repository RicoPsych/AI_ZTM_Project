#Route and Routes Classes

from math import sqrt
from BusStop import BusStop, BusStops 

class Route:
    pass

class Route:
    def __init__(self,route_dict: dict) -> None : 
        """Create Route from dictionary""" 
        self._nr = route_dict["Nr"]
        self._id = route_dict["ID"]
        self._direction = route_dict["Direction"]
        self._route = route_dict["Route"] #ID's of Bus stops
        self._other_routes = []
        #connectToBusStops

    def connectToBusStops(self,busStops: BusStops):
        """Connect Route with BusStops and add route to those busStops"""
        self._route = busStops.getRoute_ID(self._route) #change ID's to reference to BusStops
        self.addRouteToBusStop()
        self.setConnectedRoutes()

    def addRouteToBusStop(self):
        """Add self to BusStops in route"""
        for stopid in range(len(self._route)):  
            self._route[stopid].addRoute(self)

    def setConnectedRoutes(self):
        """Set routes that are connected via BusStops"""
        for busStop in self._route:                                                 #for all bus Stops in route
            for route in busStop._routes:                              #test v             #for all routes in each bus stops
                if route not in self._other_routes and route != self and route._nr != self._nr:               #if not in list add to list
                    self._other_routes.append(route)
                    route._other_routes.append(self)                                #add to this route to the other route
    
    def getConnectedRoutes(self) -> list[Route]:
        """Get list of connected routes to this route"""
        return self._other_routes          

    def getCommonStops(self,otherRoute) -> list[BusStop]:
        """Get common stops with other route"""
        if self not in otherRoute._other_routes:    return []
        else:                                       return [stop for stop in self._route if stop in otherRoute._route ]
    
    def NR(self):
        """Return Route NR"""
        txt = "Route nr: " + str(self._nr) + "\n"
        return txt

    def toString(self):
        """To string"""
        txt = "Route nr: " + str(self._nr) + "\nBus Stops:\n"
        for stop in self._route:
            txt += stop.toString() + "\n"
        txt += "Connected With:\n"
        for route in self._other_routes:
            txt += str(route._nr) + "\n"
        return txt

    def getRoute(self) -> list[BusStop]:
        """return route"""
        return self._route
    
    def getRestOfRouteFromStop(self,stops: list[BusStop]) -> list[BusStop]:
        """Get Part of Route from stop in given list stop(made for GroupedStop._stops) to end"""
        for stop in stops:
            if stop in self._route: 
               return self._route[self._route.index(stop):] #get route from stop to end

    def getPartOfRoute(self,stops1: list[BusStop],stops2: list[BusStop]):
        """Get Part of Route from stop in given list(made for GroupedStop._stops) to stop in other given list"""
        for stop in stops1:
            if stop in self._route:
                stop1 = stop
                break
        for stop in stops2:
            if stop in self._route: 
                stop2 = stop
                break
        return self._route[self._route.index(stop1) : self._route.index(stop2)+1]
    ##-------------------------------------------------------------------------------------TODO
    def getLength(self,stops1: list[BusStop] = 0, stops2 : list[BusStop] = 0):
        """Calculate length of route"""
        if stops1 == 0:
            stops1 = [self._route[0]]
        if stops2 == 0:
            stops2 = [self._route[-1]]
        route = self.getPartOfRoute(stops1,stops2)
        length = 0
        for id in range(1,len(route)):
            x = (route[id-1]._X - route[id]._X)
            y = (route[id-1]._Y - route[id]._Y)
            length += sqrt(x*x + y*y) 
        return length * 111.139

class Routes:
    def __init__(self) -> None:
        self._list = []

    def add(self,route_dict: dict):
        """Add route from dictionary to list"""
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
        """Add List of routes dictionaries to Routes List"""
        for route_dict in routes_dict:
            self.add(route_dict)
        for route in self._list:
            #connects each route to bus stops
            route.connectToBusStops(busStops)

    
    def contains(self,route_nr,route_id) -> bool:
        """Check if list contains route with given id and nr"""
        for route in self._list:
            if route_nr == route._nr and route_id == route._id:
                return True
        return False


    def contains_NR(self,route_nr) -> bool:
        """Check if list contains route with given nr"""
        for route in self._list:
            if route_nr == route._nr:
                return True
        return False


    def contains_NR_Direction(self,route_nr,direction) -> bool:
        """Check if list contains route with given nr and direction"""
        for route in self._list:
            if route_nr == route._nr and direction == route._direction:
                return True
        return False
   
    def contains_ID(self,route_id) -> bool:
        """Check if list contains route with given id"""
        for route in self._list:
            if route_id == route._id:
                return True
        return False

    def get_Nr(self,route_Nr) -> list[Route]:
        """Get list of route trips with given Nr"""
        trips = []   
        for id in range(len(self._list)):
            if route_Nr == self._list[id]._nr:
                trips.append(self._list[id])
        return trips

    def get_Nr_Direction(self,route_Nr,direction) -> list[Route]:
        """Get list of route trips with given Nr and direction"""
        trips = []   
        for id in range(len(self._list)):
            if route_Nr == self._list[id]._nr and direction == self._list[id]._direction:
                trips.append(self._list[id])
        return trips


    def get_ID(self,route_ID) -> Route:   
        """Get route/trip with given ID"""
        for id in range(len(self._list)):
            if route_ID == self._list[id]._id:
                return self._list[id]

    def printRoutes(self):
        """Print all routes from list to console"""
        for route in self._list:
            print(route.toString())

