# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 19:36:50 2019

@author: Ferdawis
"""

import pygame 
from pygame.sprite import Sprite


class Alien(Sprite):
    """ A class to represent a single alien in the fleet."""
    
    def __init__(self,ai_settings,screen):
        """initialize the alien """
        super().__init__()
        self.screen = screen 
        self.ai_settings = ai_settings
    
	# load the image of the alien and set the 'rect' property
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        
    # set the alien's initial position
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
    
    # store the alien‘s accurate positon
        self.x=float(self.rect.x)
       
    
    def blitme(self):
        """ draw the alien at the given position"""
        self.screen.blit(self.image,self.rect)
    
    def update(self):
        self.x += (self.ai_settings.alien_speed_factor*
                   self.ai_settings.fleet_direction)
        self.rect.x = self.x
        
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.left <= screen_rect.left:
            return True
        elif self.rect.right >= screen_rect.right:
            return True
        
        
        
        
        
        
        
        
        
        
        
        
        
    