# BusStop and BusStops Classes
from math import sqrt
import string


class BusStop:
    def __init__(self,dictionary: dict):
        """Create BusStop instance from dictionary"""
        self._name = dictionary["Name"]
        self._X = dictionary["X"]
        self._Y = dictionary["Y"]
        self._ID = dictionary["ID"]
        self._routes = [] 

    def addRoute(self, route):
        """Add route to conneted routes"""
        self._routes.append(route)
    
    def toString(self) -> string :
        """To string"""
        txt = str(self._name) + " ID: " + str(self._ID)
        return txt
    

class BusStops:
    def __init__(self) -> None:
        self._list = []

    def add(self,stop_dict: dict) -> None:
        """Add new BusStop to list if it doesn't contain it"""
        if not (self.contains_name(stop_dict["Name"]) and self.contains_ID(stop_dict["ID"])): 
            self._list.append(BusStop(stop_dict))

    def addList(self,stops_dict: list) -> None:
        """Add List of BusStops from list of Dictionaries"""
        for stop_dict in stops_dict:
            self.add(stop_dict)

    def contains_name(self,busStop_name) -> bool:
        """Check if list contains stop with given name"""
        for stop in self._list:
            if busStop_name == stop._name:
                return True
        return False

    def contains_ID(self,busStop_ID) -> bool:
        """Check if list contains stop with given ID"""
        for stop in self._list:
            if busStop_ID == stop._ID:
                return True
        return False


    def get_name(self,busStop_name) -> list[BusStop]:   
        """Get list of stops from this list with given name"""
        stopslist = []
        for id in range(len(self._list)):
            if busStop_name == self._list[id]._name:
                stopslist.append(self._list[id])
        return stopslist

    def get_ID(self,busStop_ID) -> BusStop:   
        """Get BusStop with given ID"""
        for id in range(len(self._list)):
            if busStop_ID == self._list[id]._ID:
                return self._list[id]


    def getRoute_Names(self,route: list) -> list[BusStop]:
        """Get list of BusStops(Route) from list of busStop names names//REDUNDANT??"""
        busStops = []
        for stop_name in route:
            if self.contains_name(stop_name):
                busStops.append(self.get_name(stop_name))
            else:
                raise Exception("Bus Stop not in List")
        return busStops

    def getRoute_ID(self,route: list) -> list[BusStop]:
        """Get list of BusStops(Route) from list of Bus Stops IDs"""
        busStops = []
        for stop_ID in route:
            if self.contains_ID(stop_ID):
                busStops.append(self.get_ID(stop_ID))
            else:
                raise Exception("Bus Stop not in List")
        return busStops

    def closestStop(self,X,Y) -> BusStop and float:
        """Find closest stop from list to given coordinates"""
        distance = float('inf')
        closest_stop = 0
        for id in range(len(self._list)):
            new_distance = sqrt(pow(X-self._list[id]._X,2) + pow(Y-self._list[id]._Y,2))
            if new_distance < distance:
                closest_stop = self._list[id]
                distance = new_distance
        return closest_stop , distance

    def printBusStops(self) -> None:
        """Print all bus stops to console"""
        for stop in self._list:
            print(stop.toString())

