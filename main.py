from src.parser import parsing
from src.models import drones_data,algo_class
from src.models import drone_class,simulation
import class_visualisation
import sys
import pygame

if len(sys.argv) == 2:
    config_file =sys.argv[1]

    
else:
    print("python3 main.py [config_file]")

file_parse = parsing.Read_input_file()
rp = file_parse.read_file(config_file)
# print(type(rp))
dict_neighbors = drones_data.Dict_neighbors()


# for i in rp[1].values():
#     print(i.metadata)


# dict_neighb = dict_neighbors.found_neighbors(rp,zones_capacitys)

algo = algo_class.Algo_dijkstra()
# print(f"{rp}\n")
# print(test,"\n")

# for i in rp[1].values():
   
#         print(f"{i.name,i.movement_cost()}")




# print(init)
# print(path)
zones_capacitys = {}
all_dornes = []

for i in range(rp[0]):
    # if i == 2:
    # print(f"d{i}: {zones_capacitys}")
    forbidden = None
   
    init = algo.initialization_dicts(rp)
    dict_neighb = dict_neighbors.found_neighbors(rp,"fast_junction")
    # if i == 2:
    #     print(f"hna{i}:{dict_neighb['merge_point']}")
    path = algo.alog_start(init,dict_neighb,rp[1],rp[4])
    if not path:
        print(f"ERROR: No path for drone {i}")
        break
    drone = drone_class.Drone(i,path)
    all_dornes.append(drone)
   
    
    # for zone in path:
    #     zones_capacitys[zone] = zones_capacitys.get(zone, 0) + 1
        # max_cap = rp[1][zone].metadata.get("max_drones", 1)
    # print(f"After drone {i}, zones_capacitys: {zones_capacitys}")
 


visual = class_visualisation.Visualisation(rp[1],rp[2], all_dornes)
s_l= visual.smallests_and_largest()

window = visual.window_width_hieght(visual.width_height(s_l))

simula = simulation.Simulation(rp[4],all_dornes,rp[0],visual)

simula.run(rp[1],rp[2],algo,init,dict_neighb,rp[4])

# visual.run_v(simula.run(rp[1],rp[2]))