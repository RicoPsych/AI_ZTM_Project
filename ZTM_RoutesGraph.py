import matplotlib.pyplot as pl 

from base.GroupedStops import GroupedStops
from load.LoadData import stops,routes

# for trip in routes.get_Nr(10):
#     for route in routes.get_Nr(148):
#         for stop in trip.getCommonStops(route):
#             print(stop.toString())

#     for route in routes.get_Nr(412):
#         for stop in trip.getCommonStops(route):
#             print(stop.toString())

Graph = GroupedStops(stops)
Graph.printAll()
start_stop = Graph.getGroup(stops.closestStop(18,54)[0])
end_stop = Graph.getGroup(stops.closestStop(18,54)[0])
for stopp in start_stop._routes:
    print(stopp._nr)
pass