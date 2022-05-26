from copy import copy
import matplotlib.pyplot as pl 
from GroupedStops import GroupedStops

from LoadData import stops,routes
from Routes import Route

def startSearch(start,end,limit):
    paths = []
    connected_routes = start._routes    
    for route in connected_routes:
        path = []
        path.append(route)
        #if route connected with end stop
        if any(x in route._route for x in end._stops):
            paths.append(path)
            continue
        rest_of_route = route.getRestOfRouteFromStop(start._stops)
        common_routes = gstops.getOtherRoutes(rest_of_route)
        common_routes = [x for x in common_routes if x not in path]
        GetPath(paths,path,route,common_routes,end,limit)
    return paths

def GetPath(paths,path, prev_route, routes, end, limit):
    if len(path)>= limit:
        return
    for route in routes:
        route: Route
        path_c = copy(path)
        path_c.append(route)
        #if route connected with end stop
        if any(x in route._route for x in end._stops):
            paths.append(path_c)
            continue
        #else
        common_stops = gstops.getCommonStops(prev_route,route)# get common stop in route with prev_route
        stop = common_stops.pop() #get last common stop in both routes
        rest_of_stops_in_route = route.getRestOfRouteFromStop(stop._stops)
        common_routes = gstops.getOtherRoutes(rest_of_stops_in_route)
        common_routes = [x for x in common_routes if x not in path_c]
        GetPath(paths,path_c, route ,common_routes,end,limit)


gstops = GroupedStops(stops)
start = gstops.getByName("Harfowa")                        #stops.closestStop(x1,y1))
end = gstops.getByName("Łostowice Świętokrzyska")                          #stops.closestStop(x2,y2))

Paths = startSearch(start,end,2)



for route in Paths:
    txt = ""
    for x in route:
        txt+=x.NR()
    print(txt)
pass