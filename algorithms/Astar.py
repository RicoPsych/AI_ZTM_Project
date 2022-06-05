from copy import copy
from base.GroupedStops import GroupedStop, GroupedStops

from base.Routes import Route
#DFS -> A* 
def startSearch(start:GroupedStop,end:GroupedStop,limit:int,gstops: GroupedStops):
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

        other_connected_routes = gstops.getOtherRoutes(rest_of_route)
        other_connected_routes = [x for x in other_connected_routes if x not in path]
        GetPath(paths, path, route, other_connected_routes, start ,end, limit, gstops)
        
        #if didnt find any routes raise limit
    if len(paths) == 0: 
        return startSearch(start,end,limit+1,gstops)
    paths.sort(key= lambda route: GetLengthForSort(route,start,end,gstops))
    return paths

def GetPath(paths, path, prev_route: Route, routes : list[Route], previous_stop : GroupedStop,end : GroupedStop, limit :int, gstops: GroupedStops):
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
    
    #Heuristic   
    routes.sort(key=lambda route: Heuristic(route,prev_route , previous_stop ,gstops.getCommonStops(prev_route,route).pop(),end))

    for route in routes[0:min(3,len(routes))]:
        path_c = copy(path)
        path_c.append(route)


        common_stops = gstops.getCommonStops(prev_route,route)# get common stop in route with prev_route
        stop = common_stops.pop() #get last common stop in both routes
        rest_of_route = route.getRestOfRouteFromStop(stop._stops) #get rest of this route
        #if route connected with end stop
        if any(x in rest_of_route for x in end._stops):
            paths.append(path_c)
            continue
        
        #else get routes that are connected to rest of this route
        common_routes = gstops.getOtherRoutes(rest_of_route)
        rt = []
        for x in common_routes: 
            is_in = False
            for p in path_c:
                if x._nr == p._nr:
                    is_in = True
                    break
            if not is_in and not Exclude(x):
                rt.append(x)
        common_routes = rt
        GetPath(paths,path_c, route ,common_routes, stop ,end,limit,gstops)

#exclude night buses
def Exclude(route) -> bool:
    return route._nr >= 400 and route._nr < 500

def Heuristic(route: Route,prev_route: Route,prev_stop:GroupedStop,stop:GroupedStop,end:GroupedStop) -> float:
    rest_of_route = route.getRestOfRouteFromStop(stop._stops)
    
    length = prev_route.getLength(prev_stop._stops,stop._stops) # len(prev_route.getPartOfRoute(prev_stop._stops,stop._stops)) #
    x = 0
    if Exclude(route):
        x += 5000
    if any(x in rest_of_route for x in end._stops):
        x += -2000
    return  ((stop.distanceFrom(end) - prev_stop.distanceFrom(end))* length + x )

def GetLengthForSort(route,start,end,gstops):
    length= 0
    prev_stop = start
    for rt in route:
        rt: Route
        
        if route.index(rt) != 0:
            prev_stop = gstops.getCommonStops(prev_route,rt).pop()    
        if route.index(rt) < len(route)-1:
            next_stop = gstops.getCommonStops(rt,route[route.index(rt)+1]).pop()
        else:
            next_stop = end

        length += rt.getLength(prev_stop._stops, next_stop._stops)

        prev_route = rt
    return length
 