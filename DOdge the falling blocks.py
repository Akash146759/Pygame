import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge the Falling Blocks")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Clock
clock = pygame.time.Clock()

# Player
player_size = 50
player_pos = [WIDTH // 2, HEIGHT - 2 * player_size]
player_speed = 10

# Block
block_size = 50
block_pos = [random.randint(0, WIDTH - block_size), 0]
block_speed = 10

# Game loop
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT] and player_pos[0] < WIDTH - player_size:
        player_pos[0] += player_speed

    # Block movement
    block_pos[1] += block_speed

    # Reset block when it goes off-screen
    if block_pos[1] > HEIGHT:
        block_pos[1] = 0
        block_pos[0] = random.randint(0, WIDTH - block_size)

    # Check collision
    if (
        player_pos[0] < block_pos[0] + block_size
        and player_pos[0] + player_size > block_pos[0]
        and player_pos[1] < block_pos[1] + block_size
        and player_pos[1] + player_size > block_pos[1]
    ):
        game_over = True

    # Drawing
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (player_pos[0], player_pos[1], player_size, player_size))
    pygame.draw.rect(screen, RED, (block_pos[0], block_pos[1], block_size, block_size))

    pygame.display.update()
    clock.tick(30)

pygame.quit()
