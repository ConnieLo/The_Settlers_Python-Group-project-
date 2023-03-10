import pygame
# button class
# Set the color and size of the circle
circle_color = (0, 0, 0)
circle_radius = 10

# Create a surface to draw the circle on
circle_surface = pygame.Surface((circle_radius*2, circle_radius*2), pygame.SRCALPHA)

# Draw the circle on the surface
pygame.draw.circle(circle_surface, circle_color, (circle_radius, circle_radius), circle_radius)

class button_points:
    def __init__(self, x, y):
        self.image2 = circle_surface
        self.rect = self.image2.get_rect()
        self.rect.topleft = (x, y)
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

            # only draw the shadow when button is not being clicked
            if self.offset == 0:
                shadow_rect = pygame.Rect(self.rect.x + 5, self.rect.y + self.offset + 5, self.rect.width, self.rect.height)
                pygame.draw.rect(surface, (0, 0, 0, 100), shadow_rect)


            # draw the circle button on screen
            surface.blit(self.image2, (self.rect.x, self.rect.y + self.offset))


        # restarts the state of 'action' variable, so the program can register the button being clicked infinite times
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # this allows to use if statements in the draw() methods, because it returns boolean values
        return action