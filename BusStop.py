# BusStop and BusStops Classes
from math import sqrt
import string


class BusStop:
    #init instance from dictionary
    def __init__(self,dictionary: dict):
        self._name = dictionary["Name"]
        self._X = dictionary["X"]
        self._Y = dictionary["Y"]
        self._ID = dictionary["ID"]
        self._routes = [] 

    def addRoute(self, route):
        self._routes.append(route)
    
    def toString(self) -> string :
        txt = str(self._name) + " ID: " + str(self._ID)
        return txt
    

class BusStops:
    def __init__(self) -> None:
        self._list = []

    def add(self,stop_dict: dict):
        if not (self.contains_name(stop_dict["Name"]) and self.contains_ID(stop_dict["ID"])): #ID?
            self._list.append(BusStop(stop_dict))

    def addList(self,route_dict: list):
        for stop_dict in route_dict:
            self.add(stop_dict)

    def contains_name(self,busStop_name) -> bool:
        for stop in self._list:
            if busStop_name == stop._name:
                return True
        return False

    def contains_ID(self,busStop_ID) -> bool:
        for stop in self._list:
            if busStop_ID == stop._ID:
                return True
        return False


    def get_name(self,busStop_name) -> list[BusStop]:   
        stopslist = []
        for id in range(len(self._list)):
            if busStop_name == self._list[id]._name:
                stopslist.append(self._list[id])
        return stopslist

    def get_ID(self,busStop_ID) -> BusStop:   
        for id in range(len(self._list)):
            if busStop_ID == self._list[id]._ID:
                return self._list[id]


    def getRoute_Names(self,route: list) -> list[BusStop]:
        busStops = []
        for stop_name in route:
            if self.contains_name(stop_name):
                busStops.append(self.get_name(stop_name))
            else:
                raise Exception("Bus Stop not in List")
        return busStops

    def getRoute_ID(self,route: list) -> list[BusStop]:
        busStops = []
        for stop_ID in route:
            if self.contains_ID(stop_ID):
                busStops.append(self.get_ID(stop_ID))
            else:
                raise Exception("Bus Stop not in List")
        return busStops


    def closestStop(self,X,Y):
        distance = float('inf')
        closest_stop = 0
        for id in range(len(self._list)):
            new_distance = sqrt(pow(X-self._list[id]._X,2) + pow(Y-self._list[id]._Y,2))
            if new_distance < distance:
                closest_stop = self._list[id]
                distance = new_distance
        return closest_stop , distance

    def printBusStops(self):
        for stop in self._list:
            print(stop.toString())

