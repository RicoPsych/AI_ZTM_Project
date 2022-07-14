from base.GroupedStops import GroupedStops
from PlotPaths import CreateGraph, Plot
from algorithms.Astar import startSearch as Asearch
from algorithms.DFS import startSearch as DFSsearch
from base.GroupedStops import GroupedStops
from load.LoadData import stops

def Find2Path():
    
    gstops = GroupedStops(stops)
    start = None
    end = None

    while(start == None):
        start_stop_name = input("Start Stop:")
        start = gstops.getByName(start_stop_name)                   
    
    while(end == None):
        end_stop_name = input("End Stop:")
        end = gstops.getByName(end_stop_name)

    Paths = Asearch(start,end,1,gstops)

    CreateGraph(Paths,start,end,gstops,graph_stops=True)
    Plot(Paths,start,end,gstops) 

def TSP():
    pass


def MainTxtUI():
    quit = False
    choice = 0

    while not quit:
        print("1.Find Shortest route between 2 points\n2.Find shortest path between given points\n3.Quit")
        choice = input()
        match choice:
            case "1":
                Find2Path()
                break
            case "2":
                break
            case "3":
                quit = True
                break
            case _:
                print("Wrong Input")
