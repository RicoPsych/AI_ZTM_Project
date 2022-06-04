from asyncio.windows_events import NULL
from datetime import datetime
import requests

from download.LoadStops import stops 

#Routes
#gets ids of all stops
stops_ids = []
for x in stops:
    stops_ids.append(x["stopId"])


#all routes
url = "https://ckan.multimediagdansk.pl/dataset/c24aa637-3619-4dc2-a171-a23eec8f2172/resource/a023ceb0-8085-45f6-8261-02e6fcba7971/download/stoptimes.json"
r = requests.get(url, allow_redirects=True)
routes = r.json()

#get today's date
date=datetime.now().strftime("%Y-%m-%d")

routes_list = []
for route in routes:
    #for url in routes[route]:
        #url = routes[route][0]
        for link in routes[route]:
            if date in link: 
                url = link
                break
        rq = requests.get(url, allow_redirects=True)
        all_stops_in_route = rq.json()["stopTimes"]
        route_stop_ids = [stop["stopId"] for stop in all_stops_in_route if stop["stopId"] in stops_ids]

        route_stop_ids = list(dict.fromkeys(route_stop_ids))
        routes_list.append({"Nr":route,
        "ID":route,
        "Route":route_stop_ids
        })
