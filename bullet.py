import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """class to manage bullets from the player ship"""
    def __init__(self, ai_settings, screen, ship):
        """spawn bullet at ship's position"""
        super().__init__()
        self.screen = screen

        # create a bullet rect at (0,0) and then set correct position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # store the bullet location as a decimal
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """move the bullet upwards"""
        self.y -= self.speed_factor

        # update the rect position (from decimal)
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
