class Dict_neighbors:
    def __init__(self) -> None:
        pass

    def found_neighbors(self, t_list: list) -> dict:
        """ this function is for  know the zone neighbors"""
        dict_neighbors = {}
        dict_connections = t_list[2]
        dict_zones = t_list[1]
        blocked_zone = []

        for element, value in dict_zones.items():
            neighbors = []

            if value.metadata.get("zone") == "blocked":
                blocked_zone.append(element)
                continue
            for ele in dict_connections:
                if (ele.name1 in blocked_zone or ele.name2 in blocked_zone):
                    continue

                elif element == ele.name1:
                    neighbor = ele.name2
                    neighbors.append(neighbor)

                elif element == ele.name2:
                    neighbor = ele.name1
                    neighbors.append(neighbor)
            dict_neighbors[element] = neighbors

        return dict_neighbors
