from algorithms.Astar import startSearch as Asearch
from algorithms.DFS import startSearch as DFSsearch
from base.GroupedStops import GroupedStops
from load.LoadData import stops
import matplotlib.pyplot as pl
from base.Routes import Route
from genetic.run import genetic_run

class FullTrip():                           # used in genetic algo
    def __init__(self, start_stop, end_stop, full_path, length):
        self.start_stop = start_stop
        self.end_stop = end_stop
        self.full_path = full_path
        self.length = length

gstops = GroupedStops(stops)

stop_list = [gstops.getByName("Oliwa"),     # list of stops in full trip
            gstops.getByName("Karczemki"), 
            gstops.getByName("Platynowa"), 
            gstops.getByName("Brama Wyżynna"),
            gstops.getByName("Leszczynowa"),
            gstops.getByName("Emaus"), 
            gstops.getByName("Sobótki"), 
            gstops.getByName("Piekarnicza"),
            gstops.getByName("Chodowieckiego"),
            gstops.getByName("Siedlicka"), ]

connections_list = []                   # temp list, helps avoiding duplicates
connections_with_shortest_route = {}    # dictionary with calculated shortest routes
for stop1 in stop_list:
    for stop2 in stop_list:
        if stop1 != stop2 and {stop1, stop2} not in connections_list:
            connections_list.append({stop1, stop2})
            #print(stop1._name +" -> " + stop2._name)
            Paths = Asearch(stop1,stop2,1,gstops)
            connections_with_shortest_route[(stop1, stop2)] = Paths[0]


full_trip_list = []                     # will be passed to genetic algo
for stop_pair, routes in connections_with_shortest_route.items():
    full_length = 0
    prev_stop = stop_pair[0]
    for rt in routes:
        rt: Route
        if routes.index(rt) != 0:
            prev_stop = gstops.getCommonStops(prev_route,rt).pop()    
        if routes.index(rt) < len(routes)-1:
            next_stop = gstops.getCommonStops(rt,routes[routes.index(rt)+1]).pop()
        else:
            next_stop = stop_pair[1]                  
        # calculates trip length
        full_length += rt.getLength(prev_stop._stops, next_stop._stops)
        prev_route = rt

    full_trip_list.append(FullTrip(start_stop = stop_pair[0], end_stop = stop_pair[1], full_path = routes, length = full_length))
    #print(str(full_length) + " " + key[0]._name + " " + key[1]._name)

# for s in stop_list:
#     print(s._name)

# for ft in full_trip_list:
#     print(str([x._name for x in stop_list].index(ft.start_stop._name)) + " " + str([x._name for x in stop_list].index(ft.end_stop._name)) + " " + str(ft.length))

best_solution = genetic_run(stop_list,full_trip_list)   # returns stop_list indexes in best order

# plotting solution
trip_for_plot = {}
for i in range(len(best_solution)-1):
    i_1 = best_solution[i]
    i_2 = best_solution[i+1]
    if (stop_list[i_1], stop_list[i_2]) in connections_with_shortest_route.keys():
        trip_for_plot[(stop_list[i_1], stop_list[i_2])] = connections_with_shortest_route[stop_list[i_1], stop_list[i_2]]
    else:
        trip_for_plot[(stop_list[i_2], stop_list[i_1])] = connections_with_shortest_route[stop_list[i_2], stop_list[i_1]]      

x = []
y = []
for stop in stops._list:
    x.append(stop._X)
    y.append(stop._Y)   

pl.figure(figsize=(192, 108), dpi=100)
pl.plot(x,y,"bo",markersize="0.5")

route_index = 0
for key, value in trip_for_plot.items():
    prev_stop = key[0]
    route_index+=1
    for rt in value:
        rt: Route
        if value.index(rt) != 0:
            prev_stop = gstops.getCommonStops(prev_route,rt).pop()    
        if value.index(rt) < len(value)-1:
            next_stop = gstops.getCommonStops(rt,value[value.index(rt)+1]).pop()
        else:
            next_stop = key[1]                
        
        lat =  []
        long = []
        part_of_route = rt.getPartOfRoute(prev_stop._stops, next_stop._stops)
        for index, stop in enumerate(part_of_route):
            long.append(stop._X)
            lat.append(stop._Y)
            if index == 0 or index == (len(part_of_route)-1):
                pl.annotate(stop._name + str(route_index),(stop._X,stop._Y))
        pl.plot(long,lat,"-",label=rt._nr)
        pl.legend()
        prev_route = rt

# pl.savefig("trvtest.png")
pl.show()