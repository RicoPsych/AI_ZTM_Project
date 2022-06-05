import matplotlib.pyplot as pl
from base.Routes import Route
from load.LoadData import stops

def CreateGraph(Paths,start,end,gstops):
    txt="digraph Paths {\""+start._name+"\", \""+end._name+"\" [shape=diamond]\n"
    for path in Paths:



        txt += "\"" + start._name + "\" -> "
        for route in path:
            txt += route.NR() + " -> "
            if path.index(route) < len(path)-1:
                next_stop = gstops.getCommonStops(route,path[path.index(route)+1]).pop()
                txt+= "\""+next_stop._name+"\" -> "
        
        txt += "\"" + end._name + "\"\n"
    txt+="}"
    graph = open("graph.dot","wb")
    graph.write(txt.encode("utf8"))    
    graph.close()
 

def Plot(Paths,start,end,gstops):
    
    img = pl.imread('resources/map.png')
  #  pl.imshow(img,extent=[18.34,18.95,54.25,54.49])

    x = []
    y = []
    for stop in stops._list:
        x.append(stop._X)
        y.append(stop._Y)   
    #pl.plot(x,y,"bo")

    for route in Paths:
        pl.imshow(img,extent=[18.34,18.95,54.25,54.49])
        pl.plot(x,y,"bo",markersize="0.5")
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
            prev_route = rt
        pl.show()