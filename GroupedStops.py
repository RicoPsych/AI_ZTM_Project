#groups stops by name
from BusStop import BusStop, BusStops
from Routes import Route


class GroupedStop:
    def __init__(self,stops: list[BusStop]) -> None:
        """Create Instance of GroupedStop with list of Bus Stops"""
        self._name = stops[0]._name
        self._stops = stops
        self._routes = []
        for stop in stops:
            for route in stop._routes:
                if route not in self._routes:
                    self._routes.append(route)
                    

class GroupedStops:
    def __init__(self,busStops: BusStops) -> None:
        """Group BusStops By name"""
        self._stops = []
        for stop in busStops._list:
            if not self.containsName(stop._name):
                self._stops.append(GroupedStop(busStops.get_name(stop._name)))

    def containsName(self,name) -> bool:
        """Check if list contains group with given name"""
        for stop in self._stops:
            if stop._name == name:
                return True
        return False

    def getByName(self,name) -> GroupedStop:
        """Get group of stops with given name"""
        for stop in self._stops:
            if stop._name == name:
                return stop        

    def getByStop(self,busStop: BusStop) -> GroupedStop:
        """Get group of stops that contains given Bus Stop"""
        for stop in self._stops:
            if busStop in stop._stops :
                return stop

    def getOtherRoutes(self, busStops: list[BusStop]) -> list[Route]:
        """Get list of routes that are connected with given list of bus stops"""
        connected_routes = []
        for stop in busStops:
            #expand list with new routes
            connected_routes = connected_routes + [x for x in self.getByStop(stop)._routes if x not in connected_routes]
        return connected_routes    

    def getCommonStops(self,route1,route2):
        """Get list of common stops of 2 given routes"""
        common_stops = []
        for stop in route1._route:
            if route2 in self.getByStop(stop)._routes:
                common_stops.append(self.getByStop(stop))
        return common_stops

    def printAll(self):
        """Print all groupes of stops with connected routes"""
        for stop in self._stops:
            txt ="" + stop._name+" : "
            for route in stop._routes:
                txt += str(route._nr) +" "
            print(txt)