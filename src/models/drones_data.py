class Dict_neighbors:
    def __init__(self) -> None:
       pass

    def found_neighbors(self,t_list:list,forbidden_zone)-> dict:
        dict_neighbors = {}
        dict_connections = t_list[2]
        dict_zones = t_list[1]
        blocked_zone = []
        for element, value in dict_zones.items():
            neighbors= []
            

            if value.metadata.get("zone") == "blocked":
                blocked_zone.append(element)
                # print("hna", blocked_zone)
                continue

            if element == forbidden_zone:
                    continue
           
            for ele in dict_connections:
                if ele.name1 in blocked_zone or ele.name2 in blocked_zone:
                    # print("hna blocked_zone", blocked_zone)
                    continue
                if ele.name1 == forbidden_zone or ele.name2 == forbidden_zone:
                        continue
                elif element == ele.name1:
                    neighbor = ele.name2
                  
                    neighbors.append(neighbor)
                 
                elif element == ele.name2:
                    neighbor = ele.name1
                    
                    neighbors.append(neighbor)
            # print("neighbors",neighbors)
            dict_neighbors[element] = neighbors
        # print(dict_neighbors)
        return dict_neighbors
       