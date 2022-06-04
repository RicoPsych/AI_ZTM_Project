#converts stops and routes from ZTM DB and saves to json files
import json
from download.LoadStops import stops as unconverted_stops
from download.LoadRoutesFromTrips import trips_list as unconverted_trips

#convert stops from ZTM to BusStop data type
stops = []
for stop in unconverted_stops:
    stops.append({
                #stopName
    "Name":stop["stopDesc"],
    "X": stop["stopLon"],
    "Y": stop["stopLat"],
    "ID": stop["stopId"]
    })

#convert routes from ZTM to Routes data type
routes = unconverted_trips #[]
# for route in unconverted_trips:
#     routes.append({ 
#         "Nr":route["Nr"],
#         "ID":int(route["ID"]) , 
#         "Direction":route["Direction"],
#         "Route": route["Route"]
#         })


#save stops and routes to json 
with open("resources/stops.json","w") as fp:
    json.dump(stops,fp)

with open("resources/routes.json","w") as fp:
    json.dump(routes,fp)
