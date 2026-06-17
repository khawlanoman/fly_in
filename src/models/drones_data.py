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
                    # print("forbidden-zone:",forbidden_zone)
                    continue
            for ele in dict_connections:
                if ele.name1 == forbidden_zone or ele.name2 == forbidden_zone:
                        continue
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
              
            dict_neighbors[element] = neighbors
        # print("giran:",dict_neighbors)
        return dict_neighbors
       