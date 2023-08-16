import pygame
from Hexagon import Hexagon

pygame.init()
screen = pygame.display.set_mode((900, 700))
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

    hex1 = Hexagon(70,70,screen)
    hex1.drawHexagon()

    hex2 = Hexagon(174,70,screen)
    hex2.drawHexagon()

    pygame.display.flip()      #prints to screen
    clock.tick(60)  # limits FPS to 60
pygame.quit()
