import pygame


class Visualisation:
    def __init__(self, zones :dict, connections: dict, drones: list) -> None:
        self.zones = zones
        self.connections = connections
        self.drones = drones
        self.scale = 100
        self.margin = 600
        self.min_x = 0
        self.min_y = 0
        self.max_x = 0
        self.max_y = 0

    def smallests_and_largest(self) -> tuple:
        if not self.zones:
            return (0, 0, 0, 0)

        min_x = min(element.x for element in self.zones.values())
        min_y = min(element.y for element in self.zones.values())

        larg_x = max(element.x for element in self.zones.values())
        larg_y = max(element.y for element in self.zones.values())

        self.min_x = min_x
        self.min_y = min_y
        self.max_x = larg_x
        self.max_y = larg_y
        return (min_x, min_y, larg_x, larg_y)

    def width_height(self, t_small_larg: tuple) -> tuple:
        width_t = t_small_larg[2] - t_small_larg[0]
        height_t = t_small_larg[3] - t_small_larg[1]
        return (width_t, height_t)

    def window_width_hieght(self, t_width_height) -> tuple:

        window_width = (t_width_height[0] * self.scale + (self.margin * 2))
        window_hieght = (t_width_height[1] * self.scale + (self.margin * 2))
        return (window_width, window_hieght)

    def run_v(self, turn: int, screen: pygame.Surface):

        dict_zones = {}
        pygame.init()
        screen_info = pygame.display.Info()
        width_screen = screen_info.current_w
        height_screen = screen_info.current_h

        for key, element in self.zones.items():
            dict_zones[element.name] = (element.x, element.y)

        x_screen = self.max_x - self.min_x
        y_screen = self.max_y - self.min_y
        if x_screen == 0 or y_screen == 0:
            scale_x = (width_screen - self.margin * 2) / x_screen
            scale_y = 1.0
        else:
            scale_x = (width_screen - self.margin * 2) / x_screen
            scale_y = (height_screen - self.margin * 2) / y_screen
        pygame.display.set_caption("hello fly_in")

        drones_image = pygame.image.load("images/drone.png").convert_alpha()

        drones_image = pygame.transform.scale(drones_image, (70, 70))
        drone_image_width = drones_image.get_width()
        drone_image_height = drones_image.get_height()

        my_text_turn = pygame.font.SysFont("Arial", 30)

        my_text_zone = pygame.font.SysFont("Arial", 20)
        my_drone_text = pygame.font.SysFont("bold", 30)

        my_text_capacity = pygame.font.SysFont("bold", 30)
        clock = pygame.time.Clock()

        screen.fill((50, 50, 50))
        text_turns = my_text_turn.render(f"TURNS: {turn}", True, (0, 255, 0))
        screen.blit(text_turns, (4, 4))

        for value in self.connections:
            check_rest = 0
            for key, element in dict_zones.items():
                if key == value.name1:
                    value1 = element
                if key == value.name2:
                    value2 = element

            con_v1_screan_x = ((value1[0] - self.min_x)
                               * scale_x + self.margin)
            con_v1_screan_y = ((value1[1] - self.min_y)
                               * scale_y + self.margin)
            con_v2_screan_x = ((value2[0] - self.min_x)
                               * scale_x + self.margin)
            con_v2_screan_y = ((value2[1] - self.min_y)
                               * scale_y + self.margin)
            pygame.draw.line(screen, pygame.Color("red"),
                             (con_v1_screan_x, con_v1_screan_y),
                             (con_v2_screan_x, con_v2_screan_y),
                             width=2)
            my_capatity_data = my_text_capacity.render(f"l={value.metadata.get('max_link_capacity')}", True, (255,255,255)) # noqa
            my_capacity_x = (con_v1_screan_x + con_v2_screan_x) / 2
            my_capacity_y = (con_v1_screan_y + con_v2_screan_y) / 2
            for key, element in self.zones.items():
                if key == value.name2:
                    if element.metadata.get("zone") == "restricted":
                        check_rest = 1
                        break
            if check_rest:
                pygame.draw.circle(screen, "gray",
                                   (my_capacity_x, my_capacity_y), 10)
                check_rest = 0
            screen.blit(my_capatity_data, (((my_capacity_x)), (my_capacity_y)))

        for key, element in self.zones.items():
            color = element.metadata.get("color", "white")
            if color is None or color == "rainbow":
                color = "white"
            screen_x = ((element.x - self.min_x)
                        * scale_x + self.margin)
            screen_y = ((element.y - self.min_y)
                        * scale_y + self.margin)
            pygame.draw.circle(screen, pygame.Color(color),
                               (screen_x, screen_y), 70)
            text_zone = my_text_zone.render(f"{element.name}",
                                            True, (255, 255, 255))
            my_text_zone_x = text_zone.get_width()
            my_text_zone_y = text_zone.get_height()
            screen.blit(text_zone,
                        (screen_x - (my_text_zone_x // 2),
                         screen_y - (my_text_zone_y // 2)))
            my_capacity_zone = my_text_capacity.render(f"d = {element.metadata.get('max_drones')}", True, (255,255,255)) # noqa
            my_capacity_zone_x = my_capacity_zone.get_width()
            my_capacity_zone_y = my_capacity_zone.get_height()
            screen.blit(my_capacity_zone,
                        ((screen_x - (my_capacity_zone_x // 2)),
                         (screen_y - (my_capacity_zone_y // 2))
                         - 100))

        for element in self.drones:
            i = 0
            for key, value in dict_zones.items():
                if element.current_zone == key:

                    target_x = value[0]
                    target_y = value[1]

                    next_zone = (element.path[element.path_index]
                                 if element.path_index < len(element.path)
                                 else None)
                    if element.state == "in_flight" and next_zone:
                        next_zone_value = dict_zones.get(next_zone)
                        if next_zone_value:
                            pro = element.flight_turns_re / 2
                            target_x = value[0] + (next_zone_value[0]
                                                   - value[0]) * pro
                            target_y = value[1] + (next_zone_value[1]
                                                   - value[1]) * pro

                    screen_x = (((target_x - self.min_x) * scale_x)
                                + self.margin)
                    screen_y = (((target_y - self.min_y) * scale_y)
                                + self.margin)

                    rotate_image = pygame.transform.rotate(drones_image, i)
                    screen.blit(rotate_image,
                                (screen_x - (drone_image_width // 2),
                                 screen_y - (drone_image_height // 2)))

                    my_drones_text = my_drone_text.render(f"D{element.id}",
                                                          True,
                                                          (255, 255, 255))
                    my_drone_text_x = my_drones_text.get_width()
                    my_drones_text_y = my_drones_text.get_height()

                    screen.blit(my_drones_text,
                                ((screen_x - (my_drone_text_x // 2),
                                  screen_y - (my_drones_text_y // 2) + 100)))

        pygame.display.flip()
        clock.tick(1)
