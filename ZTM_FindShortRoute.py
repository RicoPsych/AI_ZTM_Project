from time import time
import matplotlib.pyplot as pl
from FindConnections import startSearch 
from GroupedStops import GroupedStops

from LoadData import stops,routes
from Routes import Route



gstops = GroupedStops(stops)
start = gstops.getByName("Harfowa")                        #stops.closestStop(x1,y1))
end = gstops.getByName("Zabytkowa")                          #stops.closestStop(x2,y2))


tic = time()
Paths = startSearch(start,end,2,gstops)
toc = tic - time()

print(toc)

tic = time()
Paths = startSearch(start,end,3,gstops)
toc = tic - time()

print(toc)

x =[]
y= []
for stop in stops._list:
    x.append(stop._X)
    y.append(stop._Y)    


# for route in Paths:

#     pl.plot(x,y,"bo")
    
#     prev_stop = start
#     for rt in route:
#         rt: Route
        
#         if route.index(rt) != 0:
#             prev_stop = gstops.getCommonStops(prev_route,rt).pop()    
#         if route.index(rt) < len(route)-1:
#             next_stop = gstops.getCommonStops(rt,route[route.index(rt)+1]).pop()
#         else:
#             next_stop = end
        
#         lat =  []
#         long = []
#         for stop in rt.getPartOfRoute(prev_stop._stops, next_stop._stops):
#             long.append(stop._X)
#             lat.append(stop._Y)
#             pl.annotate(stop._name,(stop._X,stop._Y))
        
#         pl.plot(long,lat,"-",label=rt._nr)
#         pl.legend()
#         prev_route = rt
#     pl.show()
#     pass
    
    
pass