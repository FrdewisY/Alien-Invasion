# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 17:50:30 2019

@author: Ferdawis
"""

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A calss that mananges bullets fired by shpis """
    def __init__(self,ai_settings,screen,ship):
	#Create a bullet object, at the ship's current position.
        super().__init__()
        self.screen=screen
        
        #draw a bullet at the ship's position
        self.rect=pygame.Rect(0,0,ai_settings.bullet_width,
                              ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
    def update(self):
        """ move the bullet upwards"""
        self.y -= self.speed_factor
        self.rect.y=self.y
    
    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
    