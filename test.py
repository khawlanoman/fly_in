# import pygame


# pygame.init()

# screen = pygame.display.set_mode((700,700))


# pygame.display.set_caption("HELLO NOMAN")

# image_p = pygame.image.load("drone.png")
# x= int(100)
# y= int(100)
# image_f = pygame.transform.smoothscale(image_p,(x,y))
# running = True

# while running:
   
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False


#     screen.fill((255, 255, 255))
    
    
#     screen.blit(image_f,(10,100))
    
#     pygame.display.update()


import pygame
import sys

# Initialize pygame
pygame.init()

# Setup display window
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point to Point Animation")
clock = pygame.time.Clock()

# Colors
BACKGROUND = (30, 30, 30)
CIRCLE_COLOR = (255, 87, 34)
TARGET_COLOR = (76, 175, 80)

# Movement variables (Using Vector2 for precision floats)
current_pos = pygame.math.Vector2(100, 100)
target_pos = pygame.math.Vector2(700, 500)
speed = 5  # Pixels per frame

running = True
while running:
    # 1. Handle Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Set a new target point when clicking anywhere on the screen
        # elif event.type == pygame.MOUSEBUTTONDOWN:
        #     target_pos = pygame.math.Vector2(event.pos)

    # 2. Update Position (The Animation Logic)
    # Calculate vector pointing from current position to target position
    direction = target_pos - current_pos
    distance = direction.length()

    if distance > 0:
        # If we are close enough to overshoot, snap directly to target
        if distance <= speed:
            current_pos = pygame.math.Vector2(target_pos)
        else:
            # Normalize direction (makes length 1) and move by speed
            direction = direction.normalize()
            current_pos += direction * speed

    # 3. Render / Draw everything
    screen.fill(BACKGROUND)
    
    # Draw target destination marker
    pygame.draw.circle(screen, TARGET_COLOR, (int(target_pos.x), int(target_pos.y)), 6)
    
    # Draw moving object (Must convert float positions to integers for drawing)
    pygame.draw.circle(screen, CIRCLE_COLOR, (int(current_pos.x), int(current_pos.y)), 20)

    pygame.display.flip()
    clock.tick(60) # Lock the frame rate to 60 FPS

pygame.quit()
sys.exit()
