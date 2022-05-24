#load stops from ZTM DB to dictionary
import json
import requests

#Gdańsk Stops
#url = "https://ckan.multimediagdansk.pl/dataset/c24aa637-3619-4dc2-a171-a23eec8f2172/resource/4c4025f0-01bf-41f7-a39f-d156d201b82b/download/stops.json"
url = "https://ckan.multimediagdansk.pl/dataset/c24aa637-3619-4dc2-a171-a23eec8f2172/resource/d3e96eb6-25ad-4d6c-8651-b1eb39155945/download/stopsingdansk.json"
r = requests.get(url, allow_redirects=True)
allstops = r.json()["stops"]
stops = []

#filter stops without name
for x in allstops:
    if not x["stopName"] == None:
        stops.append(x)


#zgred
# txt= str(len(stops)) + "\n"
# for x in range(len(stops)):
#     txt+=str(x)+"(x:"+ str(int(stops[x]["stopLat"]*5000)) +",y:"+ str(int(stops[x]["stopLon"]*5000)) +",label:"+ str(stops[x]["stopName"])+") 0\n"
# #all = json.load()
# file = open("gdansk.txt","w")
# file.write(txt)
# file.close()
#NULL