class Drone:
    def __init__(self,id,path) -> None:
        self.id = id
        self.current_zone = path[0]
        self.path = path
        self.path_index = 1
        self.state = "holding"
        self.flight_turns_re = 0
    
    def has_next(self)->bool:
        return self.path_index < len(self.path)

    """remove this one """
    def next_zone(self, zone:dict)->str:
    
       
        next_z = self.path[self.path_index]
        zone_obj = zone.get(next_z)

        if zone_obj.metadata.get("zone") == "restricted":
            self.state = "in_flight"
            self.flight_turns_re = 1
        else:
            self.current_zone = next_z
            self.path_index +=1
              
        return next_z
    
    def move_to_zone(self,zone_n:str)->None:
        self.current_zone = zone_n
        
