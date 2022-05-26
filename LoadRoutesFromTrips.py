#loads Routes from ZTM DB to dictionary
from datetime import datetime
import requests

from LoadStops import stops 

#Routes
#gets ids of all stops
stops_ids = []
for x in stops:
    stops_ids.append(x["stopId"])

#get today's date
date=datetime.now().strftime("%Y-%m-%d")
#all trips
trips_url = "https://ckan.multimediagdansk.pl/dataset/c24aa637-3619-4dc2-a171-a23eec8f2172/resource/b15bb11c-7e06-4685-964e-3db7775f912f/download/trips.json"
#stops in trips
stops_in_trips = "https://ckan.multimediagdansk.pl/dataset/c24aa637-3619-4dc2-a171-a23eec8f2172/resource/3115d29d-b763-4af5-93f6-763b835967d6/download/stopsintrip.json"
r =  requests.get(trips_url, allow_redirects=True)
r2 = requests.get(stops_in_trips, allow_redirects=True)
trips = r.json()[date]["trips"]
trip_stops =  r2.json()[date]["stopsInTrip"]


trips_list= []

for trip in trips:
    route_dict = {}
    route = []
    for stop in trip_stops:
        if stop["routeId"] == trip["routeId"] and stop["tripId"] == trip["tripId"]:
            route_dict[stop["stopSequence"]] = stop["stopId"]
    for key in sorted(route_dict):
        route.append(route_dict[key])

    #-----------anti exception for routes outside of gdansk
    route = [stop for stop in route if stop in stops_ids]

    trips_list.append({
            "Nr":trip["routeId"],
            "ID":trip["tripId"],
            "Direction":trip["directionId"],
            "Route":route
        })
