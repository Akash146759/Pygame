import pygame  

pygame.init()  

screen = pygame.display.set_mode((600, 400))  

done = False  

while not done:  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            done = True  # Properly exit loop

    pygame.display.flip()  

pygame.quit()  # Exit pygame properly after loop ends



import pygame

pygame.init()

screen = pygame.display.set_mode((123, 435))

done = False

while not done:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
        done = True

    pygame.display.flip

pygame.quit()  