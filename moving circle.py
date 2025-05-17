import pygame  

pygame.init()  
screen = pygame.display.set_mode((400, 300))  
x = 200  
running = True  

while running:  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            running = False  
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= 10
            elif event.key == pygame.K_RIGHT:
                x += 10
                
    screen.fill((0, 0, 0))  # Clear screen
    pygame.draw.circle(screen, (255, 0, 0), (x, 150), 30)  
    pygame.display.flip()
