import pygame

class Visualisation:
    def __init__(self,zones,connections) -> None:
        self.zones = zones
        self.connections = connections
        self.scale = 300
        self.margin = 200
        self.min_x = 0
        self.min_y = 0
    
    def smallests_and_largest(self)-> tuple:
        if not self.zones:
            return (0,0,0,0)
       
        min_x = min(element.x for  element in self.zones.values())
        min_y = min(element.y for  element in self.zones.values())

        larg_x = max(element.x for  element in self.zones.values())
        larg_y = max(element.y for  element in self.zones.values())
        self.min_x =  min_x
        self.min_y = min_y
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
      
        pygame.init()

        screen = pygame.display.set_mode((window[0],window[1]))
        pygame.display.set_caption("hello fly_in")

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
        
            screen.fill((255,255,255)) 
            for key, element in self.zones.items():
                color = element.metadata.get("color", "white")
                if color is None or color == None:
                    color = "white"
                
                screen_x = ((element.x - self.min_x) * self.scale + 25 )
                screen_y = ((element.y - self.min_y) * self.scale + 25 )
                pygame.draw.circle(screen, pygame.Color(color), (screen_x, screen_y), 30)


            pygame.display.update()
        # for key, element in self.zones.items():
        #     screen_x = ((element.x - self.min_x) * self.scale + self.margin )
        #     screen_y = ((element.y - self.min_y) * self.scale + self.margin )
        #     print( "screen_zones",screen_x,screen_y)


