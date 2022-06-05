import matplotlib.pyplot as pl 

from load.LoadData import stops,routes

pl.figure(figsize=(192, 108), dpi=100)
x = []
y = []
for stop in stops._list:
    x.append(stop._X)
    y.append(stop._Y)
    #pl.annotate(stop._name,(stop._X,stop._Y))    
pl.plot(x,y,"bo")
img = pl.imread('resources/map.png')
pl.imshow(img,extent=[18.34,18.95,54.25,54.49])


nr = 0
while nr != "q": 
    nr = input("Wpisz nr Lini:\n")
    if not routes.contains_NR(int(nr)):
        continue
    routes_list = routes.get_Nr(int(nr))
# N3 - > ID NR 403 

    for route in routes_list:
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
    pl.savefig("trasa.png")

# stop, dist = stops.closestStop(18,50)
# print(stop + " Distance " + str(dist))

    