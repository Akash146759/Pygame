import pygame  

pygame.init()  
screen = pygame.display.set_mode((400, 300))  
done = False  

while not done:  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            done = True  
            
    screen.fill((0, 0, 0))  # Clear the screen
    pygame.draw.rect(screen, (100, 125, 255), pygame.Rect(120, 30, 60, 60))    

    pygame.display.flip()
pygame.quit()