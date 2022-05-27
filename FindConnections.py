from copy import copy
from GroupedStops import GroupedStops

from Routes import Route

def startSearch(start,end,limit,gstops: GroupedStops):
    paths = []
    connected_routes = start._routes    
    for route in connected_routes:
        path = []
        path.append(route)
        #if route connected with end stop

        rest_of_route = route.getRestOfRouteFromStop(start._stops)

        if any(x in rest_of_route for x in end._stops):
            paths.append(path)
            continue
        common_routes = gstops.getOtherRoutes(rest_of_route)
        common_routes = [x for x in common_routes if x not in path]
        GetPath(paths,path,route,common_routes,end,limit ,gstops)
    return paths

def GetPath(paths,path, prev_route, routes, end, limit, gstops: GroupedStops):
    if len(path)>= limit:
        return
    for route in routes:
        route: Route
        path_c = copy(path)
        path_c.append(route)
        #if route connected with end stop

        #else
        common_stops = gstops.getCommonStops(prev_route,route)# get common stop in route with prev_route
        stop = common_stops.pop() #get last common stop in both routes
        rest_of_route = route.getRestOfRouteFromStop(stop._stops)

        if any(x in rest_of_route for x in end._stops):
            paths.append(path_c)
            continue

        common_routes = gstops.getOtherRoutes(rest_of_route)
        common_routes = [x for x in common_routes if x not in path_c]
        GetPath(paths,path_c, route ,common_routes,end,limit,gstops)
