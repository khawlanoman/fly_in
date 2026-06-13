import pygame


pygame.init()

screen = pygame.display.set_mode((700,700))


pygame.display.set_caption("HELLO NOMAN")

image_p = pygame.image.load("drone.png")
x= int(100)
y= int(100)
image_f = pygame.transform.smoothscale(image_p,(x,y))
running = True

while running:
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill((255, 255, 255))
    
    
    screen.blit(image_f,(10,100))
    
    pygame.display.update()