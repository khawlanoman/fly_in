class Algo_dijkstra:
    def __init__(self) -> None:
        pass

    # def initialization_dicts(self, t_list:list)->list:
    #     zones = t_list[1]
    #     distance = {}
    #     unvisited = []
    #     prev = {}
    #     for k in zones.keys():
    #         if (k == "start"):
    #             distance[k] = 0
    #         else:
    #             distance[k] = float('inf')
    #         unvisited.append(k)
    #         prev[k] = None
        
    #     return [distance,unvisited,prev]
    
    def alog_start(self,t_list:list, dict_neighbors:dict,zones:dict,end_hub:str,)->list:
        
        zones = t_list[1]
        distance_al = {}
        unvisited_al = []
        prev_al = {}
        for k in zones.keys():
            if (k == "start"):
                distance_al[k] = 0
            else:
                distance_al[k] = float('inf')
            unvisited_al.append(k)
            prev_al[k] = None
        
        path = []
       

        # print("prev_al",prev_al)
        # print("ID of dict_neighbors before while:", id(dict_neighbors))
        """find small zone ("""
        while unvisited_al:
            # print("ID of dict_neighbors after while:", 
            
            small_zone_dist = None
            small = float('inf')
            for k in unvisited_al:
                if distance_al[k] < small:
                    small = distance_al[k]
                    small_zone_dist = k

            if small_zone_dist is None:
                break
          
            """remove  zone from unvisited"""
            unvisited_al.remove(small_zone_dist)
            # print("\nhinaaa",unvisited_al)

            """neighbors" of small zone"""
            for key, value in dict_neighbors.items():
                # print("neighbor",value)
                if key == small_zone_dist:
                    neighbors = value
            
            # print(neighbors)
            neighbors_cost = {}
            for element in neighbors:
                
                for ele in zones:
                    if element == ele:
                        neighbors_cost[element] = zones[ele].movement_cost()

            

            for k,v in neighbors_cost.items():
                if k not in unvisited_al:
                        continue
                for element in distance_al:
                    if k == element:
                        calculate_dist = small + v
                        if calculate_dist < distance_al[k]:
                            distance_al[k] = calculate_dist
                            prev_al[element] = small_zone_dist
                            
         
        current = end_hub

        while current is not None:
            path.append(current)
            current = prev_al[current]
        path.reverse()

       
        # print("Path f", path)
        return path
      


                