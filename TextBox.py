import pygame

class TextBox:

    def __init__(self, text, coords, boxX = None, boxY = None, font = "ALGER.ttf", fontSize = 32, colour = (0, 0, 0)):
        self.string = text
        self.x = coords[0] #this will be the centre of the text
        self.y = coords[1] #centre
        self.boxX = boxX
        self.boxY = boxY
        self.font = pygame.font.Font(font, 32)
        self.colour = colour
        self.text = None
        self.textRect = None

    def display(self, screen, coords = None): #use these parameters to change coordinates if wanted
        self.render(coords)
        screen.blit(self.text, self.textRect)

    def render(self, coords = None): #can preemptively change coordinates without displaying using this
        if coords == None:
            x = self.x
            y = self.y
        else:
            x = coords[0]
            y = coords[1]
        self.text = self.font.render(self.string, True, self.colour)
        self.textRect = self.text.get_rect()
        self.textRect.center = (x // 2, y // 2)

    def changeText(self, text):
        self.text = text



    
