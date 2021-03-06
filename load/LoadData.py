#Loads stops and routes from json file as routes and stops variables

from base.BusStop import BusStops
from base.Routes import Routes
import json

with open('resources/stops.json', 'r') as fp:
    stops_dict = json.load(fp)

with open('resources/routes.json', 'r') as fp:
    routes_dict = json.load(fp)

stops = BusStops()
routes = Routes()

#load stops
stops.addList(stops_dict)
#load routes and connect them to stops
routes.addList(routes_dict,stops)
