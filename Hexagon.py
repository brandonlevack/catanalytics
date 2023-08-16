import pygame

class Hexagon:
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.screen = screen
    
    def drawHexagon(self):
        pygame.draw.line(self.screen, "black", (self.x + 52, self.y - 30),(self.x, self.y - 60))
        pygame.draw.line(self.screen, "black", (self.x, self.y -60),(self.x - 52, self.y - 30))
        pygame.draw.line(self.screen, "black", (self.x - 52, self.y - 30),(self.x - 52, self.y + 30))
        pygame.draw.line(self.screen, "black", (self.x - 52, self.y + 30),(self.x, self.y + 60))
        pygame.draw.line(self.screen, "black", (self.x, self.y + 60),(self.x + 52, self.y + 30))
        pygame.draw.line(self.screen, "black", (self.x + 52, self.y + 30),(self.x + 52, self.y - 30))


#Use this class to have python draw to a jpg or other format, then use that do fill in in paint