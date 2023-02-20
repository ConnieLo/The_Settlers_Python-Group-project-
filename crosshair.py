import pygame

class crosshair(pygame.sprite.Sprite):
    def __init__(self, picture_path, alt_picture_path):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.alt_image = pygame.image.load(alt_picture_path)
        self.rect = self.image.get_rect()

    # checks for any collisions
    def check_collision(self, sprite):
        if self.rect.colliderect(sprite.rect):
            # Collision detected
            return True
        else:
            return False

    # gets the position of the mouse
    def update(self):
        self.rect.center = pygame.mouse.get_pos()

    # collision detection and image switching
    def switch_image(self, sprites=[], picture_path="resources/cursor_fist.gif", alt_image_path="resources/cursor.gif"):
        for sprite in sprites:
            if self.check_collision(sprite):
                self.image = pygame.image.load(alt_image_path)
                return
        self.image = pygame.image.load(picture_path)
