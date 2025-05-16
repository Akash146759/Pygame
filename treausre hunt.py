import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Treasure Hunt")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GOLD = (255, 215, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Clock
clock = pygame.time.Clock()

# Player
player_size = 50
player_pos = [WIDTH // 2, HEIGHT // 2]
player_speed = 10

# Treasure
treasure_size = 30
treasure_pos = [random.randint(0, WIDTH - treasure_size), random.randint(0, HEIGHT - treasure_size)]

# Obstacles
obstacle_size = 50
obstacle_pos = [random.randint(0, WIDTH - obstacle_size), random.randint(0, HEIGHT - obstacle_size)]
obstacle_speed = 5

# Score
score = 0
font = pygame.font.SysFont("Arial", 30)

# Game loop
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_pos[1] > 0:
        player_pos[1] -= player_speed
    if keys[pygame.K_DOWN] and player_pos[1] < HEIGHT - player_size:
        player_pos[1] += player_speed
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT] and player_pos[0] < WIDTH - player_size:
        player_pos[0] += player_speed

    # Move obstacle
    obstacle_pos[1] += obstacle_speed
    if obstacle_pos[1] > HEIGHT:
        obstacle_pos[0] = random.randint(0, WIDTH - obstacle_size)
        obstacle_pos[1] = 0

    # Check collision with treasure
    if (
        player_pos[0] < treasure_pos[0] + treasure_size
        and player_pos[0] + player_size > treasure_pos[0]
        and player_pos[1] < treasure_pos[1] + treasure_size
        and player_pos[1] + player_size > treasure_pos[1]
    ):
        score += 1
        treasure_pos = [random.randint(0, WIDTH - treasure_size), random.randint(0, HEIGHT - treasure_size)]

    # Check collision with obstacle
    if (
        player_pos[0] < obstacle_pos[0] + obstacle_size
        and player_pos[0] + player_size > obstacle_pos[0]
        and player_pos[1] < obstacle_pos[1] + obstacle_size
        and player_pos[1] + player_size > obstacle_pos[1]
    ):
        game_over = True

    # Drawing
    screen.fill(WHITE)
    pygame.draw.rect(screen, GREEN, (player_pos[0], player_pos[1], player_size, player_size))
    pygame.draw.rect(screen, GOLD, (treasure_pos[0], treasure_pos[1], treasure_size, treasure_size))
    pygame.draw.rect(screen, RED, (obstacle_pos[0], obstacle_pos[1], obstacle_size, obstacle_size))

    # Show score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(30)

pygame.quit()

# End game message
print(f"Game Over! Your final score is: {score}")
