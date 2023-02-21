import pygame

class TextBox:

    def __init__(self, text, x, y, boxX = None, boxY = None, font = "ALGER.ttf", fontSize = 32, colour = (0, 0, 0)):
        self.string = text
        self.x = x #this will be the centre of the text
        self.y = y #centre
        self.boxX = boxX
        self.boxY = boxY
        self.font = pygame.font.Font(font, 32)
        self.colour = colour
        self.text = None
        self.textRect = None

    def display(self, screen, x = None, y = None): #use these parameters to change coordinates if wanted
        self.render(x, y)
        screen.blit(self.text, self.textRect)

    def render(self, x = None, Y = None): #can preemptively change coordinates without displaying using this
        if x == None:
            x == self.x
        if y == None: 
            y = self.y
        self.text = self.font.render(self.string, True, self.colour)
        self.textRect = self.text.get_rect()
        self.textRect.center = (x // 2, y // 2)



    
