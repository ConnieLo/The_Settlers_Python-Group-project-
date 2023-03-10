import pygame
# button class
# Set the color and size of the circle
circle_radius = 10

# Create a surface to draw the circle on
circle_surface = pygame.Surface((circle_radius*2, circle_radius*2), pygame.SRCALPHA)

# create a surface with a white circle and a transparent center
circle_surface = pygame.Surface((20, 20), pygame.SRCALPHA)
pygame.draw.circle(circle_surface, (255, 255, 255, 200), (10, 10), 10)

class button_points:
    def __init__(self, x, y):
        self.image2 = circle_surface
        self.rect = self.image2.get_rect()
        self.rect.center = (x, y)
        self.clicked = False
        self.offset = 0 # for animation purposes

    def draw(self, surface):
        action = False  # just a variable used for boolean values, i.e., a flag
        # get mouse's position
        pos = pygame.mouse.get_pos()
        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):  # is the cursor colliding the rectangle of the button
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:  # [0] means left click, [1] means middle click, [2] means right click
                self.clicked = True
                action = True
                self.offset = 6 # the amount of pixels getting shifted down when the button is being clicked on
            elif pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
                self.offset = 0 # when the button is no longer being clicked on the amount of pixels getting shifted down will be 0, i.e., goes back to its position

            # draw the circle button on screen
            surface.blit(self.image2, (self.rect.x, self.rect.y + self.offset))

#        # restarts the state of 'action' variable, so the program can register the button being clicked infinite times
#        if pygame.mouse.get_pressed()[0] == 0:
#            self.clicked = False

        # this allows to use if statements in the draw() methods, because it returns boolean values
        return action