from copy import copy
from base.GroupedStops import GroupedStops

from base.Routes import Route
#DFS
def startSearch(start,end,limit,gstops: GroupedStops):
    """Search for all paths between two stops
       :start,end - starting and ending stop
       :limit - limit for routes in path
       :gstops - GroupedStops - contains list of grouped BusStops
    """
    paths = []
    connected_routes = start._routes    
    for route in connected_routes:
        path = []
        path.append(route)

        if Exclude(route):
            continue

        #if route connected with end stop
        rest_of_route = route.getRestOfRouteFromStop(start._stops)
        if any(x in rest_of_route for x in end._stops):
            paths.append(path)
            continue
        common_routes = gstops.getOtherRoutes(rest_of_route)
        common_routes = [x for x in common_routes if x not in path]
        GetPath(paths,path,route,common_routes,end,limit ,gstops)

        #if didnt find any routes raise limit
    if len(paths) == 0: 
        return startSearch(start,end,limit+1,gstops)
    return paths

def GetPath(paths,path, prev_route, routes, end, limit, gstops: GroupedStops):
    """Recursive search for path
       :paths - list of all found paths
       :path  - current path, contains Routes
       :prev_route - previous found route
       :routes - list of next routes to research for end stop
       :end - end stop
       :limit - limit for size of path, how many routes in path
       :gstops - GroupedStops - contains list of grouped BusStops
    """
    if len(path)>= limit:
        return
    for route in routes:
        route: Route
        path_c = copy(path)
        path_c.append(route)

        if Exclude(route):
            continue


        common_stops = gstops.getCommonStops(prev_route,route)# get common stop in route with prev_route
        stop = common_stops.pop() #get last common stop in both routes
        rest_of_route = route.getRestOfRouteFromStop(stop._stops)#get rest of this route
        #if route connected with end stop
        if any(x in rest_of_route for x in end._stops):
            paths.append(path_c)
            continue

        #else get routes that are connected to rest of this route
        common_routes = gstops.getOtherRoutes(rest_of_route)
        common_routes = [x for x in common_routes if x not in path_c]
        GetPath(paths,path_c, route ,common_routes,end,limit,gstops)

def Exclude(route) -> bool:
    """Exclude Some Routes"""
    return route._nr >= 400 and route._nr < 500
