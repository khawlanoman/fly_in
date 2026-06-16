class Dict_neighbors:
    def __init__(self) -> None:
       pass

    def found_neighbors(self,t_list:list,forbidden_zone)-> dict:
        dict_neighbors = {}
        dict_connections = t_list[2]
        dict_zones = t_list[1]
    
        for element in dict_zones.keys():
            neighbors= []
            if element == forbidden_zone:
                    continue
            for ele in dict_connections:
                if element == ele.name1:
                    neighbor = ele.name2
                    # if zones_capacitys.get(neighbor,0) < dict_zones[neighbor].metadata.get("max_drones",1):
                    neighbors.append(neighbor)
                    # else:
                    #     continue
                if element == ele.name2:
                    neighbor = ele.name1
                    # if zones_capacitys.get(neighbor,0) < dict_zones[neighbor].metadata.get("max_drones",1):
                    neighbors.append(neighbor)
                    # else:
                    #     continue
            # print(f"Checking zone {element}, capacity={zones_capacitys.get(neighbor,0)}, max={dict_zones[neighbor].metadata.get('max_drones',1)}")
            # print(f"Checking zone {element}, capacity={zones_capacitys.get(element,0)}, max={dict_zones[element].metadata.get('max_drones',1)}")
            dict_neighbors[element] = neighbors
            # if zones_capacitys.get(neighbor,0) >= dict_zones[neighbor].metadata.get("max_drones",1):
            #     zones_capacitys[element] = zones_capacitys.get(element, 0)
        return dict_neighbors
       