from time import time
from PlotPaths import CreateGraph, Plot
from algorithms.Astar import startSearch as Asearch
from algorithms.DFS import startSearch as DFSsearch
from base.GroupedStops import GroupedStops
from load.LoadData import stops


gstops = GroupedStops(stops)
start = gstops.getByName("Myśliwska")                        #stops.closestStop(x1,y1))
end = gstops.getByName("Hucisko")                          #stops.closestStop(x2,y2))


tic = time()
Paths = DFSsearch(start,end,2,gstops)
print(time()-tic)
CreateGraph(Paths,start,end,gstops)
CreateGraph(Paths,start,end,gstops,graph_stops=True)

tic = time()
Paths = Asearch(start,end,1,gstops)
print(time()-tic)

CreateGraph(Paths,start,end,gstops,graph_stops=False)
CreateGraph(Paths,start,end,gstops,graph_stops=True)

Plot(Paths,start,end,gstops) 

pass