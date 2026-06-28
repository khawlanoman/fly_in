import pygame
from src.models import drones_data
from class_visualisation import Visualisation
from src.models.algo_class import Algo_dijkstra
import sys


class Simulation:
    def __init__(self, end_hub: str, all_dornes: list,
                 nb_drones: int, visual: Visualisation) -> None:
        self.end = end_hub
        self.all_drones = all_dornes
        self.nb_drones = nb_drones
        self.visual = visual

    def all_drones_at_goal(self) -> bool:
        for drone in self.all_drones:
            if drone.current_zone != self.end:
                return True
        return False

    def run(self, zone: dict, connections: dict,
            algo: Algo_dijkstra, end: str, t_list: list) -> int:
        """this function is the import part in project ,
        is execute the simulation turn by turn , is
        manage the movement of all drones , is check the
        zones and connections capacitys... """
        turn = 0

        pygame.init()
        screen_info = pygame.display.Info()
        width_screen = screen_info.current_w
        height_screen = screen_info.current_h
        screen = pygame.display.set_mode((width_screen, height_screen))
        dict_neighbors = drones_data.Dict_neighbors()

        connection_dict = {}
        for conn in connections:
            key = tuple(sorted([conn.name1, conn.name2]))
            connection_dict[key] = conn

        while self.all_drones_at_goal():
            zone_used: dict[str, int] = {}
            connections_used: dict[tuple, int] = {}
            turn_dict = {}
            value_turns = []
            turn += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return 0

            for d in self.all_drones:
                if d.state == "holding" and d.current_zone != self.end:
                    zone_used[d.current_zone] = zone_used.get(d.current_zone, 0) + 1 # noqa
            for drone in self.all_drones:
                if drone.current_zone == self.end:
                    continue
                if drone.state == "holding":
                    next_zone = drone.path[drone.path_index]
                    connection_key = tuple(sorted([drone.current_zone,
                                                   next_zone]))
                    current_count = zone_used.get(next_zone, 0)
                    connection_count = connections_used.get(connection_key, 0)
                    connection_t = connection_dict.get(connection_key)
                    if connection_t is None:
                        print("No connection between"
                              f"{drone.current_zone} and {next_zone}")
                        return -1
                    zone_t = zone[next_zone]
                    max_drones = zone_t.metadata.get("max_drones", 1)
                    max_link = connection_t.metadata.get("max_link_capacity", 1) # noqa
                    connection_check_free = False
                    for dr in self.all_drones:
                        if dr.state == "in_flight":
                            connection_link = tuple(sorted([dr.current_zone,
                                                            dr.next_zone]))
                            if connection_link == connection_key:
                                connection_check_free = True
                                break
                    if connection_check_free:
                        continue
                    if (current_count >= max_drones
                            or connection_count >= int(max_link)):
                        try:
                            dict_neighb = dict_neighbors.found_neighbors(t_list) # noqa
                            new_path = algo.alog_start(t_list, dict_neighb,
                                                       zone, end, zone_used,
                                                       drone.current_zone,
                                                       self.all_drones)
                        except ValueError:
                            print("no path found")
                            sys.exit(1)
                        if new_path and len(new_path) > 1:
                            drone.path = new_path
                            drone.path_index = 1
                            drone.state = "holding"
                            drone.next_zone = None
                            next_zone = drone.path[drone.path_index]
                            connection_key = tuple(sorted([drone.current_zone, next_zone])) # noqa
                            current_count = zone_used.get(next_zone, 0) + 1
                            connection_count = connections_used.get(connection_key, 0) # noqa
                            connection_t = connection_dict[connection_key]
                            zone_t = zone[next_zone]
                            max_drones = zone_t.metadata.get("max_drones", 1)
                            max_link = connection_t.metadata.get("max_link_capacity", 1) # noqa
                            if (current_count >= max_drones
                                    or connection_count >= int(max_link)):
                                continue
                        else:
                            continue
                    if zone_t.metadata.get("zone") == "restricted":
                        if connection_count >= int(max_link):
                            continue
                        zone_used[drone.current_zone]  = zone_used.get(drone.current_zone, 1) - 1 # noqa
                        connections_used[connection_key] = connection_count + 1
                        drone.state = "in_flight"
                        drone.flight_turns_re = 2
                        drone.next_zone = next_zone
                        drone.check_rest = 1
                        value_turns.append(f"D{drone.id}-connection({next_zone})") # noqa
                        continue
                    else:
                        zone_used[drone.current_zone] = zone_used.get(drone.current_zone, 1) - 1 # noqa
                        connections_used[connection_key] = connection_count + 1
                        drone.move_to_zone(next_zone)
                        drone.path_index += 1
                        zone_used[next_zone] = zone_used.get(next_zone, 0) + 1
                        connections_used[connection_key] = connection_count + 1
                        value_turns.append(f"D{drone.id}-{next_zone}")
                        continue

            for drone in self.all_drones:
                if drone.state == "in_flight":
                    drone.flight_turns_re -= 1
                    next_z = drone.next_zone
                    zone_t = zone[next_z]
                    if drone.flight_turns_re > 0:
                        continue
                    current_count = zone_used.get(next_z, 0)
                    max_drones = zone_t.metadata.get("max_drones", 1)
                    if current_count >= max_drones:
                        drone.flight_turns_re = 1
                        continue
                    drone.current_zone = next_z
                    drone.path_index += 1
                    zone_used[next_z] = zone_used.get(next_z, 0) + 1
                    value_turns.append(f"D{drone.id}-{next_z}")
                    drone.state = "holding"
                    drone.check_rest = 0
                    drone.next_z = None

            self.visual.run_v(turn, screen)
            turn_dict[turn] = value_turns
            print(", ".join(f"turn {k}:{"  ".join(ele)} "
                            for k, ele in turn_dict.items()))

        return turn
