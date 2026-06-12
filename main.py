from src.parser import parsing
from src.models import drones_data,algo_class
from src.models import drone_class,simulation

import sys

if len(sys.argv) == 2:
    config_file =sys.argv[1]

    
else:
    print("python3 main.py [config_file]")

file_parse = parsing.Read_input_file()
rp  = file_parse.read_file(config_file)
dict_neighbors = drones_data.Dict_neighbors()
dict_neighb = dict_neighbors.found_neighbors(rp)

algo = algo_class.Algo_dijkstra()
# print(f"{rp}\n")
# print(test,"\n")

# for i in rp[1].values():
   
#         print(f"{i.name,i.movement_cost()}")
init = algo.initialization_dicts(rp)
path = algo.alog_start(init,dict_neighb,rp[1],rp[4])
# print(init)
# print(path)
all_dornes = []
for i in range(rp[0]):
    drone = drone_class.Drone(i,path)
    all_dornes.append(drone)
    # print("\nd",i)
   
print(all_dornes)


simula = simulation.Simulation(drone,rp[4],all_dornes,rp[0])

print("turns",simula.run(rp[1],rp[2]))
