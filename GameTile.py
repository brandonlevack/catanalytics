from Hexagon import Hexagon

class GameTile:
    def __init__ (self, x, y, resource, num, screen):
        self.x = x
        self.y = y
        self.resource = resource
        self.dieNumber = num
        self.hex = Hexagon(x,y,screen)

    def drawTile(self):
        self.hex.drawHexagon()

    
