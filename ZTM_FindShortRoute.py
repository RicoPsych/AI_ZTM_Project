from time import time
import matplotlib.pyplot as pl
from algorithms.Astar import startSearch as Asearch
from algorithms.DFS import startSearch as DFSsearch
from base.GroupedStops import GroupedStops

from load.LoadData import stops,routes
from base.Routes import Route


def CreateGraph(Paths,start,end):
    txt="digraph Paths {\""+start._name+"\", \""+end._name+"\" [shape=diamond]\n"
    for path in Paths:
        txt += "\"" + start._name + "\" -> "
        for route in path:
            txt += route.NR() + " -> "
        txt += "\"" + end._name + "\"\n"
    txt+="}"
    graph = open("graph.dot","w")
    graph.write(txt)    
    graph.close()
 

gstops = GroupedStops(stops)
start = gstops.getByName("Plac Wolności")                        #stops.closestStop(x1,y1))
end = gstops.getByName("Osowa PKP")                          #stops.closestStop(x2,y2))


tic = time()
Paths = DFSsearch(start,end,2,gstops)
print(time()-tic)

CreateGraph(Paths,start,end)
tic = time()
Paths = Asearch(start,end,2,gstops)
print(time()-tic)
CreateGraph(Paths,start,end)

img = pl.imread('resources/map.png')
pl.imshow(img,extent=[18.34,18.95,54.25,54.49])

x = []
y = []
for stop in stops._list:
    x.append(stop._X)
    y.append(stop._Y)    
#pl.plot(x,y,"bo")

for route in Paths:

    pl.plot(x,y,"bo",markersize="0.5")
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