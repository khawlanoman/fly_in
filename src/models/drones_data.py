class Dict_neighbors:
    def __init__(self) -> None:
       pass

    def found_neighbors(self,t_list:list)-> dict:
        dict_neighbors = {}
        dict_connections = t_list[2]
        dict_zones = t_list[1]

        for element in dict_zones.keys():
            value_list= []
            for ele in dict_connections:
                if element == ele.name1:
                    value_list.append(ele.name2)
                if element == ele.name2:
                    value_list.append(ele.name1)
            
            dict_neighbors[element] = value_list
        
        return dict_neighbors

        
