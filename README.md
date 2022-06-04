# AI Project
University AI Project ZTM
Algorithms that will search for fastest route via Gdańsk public transport(ZTM) between chosen points on the map.

Use UpdateData to download up to date data from ZTM.
Other Scripts in main directory use local downloaded data.


Modules:
"base"      contains base Clases for ZTM Data.
"download"  contains scripts to download ZTM Data and save to json in "resources".
"resources" contains Map image and json files with stops and routes.
"load"      contains script to load data from "resources".