import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf

def game_init():
    # set up the screen object
    pygame.init()
    ai_settings = Settings()    # import game settings
    screen = pygame.display.set_mode(
            (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Cosmo Invaders!!")
    bg_color = (41,41,61)
    ship = Ship(ai_settings, screen)
    
    # make a group for bullets
    bullets = Group()

    # game process start
    while True:
        # listen for player input events
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets) 
        # fill the screen with the background color
        gf.update_screen(ai_settings, screen, ship, bullets)
    
game_init()
