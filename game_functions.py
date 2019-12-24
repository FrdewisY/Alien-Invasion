# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 12:55:34 2019

@author: Ferdawis
"""

import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep
from scoreboard import Scoreboard

def check_keydown_events(event,ai_settings,screen,ship,bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)
    elif event.key == pygame.K_q:
        sys.exit()
       

def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False
        
def check_events(ai_settings,screen,stats,scoreboard,
                 play_button,ship,aliens,bullets):
     for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                check_keydown_events(event,ai_settings,screen,ship,bullets)
            elif event.type == pygame.KEYUP:
               check_keyup_events(event,ship)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x,mouse_y = pygame.mouse.get_pos()
                check_play_button(ai_settings,screen,stats,scoreboard,
                                  play_button,ship,aliens,bullets,
                                  mouse_x,mouse_y)
                
def check_play_button(ai_settings,screen,stats,scoreboard,play_button,
                      ship,aliens,bullets,mouse_x,mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    if (button_clicked) and (stats.game_active == False):
        if play_button.rect.collidepoint(mouse_x,mouse_y):
            # Reset the game settings when restart
            ai_settings.initialize_dynamic_settings()
            pygame.mouse.set_visible(False)
            # Reset the game status
            stats.reset_stats()
            stats.game_active = True
            scoreboard.prep_score()
            scoreboard.prep_high_score()
            scoreboard.prep_level()
            scoreboard.prep_ships()
            
        
            # Clear the list of alien and bullets
            aliens.empty()
            bullets.empty()
        
            # Create a new fleet of aliens and rsset the ship
            create_fleet(ai_settings,screen,ship,aliens)
            ship.center_ship()
                
def update_screen(ai_settings,screen,stats,scoreboard,ship,aliens,bullets,play_button):
     # Redraw the screen, each pass through the loop.
        screen.fill(ai_settings.bg_color)
        
		# Redraw all bullets, behind ship and aliens.
        for bullet in bullets.sprites():
            bullet.draw_bullet()
        ship.blitme()
        aliens.draw(screen)
        scoreboard.show_score()
        # If the game is not active, draw the paly button
        if not stats.game_active:
            play_button.draw_button()
        
		# Make the most recently drawn screen visible.
        pygame.display.flip()

def update_bullet(ai_settings,screen,stats,scoreboard,ship,aliens,bullets):
    """update the bullets and delete the bullets that moved out of screen """
    #Update bullet positions.
    bullets.update()

    #delete the bullets that moved out of the screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
			
    check_alien_bullet_collision(ai_settings,screen,stats,scoreboard,
                                 ship,aliens,bullets)

def check_alien_bullet_collision(ai_settings,screen,stats,scoreboard,
                                 ship,aliens,bullets):
    """Respond to bullet-alien collisions."""
	# Remove any bullets and aliens that have collided.
    collisions=pygame.sprite.groupcollide(bullets,aliens,True,True)
    
    if collisions:       
        #for alien in collisions.values():
        stats.score += ai_settings.alien_points#*len(aliens)
        scoreboard.prep_score()
        check_high_score(stats,scoreboard)
    
    if len(aliens) == 0:
        # Delete the current bullets, speed up the game and create new fleet
        bullets.empty()
        ai_settings.increase_speed()
        stats.level += 1
        scoreboard.prep_level()
        create_fleet(ai_settings,screen,ship,aliens)
        
    
def fire_bullet(ai_settings,screen,ship,bullets):
    """Fire a bullet, if limit not reached yet."""
	
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)
        
def get_number_aliens_x(ai_settings,alien_width):
    """calculates the number of aliens that a row could contain """
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(ai_settings,ship_height,alien_height):
    available_space_y = (ai_settings.screen_height - (3 * alien_height)
                         - ship_height)
    numer_rows = int(available_space_y/(2*alien_height))
    return numer_rows

def create_alien(ai_settings,screen,aliens,alien_number,row_number):
    """create an alien and put it in the row at present """
    alien=Alien(ai_settings,screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width*alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height*row_number
    aliens.add(alien)
    
def create_fleet(ai_settings,screen,ship,aliens):
    """create a fleet of aliens """
    alien=Alien(ai_settings,screen)
    number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)
    number_rows = get_number_rows(ai_settings,ship.rect.height,
                                  alien.rect.height)
    # create a fleet of aliens
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings,screen,aliens,alien_number,row_number)
def check_fleet_edges(ai_settings,aliens):
    """take measures if one alien hits the edge of the screen """
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break
    
def change_fleet_direction(ai_settings, aliens):
    """change the direcrion of the fleet and move the fleet downward """
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1
        
def ship_hit(ai_settings,stats,screen,scoreboard,ship,aliens,bullets):
    """ respond to the ship that was hit"""
    if stats.ships_left > 0:
        # Decrement ships_left 
        stats.ships_left -= 1
        scoreboard.prep_ships()
    else:
        stats.game_active = False 	
        pygame.mouse.set_visible(True)

    aliens.empty()
    bullets.empty()
    create_fleet(ai_settings,screen,ship,aliens)
    ship.center_ship()
    sleep(0.5)
    
    
def update_aliens(ai_settings, stats, screen, scoreboard, ship, aliens, bullets):
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings,stats,screen, scoreboard, ship,aliens,bullets)
    check_aliens_bottom(ai_settings,stats,screen,scoreboard,
                        ship,aliens,bullets)
        
def check_aliens_bottom(ai_settings,stats,screen,scoreboard,
                        ship,aliens,bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings,stats,screen,scoreboard,
                     ship,aliens,bullets)
            break
    
def check_high_score(stats,scoreboard):
    """ Check if there is a new high score"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        scoreboard.prep_high_score()
    

       
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    