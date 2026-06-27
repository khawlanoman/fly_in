from src.parser import parsing
from src.models.zone_class import Zone
from src.models import drones_data, algo_class
from src.models import drone_class, simulation
import class_visualisation
import sys
import pygame


class Main:
    def __init__(self) -> None:
        pass

    def run_main(self) -> None:

        if len(sys.argv) == 2:
            config_file = sys.argv[1]
        else:
            print("python3 main.py [config_file]")
        file_parse = parsing.Read_input_file()
        rp = file_parse.read_file(config_file)
        dict_neighbors = drones_data.Dict_neighbors()
        algo = algo_class.Algo_dijkstra()
        all_dornes = []
        for i in range(rp[0]):
            try:
                dict_neighb = dict_neighbors.found_neighbors(rp)
                zone_used: dict[str, int]= {}
                all_drones: list[Zone] = []
                path = algo.alog_start(rp, dict_neighb, rp[1],
                                       rp[4], zone_used,
                                       "start", all_drones)
                if not path:
                    print(f"ERROR: No path for drone {i}")
                    break
            except ValueError:
                print("no path found")
                sys.exit(1)
            drone = drone_class.Drone(i, path)
            all_dornes.append(drone)
        visual = class_visualisation.Visualisation(rp[1],
                                                   rp[2], all_dornes)
        s_l = visual.smallests_and_largest()

        visual.window_width_hieght(visual.width_height(s_l))
        simula = simulation.Simulation(rp[4],
                                       all_dornes, rp[0], visual)
        pygame.init()
        screen_info = pygame.display.Info()
        width_screen = screen_info.current_w
        height_screen = screen_info.current_h
        screen = pygame.display.set_mode((width_screen, height_screen))
        image_init = pygame.image.load("images/enter_image.png")
        image_rect = image_init.get_rect()
        image_rect.center = (width_screen // 2, height_screen // 2)
        start = False
        screen.blit(image_init, image_rect)
        pygame.display.flip()
        # while not start:
        #     for event in pygame.event.get():
        #         if event.type == pygame.QUIT:
        #             sys.exit(1)
        #         if event.type == pygame.KEYDOWN:
        #             if event.key == pygame.K_RETURN:
        #                 start = True
        turn_t = simula.run(rp[1], rp[2], algo, rp[4], rp)
        visual.run_v(turn_t, screen)
        pygame.quit()


app = Main()
app.run_main()
