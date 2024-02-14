import pygame
import sys

pygame.init()

# Set up the display
width, height = 400, 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Drawing a Pig")

# Colors
white = (255, 255, 255)
pink = (255, 182, 193)
black = (0, 0, 0)

leg_height = 30

def draw_pig(leg_position):
    # Draw the body
    pygame.draw.circle(screen, pink, (200, 200), 50)

    # Draw the head
    pygame.draw.circle(screen, pink, (150, 150), 30)

    # Draw the eyes
    pygame.draw.circle(screen, black, (140, 140), 5)
    pygame.draw.circle(screen, black, (160, 140), 5)

    # Draw the nose
    pygame.draw.circle(screen, pink, (150, 145), 5)

    # Draw the ears
    pygame.draw.circle(screen, pink, (120, 120), 10)
    pygame.draw.circle(screen, pink, (180, 120), 10)

    # Draw the legs
    pygame.draw.rect(screen, black, (170, 200 + leg_position, 10, leg_height))
    pygame.draw.rect(screen, black, (220, 200 + leg_position, 10, leg_height))

    pygame.display.flip()

leg_position = 40

# Run the game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(white)
    draw_pig(leg_position)
    pygame.display.flip()


    pygame.time.delay(50)  # Add a slight delay to see the drawing and control the speed of movement
