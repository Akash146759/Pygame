import pygame
import random

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gravity Ball Challenge")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Ball settings
ball_size = 20
ball_x = WIDTH // 3
ball_y = HEIGHT - ball_size - 10
ball_speed_y = 0
gravity = 0.5
jump_power = -10
is_jumping = False

# Platforms
platforms = [(random.randint(50, WIDTH - 50), random.randint(100, HEIGHT - 50)) for _ in range(5)]

# Clock
clock = pygame.time.Clock()

# Game loop
running = True
game_over = False

while running:
    screen.fill(WHITE)  # Clear screen before drawing

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        # Gravity effect
        ball_speed_y += gravity
        ball_y += ball_speed_y

        # Jump mechanism
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and not is_jumping:
            ball_speed_y = jump_power
            is_jumping = True

        # Collision with platforms
        for plat_x, plat_y in platforms:
            if (plat_x < ball_x < plat_x + 80) and (plat_y - ball_size < ball_y < plat_y):
                ball_y = plat_y - ball_size
                ball_speed_y = 0
                is_jumping = False

        # Lose condition (Ball hits the ground)
        if ball_y >= HEIGHT - ball_size:
            game_over = True

        # Draw Ball
        pygame.draw.circle(screen, BLUE, (ball_x, int(ball_y)), ball_size)

        # Draw Platforms
        for plat_x, plat_y in platforms:
            pygame.draw.rect(screen, GREEN, (plat_x, plat_y, 80, 10))
    
    else:
        # Display Game Over Message
        font = pygame.font.Font(None, 50)
        text = font.render("Game Over! Press R to Restart", True, RED)
        screen.blit(text, (WIDTH // 6, HEIGHT // 2))

        # Restart Game
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:  # If "R" is pressed, reset game
            ball_y = HEIGHT - ball_size - 10
            ball_speed_y = 0
            game_over = False

    pygame.display.update()
    clock.tick(30)  # Maintain smooth frame rate

pygame.quit()
