import pygame
class Simulation:
    def __init__(self,drone,end_hub,all_dornes:list, nb_drones:int, visual) -> None:
        self.end = end_hub
        self.all_drones = all_dornes
        self.nb_drones =nb_drones
        self.visual = visual


    def all_drones_at_goal(self):
        for  drone in self.all_drones:
            if drone.current_zone != self.end:
                return True
        return False


    def run(self,zone, connections)->dict:
        turn = 0;
        # hh
        pygame.init()
        screen_info = pygame.display.Info()
        width_screen =  screen_info.current_w
        height_screen = screen_info.current_h
        screen = pygame.display.set_mode((width_screen,height_screen))

        #  #
        connection_dict = {}
        for conn in connections:
            key = tuple(sorted([conn.name1, conn.name2]))
            connection_dict[key] = conn

        while self.all_drones_at_goal():
            zone_used = {}
            connections_used = {}
            turn_dict = {}
            value_turns = []
            self.visual.run_v(turn, screen)
            turn += 1
            for drone in self.all_drones:
                if drone.current_zone == self.end:
                    continue 
                if drone.state == "holding":
                        next_zone = drone.path[drone.path_index]
                        connection_key = tuple(sorted([drone.current_zone, next_zone]))

                        current_count = zone_used.get(next_zone, 0)

                        connection_count = connections_used.get(connection_key, 0)
                        connection_t = connection_dict.get(connection_key)

                        if connection_t is None:
                            return (f"No connection between {drone.current_zone} and {next_zone}")
                        zone_t = zone.get(next_zone)
                       
                        max_drones = zone_t.metadata.get("max_drones", 0) 
                        max_link = connection_t.metadata.get("max_link_capacity", 0) 

                        if current_count < max_drones and connection_count < int(max_link):
                            drone.path_index +=1
                            zone_used[next_zone]= current_count + 1
                            connections_used[connection_key]= connection_count + 1
                            drone.move_to_zone(next_zone)
                            # print(f" turn {turn}:D{drone.id}-{next_zone}")
                            value_turns.append(f"D{drone.id}-{next_zone}")
                            turn_dict[turn] = value_turns
                            # print(f"Turn {turn}: Drone {drone.id} state={drone.state}, current={drone.current_zone}, path_index={drone.path_index}")
                        
                elif drone.state == "in_flight":
                    drone.flight_turns_re -= 1

                    if drone.flight_turns_re == 0:
                        next_z = drone.path[drone.path_index]
                        drone.current_zone = next_z
                        # print(f" turn {turn}:D{drone.id}-{next_z}")
                        value_turns.append(f"D{drone.id}-{next_z}")
                        turn_dict[turn] = value_turns
                        # print(f"Turn {turn}: Drone {drone.id} state={drone.state}, current={drone.current_zone}, path_index={drone.path_index}")
                        drone.state = "holding"
                        drone.path_index +=1
            
            print(f"turn:{turn_dict}")
        return turn