import math
import random
import pygame

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
PLAYER_START_X = 370
PLAYER_START_Y = 380
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 40
BULLET_SPEED_Y = 10
COLLISION_DISTANCE = 27
FPS = 60

# Initialize Pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Load assets
background = pygame.image.load('background.png')
playerImg = pygame.image.load('player.png')
enemyImg = pygame.image.load('enemy.png')
bulletImg = pygame.image.load('bullet.png')

# Player variables
playerX = PLAYER_START_X
playerY = PLAYER_START_Y
playerX_change = 0

# Enemy setup
num_of_enemies = 6
enemies = []
for _ in range(num_of_enemies):
    enemies.append({
        "x": random.randint(0, SCREEN_WIDTH - 64),
        "y": random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX),
        "x_change": ENEMY_SPEED_X,
        "y_change": ENEMY_SPEED_Y,
        "alive": True
    })

# Bullet setup
bullets = []  # List for multiple bullets

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

# Game over text
over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score():
    score = font.render(f"Score: {score_value}", True, (255, 255, 255))
    screen.blit(score, (10, 10))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(enemy_data):
    screen.blit(enemyImg, (enemy_data["x"], enemy_data["y"]))

def fire_bullet(x, y):
    bullets.append({"x": x, "y": y})

def isCollision(enemy_data, bullet_data):
    distance = math.sqrt((enemy_data["x"] - bullet_data["x"]) ** 2 + (enemy_data["y"] - bullet_data["y"]) ** 2)
    return distance < COLLISION_DISTANCE

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(FPS)
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                fire_bullet(playerX + 16, playerY)
        if event.type == pygame.KEYUP and event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
            playerX_change = 0

    # Player movement
    playerX += playerX_change
    playerX = max(0, min(playerX, SCREEN_WIDTH - 64))

    # Enemy movement & collision check
    for enemy_data in enemies:
        if enemy_data["y"] > 340:
            for e in enemies:
                e["y"] = 2000
            game_over_text()
            break
        
        enemy_data["x"] += enemy_data["x_change"]
        if enemy_data["x"] <= 0 or enemy_data["x"] >= SCREEN_WIDTH - 64:
            enemy_data["x_change"] *= -1
            enemy_data["y"] += enemy_data["y_change"]
        
        # Bullet collision
        for bullet_data in bullets[:]:  # Iterate over a copy to remove bullets
            if isCollision(enemy_data, bullet_data):
                bullets.remove(bullet_data)
                score_value += 1
                enemy_data["x"] = random.randint(0, SCREEN_WIDTH - 64)
                enemy_data["y"] = random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX)

        enemy(enemy_data)

    # Bullet movement
    for bullet_data in bullets[:]:
        if bullet_data["y"] <= 0:
            bullets.remove(bullet_data)
        else:
            screen.blit(bulletImg, (bullet_data["x"], bullet_data["y"]))
            bullet_data["y"] -= BULLET_SPEED_Y

    player(playerX, playerY)
    show_score()
    pygame.display.update()
