import sys
import pygame
from bullet import Bullet

def check_events(ai_settings, screen, ship, bullets):
    """keys and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """keypress events"""
    if event.key == pygame.K_RIGHT:
        # move ship to the right
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # move ship to the left
        ship.moving_left = True
    # shooting
    elif event.key == pygame.K_SPACE:
        # spawn new bullet and add it to the group
        fire_bullets(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event, ship):
    """key release events"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def fire_bullets(ai_settings, screen, ship, bullets):
    """spawn new bullet and add it to the group, limit their number"""
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def update_screen(ai_settings, screen, ship, bullets):
    """update images on scren and flip to new one"""
    screen.fill(ai_settings.bg_color) 
    # redraw the bullets behind ship
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    pygame.display.flip() # update the screen

def update_bullets(bullets):
    """update position of bullets and delete old ones"""
    bullets.update()
    # delete bullets that reach the top
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
