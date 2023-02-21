import pygame

class TextBox:

    def __init__(self, text, x, y, boxX = None, boxY = None, font = "ALGER.ttf", fontSize = 32):
        self.text = text
        self.x = x
        self.y = y
        self.boxX = boxX
        self.boxY = boxY
        self.font = pygame.font.Font(font, 32)

    

    
