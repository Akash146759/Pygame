import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 500, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball Fun!")

# Define colors
def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Ball settings
ball_radius = 20
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
ball_speed_x, ball_speed_y = 4, 4
ball_color = random_color()

# Run the game loop
running = True
while running:
    pygame.time.delay(30)
    screen.fill((0, 0, 0))  # Clear screen
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Get key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        ball_x -= 5
    if keys[pygame.K_RIGHT]:
        ball_x += 5
    if keys[pygame.K_UP]:
        ball_y -= 5
    if keys[pygame.K_DOWN]:
        ball_y += 5

    # Ball movement
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Bounce off walls
    if ball_x - ball_radius <= 0 or ball_x + ball_radius >= WIDTH:
        ball_speed_x = -ball_speed_x
        ball_color = random_color()
    if ball_y - ball_radius <= 0 or ball_y + ball_radius >= HEIGHT:
        ball_speed_y = -ball_speed_y
        ball_color = random_color()

    # Draw ball
    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)
    pygame.display.update()

pygame.quit()
