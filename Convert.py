#converts stops and routes from ZTM DB and saves to json files
import json
from LoadStops import stops as unconverted_stops
from LoadRoutesFromTrips import trips_list as unconverted_trips

#convert stops from ZTM to BusStop data type
stops = []
for stop in unconverted_stops:
    stops.append({
    "Name":stop["stopName"],
    "X": stop["stopLon"],
    "Y": stop["stopLat"],
    "ID": stop["stopId"]
    })

#convert routes from ZTM to Routes data type
routes = []
for route in unconverted_trips:
    routes.append({ 
        "Nr":route["Nr"],
        "ID":int(route["ID"]) , 
        "Route": route["Route"]
        })


#save stops and routes to json 
with open("stops.json","w") as fp:
    json.dump(stops,fp)

with open("routes.json","w") as fp:
    json.dump(routes,fp)
