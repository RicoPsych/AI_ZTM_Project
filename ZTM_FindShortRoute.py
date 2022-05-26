import matplotlib.pyplot as pl 
from GroupedStops import GroupedStops

from LoadData import stops,routes


gstops = GroupedStops(stops)
start = gstops.getByName("Harfowa")                        #stops.closestStop(x1,y1))
end = gstops.getByName("Osowa PKP")                          #stops.closestStop(x2,y2))

for stop in gstops._stops:
    if len(stop._routes) == 0:
        pass

ShortestRoute = []

rous = routes.get_Nr(210)

connected_routes = start._routes
for route in connected_routes:
    if any(x in route._route for x in end._stops):
        ShortestRoute.append(route)

print(ShortestRoute)


pass