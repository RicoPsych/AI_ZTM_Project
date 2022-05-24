#groups stops by name
from BusStop import BusStop, BusStops


class GroupedStop:

    def __init__(self,stops: list[BusStop]) -> None:
        self._name = stops[0]._name
        self._stops = stops
        self._routes = []
        for stop in stops:
            for route in stop._routes:
                if route not in self._routes:
                    self._routes.append(route)
                    

class GroupedStops:
    def __init__(self,busStops: BusStops) -> None:
        self._stops = []
        for stop in busStops._list:
            if not self.containsName(stop._name):
                self._stops.append(GroupedStop(busStops.get_name(stop._name)))


    def containsName(self,name) -> bool:
        for stop in self._stops:
            if stop._name == name:
                return True
        return False

    def getGroup(self,busStop: BusStop) -> GroupedStop:
        for stop in self._stops:
            if stop._stops.contains(busStop):
                return stop

    def printAll(self):
        for stop in self._stops:
            txt ="" + stop._name+" : "
            for route in stop._routes:
                txt += str(route._nr) +" "
            print(txt)