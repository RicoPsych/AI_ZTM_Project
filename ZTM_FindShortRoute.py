from time import time
import matplotlib.pyplot as pl
from FindConnections import startSearch 
from GroupedStops import GroupedStops

from LoadData import stops,routes
from Routes import Route



gstops = GroupedStops(stops)
start = gstops.getByName("Damroki")                        #stops.closestStop(x1,y1))
end = gstops.getByName("Pomorska")                          #stops.closestStop(x2,y2))


Paths = startSearch(start,end,0,gstops)


x =[]
y= []
for stop in stops._list:
    x.append(stop._X)
    y.append(stop._Y)    
#pl.plot(x,y,"bo")

for route in Paths:

    pl.plot(x,y,"bo")
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
        
        lat =  []
        long = []
        for stop in rt.getPartOfRoute(prev_stop._stops, next_stop._stops):
            long.append(stop._X)
            lat.append(stop._Y)
            pl.annotate(stop._name,(stop._X,stop._Y))
        pl.plot(long,lat,"-",label=rt._nr)
        pl.legend()
        
        length += rt.getLength(prev_stop._stops, next_stop._stops)

        prev_route = rt
    print(length)
    pl.show()

pass
    
    
pass