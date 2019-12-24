# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 13:39:09 2019

@author: Ferdawis
"""

import pygame 
from pygame.sprite import Group

from ship import Ship
from settings import Settings
import game_functions as gf
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
# Initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,
                                   ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
	# Make a ship, a group of bullets, and a group of aliens.
    ship=Ship(ai_settings,screen)
    bullets=Group()
    aliens=Group()
	
	# Create the fleet of aliens.
    gf.create_fleet(ai_settings,screen,ship,aliens)
    
	# Create an instance to store game statistics.
    stats = GameStats(ai_settings)
    play_button = Button(ai_settings,screen,"Play")
    scoreboard = Scoreboard(ai_settings, screen, stats)
# Start the main loop for the game.
    while True:
        gf.check_events(ai_settings,screen,stats,scoreboard,play_button,
                        ship,aliens,bullets)
        
        if stats.game_active:
            ship.update()
            gf.update_bullet(ai_settings,screen,stats,scoreboard,
                             ship,aliens,bullets)
            gf.update_aliens(ai_settings,stats,screen, scoreboard, 
                             ship,aliens,bullets)
        
        gf.update_screen(ai_settings,screen,stats,scoreboard,
                         ship,aliens,bullets,play_button)

        
                  
run_game()
#os.system("pause")


    