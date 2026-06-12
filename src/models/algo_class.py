class Algo_dijkstra:
    def __init__(self) -> None:
        self. distance= {}
        self.unvisited = []
        self.prev = {}

    def initialization_dicts(self, t_list:list)->list:
        zones = t_list[1]

        for k in zones.keys():
            if (k == "start"):
                self.distance[k] = 0
            else:
                self.distance[k] = float('inf')
            self.unvisited.append(k)
            self.prev[k] = None
        
        return [self.distance,self.unvisited,self.prev]
    
    def alog_start(self,t_list:list, dict_neighbors:dict,zones:dict,end_hub:str)->list:
        distance_al = t_list[0]
        unvisited_al = t_list[1]
        prev_al = t_list[2]

        """find small zone ("""
        while unvisited_al:
            small = None
            small_zone_dist = None
            for k in unvisited_al:
                if distance_al[k] < float('inf'):
                    small_zone_dist = k
                    small = distance_al[k]
            # print("small: ",small_zone_dist)


            """remove  zone from unvisited"""
            unvisited_al.remove(small_zone_dist)
            # print("\nhinaaa",unvisited_al)

            """neighbors" of small zone"""
            for key, value in dict_neighbors.items():
                if key == small_zone_dist:
                    neighbors = value
            
            # print(neighbors)
            neighbors_cost = {}
            for element in neighbors:
                for ele in zones:
                    if element == ele:
                        neighbors_cost[element] = zones[ele].movement_cost()

            

            for k,v in neighbors_cost.items():
                for element in distance_al:
                    if k == element:
                        calculate_dist = small + v
                        if calculate_dist < distance_al[k]:
                            distance_al[k] = calculate_dist
                            prev_al[element] = small_zone_dist
                            
            #print("distances:",distance_al)
            # print("prev:",prev_al)
                            
            path = []
            current = end_hub

            while current is not None:
                path.append(current)
                current = prev_al[current]
            path.reverse()

        return path
        # print("this is my path",path)


                