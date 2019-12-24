# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 22:48:42 2019

@author: Ferdawis
"""

import pygame.font
from pygame.sprite import Group

from ship import Ship

class Scoreboard():
    """ A class to show the score """
    
    def __init__(self,ai_settings,screen,stats):
        # Initialize the attributes
        self.ai_settings = ai_settings
        self.stats = stats
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        # Font settings for displaying score
        self.text_color = (45, 45, 45)
        self.font = pygame.font.SysFont(None, 48)
        
        #prepare the score image
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()
        
    def prep_score(self):
        """ Turn the score into a rendered image"""
        rounded_score = int(round(self.stats.score, -1))
        score_str = " {:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color,
                                            self.ai_settings.bg_color)
        
        # Dispaly the score ate the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
        
    def prep_high_score(self):
        """ Turn the highest score into rendered image"""
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str,True,
                                                 self.text_color,
                                                 self.ai_settings.bg_color)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top
        
    def prep_level(self):
        """ Turn the level into rendered image"""
        self.level_image = self.font.render(str(self.stats.level),True,
                                                 self.text_color,
                                                 self.ai_settings.bg_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
    
    def prep_ships(self):
        """ Display how many ships left"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10+ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
            
        
    def show_score(self):
        """ Display the score on the screen"""
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(self.level_image,self.level_rect)
        self.ships.draw(self.screen)
        
        