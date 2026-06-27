class Drone:
    def __init__(self, id: int, path: list) -> None:
        self.id = id
        self.current_zone = path[0]
        self.path = path
        self.path_index = 1
        self.state = "holding"
        self.flight_turns_re = 0
        self.check_rest = 0

    def move_to_zone(self, zone_n: str) -> None:
        """ this function is for  take the next zone for  drone"""
        self.current_zone = zone_n
