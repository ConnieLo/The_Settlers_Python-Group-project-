import pygame
# button class

class button_points:
    def __init__(self, x, y, image, hover_image=None):
        self.image = image
        self.hover_image = hover_image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def draw(self, screen):
        # Get mouse's position
        mouse_pos = pygame.mouse.get_pos()

        # Check if the cursor is colliding with the rectangle of the button
        if self.hover_image and self.rect.collidepoint(mouse_pos):
            # Draw the hover image on the screen
            screen.blit(self.hover_image, self.rect)


    def is_clicked(self):
        # Check if the left mouse button is pressed and the cursor is on the button
        return pygame.mouse.get_pressed(3)[0] and self.rect.collidepoint(pygame.mouse.get_pos())