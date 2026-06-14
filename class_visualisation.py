import pygame

class Visualisation:
    def __init__(self,zones,connections) -> None:
        self.zones = zones
        self.connections = connections
        self.scale = 300
        self.margin = 200
        self.min_x = 0
        self.min_y = 0
        self.max_x = 0
        self.max_y = 0
    
    def smallests_and_largest(self)-> tuple:
        if not self.zones:
            return (0,0,0,0)
       
        min_x = min(element.x for  element in self.zones.values())
        min_y = min(element.y for  element in self.zones.values())

        larg_x = max(element.x for  element in self.zones.values())
        larg_y = max(element.y for  element in self.zones.values())
        self.min_x =  min_x
        self.min_y = min_y
        self.max_x = larg_x
        self.max_y = larg_y
        return  (min_x,min_y,larg_x,larg_y)
    
    def width_height(self, t_small_larg:tuple)-> tuple:
        width_t = t_small_larg[2] - t_small_larg[0]
        height_t = t_small_larg[3] - t_small_larg[1]
        return (width_t,height_t)

    def window_width_hieght(self, t_width_height)->tuple:
     
        window_width = (t_width_height[0] * self.scale + (self.margin * 2))
        window_hieght = (t_width_height[1] * self.scale + (self.margin * 2))
        return (window_width,window_hieght)
    
    def run_v(self,window, t_width_height):
        dict_zones={}
        pygame.init()
        screen_info = pygame.display.Info()
        width_screen =  screen_info.current_w
        height_screen = screen_info.current_h

        for key, element in self.zones.items():
                dict_zones[element.name] = (element.x, element.y)
        
        scale_x = (width_screen - self.margin * 2) / (self.max_x - self.min_x)
        scale_y = (height_screen - self.margin * 2) / (self.max_y - self.min_y)
        screen = pygame.display.set_mode((width_screen,height_screen))
        pygame.display.set_caption("hello fly_in")

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
        
            screen.fill((255,255,255)) 

            for value in self.connections:
                for key,element in dict_zones.items():
                        if key == value.name1:
                                value1 = element
                        if key == value.name2:
                                value2 = element
                                
                print(f"{value.name1} -> {value.name2}: {value1} to {value2}")
                con_v1_screan_x = ((value1[0] - self.min_x)* scale_x+ self.margin)
                con_v1_screan_y = ((value1[1] - self.min_y)* scale_y+ self.margin)

                con_v2_screan_x = ((value2[0] - self.min_x)* scale_x+ self.margin)
                con_v2_screan_y = ((value2[1] - self.min_y)* scale_y+ self.margin)
                pygame.draw.line(screen, pygame.Color("red"), (con_v1_screan_x,con_v1_screan_y), (con_v2_screan_x,con_v2_screan_y), width=2)

            for key, element in self.zones.items():
                color = element.metadata.get("color", "white")
                if color is None or color == None:
                    color = "white"
                
                
                screen_x = ((element.x - self.min_x) * scale_x + self.margin)
                screen_y = ((element.y - self.min_y) * scale_y + self.margin)
                pygame.draw.circle(screen, pygame.Color(color), (screen_x, screen_y), 50)
            
          

            pygame.display.update()
        # for key, element in self.zones.items():
        #     screen_x = ((element.x - self.min_x) * self.scale + self.margin )
        #     screen_y = ((element.y - self.min_y) * self.scale + self.margin )
        #     print( "screen_zones",screen_x,screen_y)


