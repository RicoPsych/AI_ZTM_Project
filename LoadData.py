#Loads stops and routes from json file as routes and stops variables

from BusStop import BusStops
from Routes import Routes
import json

with open('stops.json', 'r') as fp:
    stops_dict = json.load(fp)

with open('routes.json', 'r') as fp:
    routes_dict = json.load(fp)

stops = BusStops()
routes = Routes()

stops.addList(stops_dict)

for x in routes_dict:
    x["Route"] = stops.getRoute_ID(x["Route"])

routes.addList(routes_dict)