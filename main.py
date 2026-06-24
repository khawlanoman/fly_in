from src.parser import parsing
from src.models import drones_data,algo_class
from src.models import drone_class,simulation
import class_visualisation
import sys
import pygame


# class Main:
#     def __init__(self) -> none:
#         pass
    
    
if len(sys.argv) == 2:
    config_file =sys.argv[1]

    
else:
    print("python3 main.py [config_file]")

file_parse = parsing.Read_input_file()
rp = file_parse.read_file(config_file)

dict_neighbors = drones_data.Dict_neighbors()


algo = algo_class.Algo_dijkstra()

zones_capacitys = {}
all_dornes = []

for i in range(rp[0]):

    try:
        dict_neighb = dict_neighbors.found_neighbors(rp)
        zone_used ={}
        all_drones = {}
        path = algo.alog_start(rp,dict_neighb,rp[1],rp[4],zone_used,"start",all_drones )
        if not path:
            print(f"ERROR: No path for drone {i}")
            break
    except:
        print(f"no path found")
        sys.exit(1)
    drone = drone_class.Drone(i,path)
    all_dornes.append(drone)

visual = class_visualisation.Visualisation(rp[1],rp[2], all_dornes)
s_l= visual.smallests_and_largest()

window = visual.window_width_hieght(visual.width_height(s_l))

simula = simulation.Simulation(rp[4],all_dornes,rp[0],visual)

simula.run(rp[1],rp[2],algo,rp[4], rp)
