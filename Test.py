from BusStop import BusStops
from Routes import Routes



busStopsList = BusStops()
routesList = Routes()

#-----------------------------example stop
# stop = {
#     "Name":"1", #string
#     "X": 1, #integer/double
#     "Y": 1, #integer/double
#     "ID":1  #integer
#     }
#-----------------------------example route
# route = {
#     "Nr":"r1" ,
#     "ID": 132131, 
#     "Route": busStopsList.getRoute_Names(["1","2","3","4","5"])
# }
#-----------------------------

#lists of bus stops and routes
busstops = [{
    "Name":"1", #string
    "X": 1, #integer/double
    "Y": 1, #integer/double
    "ID":1  #integer
    },
    {
    "Name":"2", #string
    "X": 2, #integer/double
    "Y": 2, #integer/double
    "ID":2  #integer 
    },
    {
    "Name":"3", #string
    "X": 3, #integer/double
    "Y": 3, #integer/double
    "ID":3  #integer
    },
    {
    "Name":"4", #string
    "X": 4, #integer/double
    "Y": 4, #integer/double
    "ID":4  #integer
    },
    {
    "Name":"5", #string
    "X": 5, #integer/double
    "Y": 5, #integer/double
    "ID":5  #integer
    },
    {
    "Name":"6", #string
    "X": 6, #integer/double
    "Y": 6, #integer/double
    "ID":6  #integer
    },
    {
    "Name":"7", #string
    "X": 7, #integer/double
    "Y": 7, #integer/double
    "ID":7  #integer
    }]

#!!!Must add bus stops before creating any routes
busStopsList.addList(busstops)


testroutes = [{
    "Nr":"r1" ,
    "ID": 1, 
    "Route": busStopsList.getRoute_Names(["1","2","3","4","5"])},
    {
    "Nr":"r2" ,
    "ID": 2, 
    "Route": busStopsList.getRoute_Names(["1","5","6"])},
    {
    "Nr":"r3" ,
    "ID": 3, 
    "Route": busStopsList.getRoute_Names(["6","7"])},
    {
    "Nr":"r4" ,
    "ID": 4, 
    "Route": busStopsList.getRoute_ID([2,4])}
    ]

routesList.addList(testroutes)

routesList.printRoutes()

for x in routesList.get_ID(1).getCommonStops(routesList.get_ID(1)):
    print(x.toString())