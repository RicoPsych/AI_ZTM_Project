import json
import matplotlib.pyplot as pl 

from LoadData import stops,routes

pl.figure(figsize=(192, 108), dpi=100)
x = []
y = []
for stop in stops._list:
    x.append(stop._X)
    y.append(stop._Y)
    #pl.annotate(stop._name,(stop._X,stop._Y))    
pl.plot(x,y,"bo")

# nr = 0
# while nr != "q": 
#     nr = input("Wpisz nr Lini:\n")
#     if not routes.contains_NR(int(nr)):
#         continue
#     routes_list = routes.get_Nr(int(nr))
# N3 - > ID NR 403 
if True:
    for route in routes._list:
    # for route in routes_list:
        lat =  []
        long = []
        for stop in route._route:
            if stop._ID == 300:
                continue
            long.append(stop._X)
            lat.append(stop._Y)
            pl.annotate(stop._name,(stop._X,stop._Y))    
        pl.plot(long,lat,"-")
        #print(route.toString())
    pl.savefig("trasa.png")

# stop, dist = stops.closestStop(18,50)
# print(stop + " Distance " + str(dist))

    