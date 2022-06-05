from time import time
from PlotPaths import CreateGraph, Plot
from algorithms.Astar import startSearch as Asearch
from algorithms.DFS import startSearch as DFSsearch
from base.GroupedStops import GroupedStops
from load.LoadData import stops


gstops = GroupedStops(stops)
start = gstops.getByName("Plac Wolności")                        #stops.closestStop(x1,y1))
end = gstops.getByName("Osowa PKP")                          #stops.closestStop(x2,y2))


tic = time()
Paths = DFSsearch(start,end,1,gstops)
print(time()-tic)
CreateGraph(Paths,start,end,gstops)

tic = time()
Paths = Asearch(start,end,1,gstops)
print(time()-tic)
CreateGraph(Paths,start,end,gstops)

Plot(Paths,start,end,gstops) 

pass