import pygame

pygame.init()
screen = pygame.display.set_mode((900, 525))
pygame.display.set_caption("Catanalytics!")
icon = pygame.image.load("Catan-logo.jpg")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
done = False




#Game loop
while(not done):
    #event handler / game exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((0,94,184))



    pygame.display.flip()      #prints to screen
    clock.tick(60)  # limits FPS to 60
pygame.quit()
