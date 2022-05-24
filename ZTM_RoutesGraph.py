import matplotlib.pyplot as pl 

from BusStop import BusStops
from GroupedStops import GroupedStops
from Routes import Routes
from LoadData import stops,routes

# connection_graph = []

# for route in routes._list:
#     x = [route]
#     y = route.getConnectedRoutes()
#     z = []
#     zz = []
#     for s in y: 
#         if s._nr not in zz:
#             z.append(s)
#             zz.append(s._nr)

#     x.append(z)
#     connection_graph.append(x)

# for connection in connection_graph:
#     txt = connection[0].toStringNR()[:-1]+":"
#     for route in connection[1]:
#         txt += " " + str(route._nr)
#     print(txt)

# for trip in routes.get_Nr(10):
#     for route in routes.get_Nr(148):
#         for stop in trip.getCommonStops(route):
#             print(stop.toString())

#     for route in routes.get_Nr(412):
#         for stop in trip.getCommonStops(route):
#             print(stop.toString())

#Domeyki ????
Graph = GroupedStops(stops)
Graph.printAll()
pass