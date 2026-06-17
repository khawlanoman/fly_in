import pygame
from src.models import drones_data
class Simulation:
    def __init__(self,end_hub,all_dornes:list, nb_drones:int, visual) -> None:
        self.end = end_hub
        self.all_drones = all_dornes
        self.nb_drones =nb_drones
        self.visual = visual


    def all_drones_at_goal(self):
        for  drone in self.all_drones:
            if drone.current_zone != self.end:
                return True
        return False


    def run(self,zone, connections,algo,end,t_list)->dict:
        turn = 0;
        # hh
        pygame.init()
        screen_info = pygame.display.Info()
        width_screen =  screen_info.current_w
        height_screen = screen_info.current_h
        screen = pygame.display.set_mode((width_screen,height_screen))
       
        dict_neighbors = drones_data.Dict_neighbors()
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

            # 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return {}
              
            self.visual.run_v(turn, screen)

            p_moves = []
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

                        max_drones = zone_t.metadata.get("max_drones", 1) 
                        max_link = connection_t.metadata.get("max_link_capacity", 1) 

                        if zone_t.metadata.get("zone") == "restricted":
                            
                            if connection_count >= int(max_link):
                                
                                forbidden_zone = next_zone
                                dict_neighb = dict_neighbors.found_neighbors(t_list,forbidden_zone)
                                # print("path:",drone.path)
                                new_path = algo.alog_start(t_list,dict_neighb,zone,end)
                                # print("new_path", new_path)
                                if new_path and len(new_path) > 1:
                                    drone.path = new_path
                                    drone.path_index = 1
                                    # print("path_index:",drone.path_index)
                                    drone.state = "holding"
                                    drone.next_zone = None
                                    
                                    
                                # print("makynch path")
                                continue
                                
                            connections_used[connection_key] = connection_count + 1
                            
                            drone.state = "in_flight"
                            drone.flight_turns_re = 2
                            drone.next_zone = next_zone
                            # drone.path_index +=1
                            # 
                            value_turns.append(f"D{drone.id} go to connection ({next_zone})")
                            continue

                        if current_count >= max_drones or connection_count >= int(max_link):
                                forbidden_zone = next_zone
                                dict_neighb = dict_neighbors.found_neighbors(t_list,forbidden_zone)
                                new_path = algo.alog_start(t_list,dict_neighb,zone,end)
                                # print("new_path", new_path)
                                if new_path and len(new_path) > 1:
                                    drone.path = new_path
                                    drone.path_index = 1
                                    # print("path_index:",drone.path_index)
                                    drone.state = "holding"
                                    drone.next_zone = None
                                    
                                # print("makynch path")
                                continue
                           

                        drone.move_to_zone(next_zone)
                        drone.path_index +=1
                           
                        zone_used[next_zone]= current_count + 1
                        connections_used[connection_key]= connection_count + 1
                            
                         
                        value_turns.append(f"D{drone.id}-{next_zone}")
                         
                            
                elif drone.state == "in_flight":

                    drone.flight_turns_re -= 1
                    next_z = drone.next_zone
                    zone_t = zone.get(next_z)

                    if drone.flight_turns_re  > 0:
                        value_turns.append(f"D{drone.id} waiting {next_z}")
                        continue
                
                    current_count = zone_used.get(next_z, 0)
                    max_drones = zone_t.metadata.get("max_drones", 1) 

                    if current_count >= max_drones:
                            continue
                    drone.current_zone = next_z
                    drone.path_index += 1
                    zone_used[next_z]= current_count + 1
                    
                        # print(f" turn {turn}:D{drone.id}-{next_z}")
                    value_turns.append(f"D{drone.id}-{next_z}")
                    
                        # print(f"Turn {turn}: Drone {drone.id} state={drone.state}, current={drone.current_zone}, path_index={drone.path_index}")
                    drone.state = "holding"
                    drone.next_z= None

            turn_dict[turn] = value_turns     
            print(f"turn:{turn_dict}")
            turn += 1

        return turn
    
    