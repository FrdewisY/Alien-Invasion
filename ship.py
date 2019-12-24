# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 12:38:21 2019

@author: Ferdawis
"""
import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """This class is used to describe ships"""
    def __init__(self,ai_settings,screen):
        super().__init__()
        """Initialize the ship, and set its starting position."""
        self.screen=screen
        self.ai_settings=ai_settings
        #load the image and get the images.rect
        self.image=pygame.image.load('images/ship.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        #set the ship's position
        self.rect.centerx=self.screen_rect.centerx
        self.rect.centery=self.screen_rect.bottom
        #position flags
        self.moving_right=False
        self.moving_left=False
        self.moving_up=False
        self.moving_down=False
        #Store a decimal value for the ship's center.
        self.center=float(self.rect.centerx)
        self.vertical=float(self.rect.centery)
        
    def update(self):
        if (self.moving_right) and (self.rect.right<self.screen_rect.right):
            self.center+=self.ai_settings.ship_speed_factor
        if (self.moving_left) and (self.rect.left>self.screen_rect.left):
            self.center-=self.ai_settings.ship_speed_factor
        if (self.moving_up) and (self.rect.top>self.screen_rect.top):
            self.vertical-=self.ai_settings.ship_speed_factor
        if (self.moving_down) and (self.rect.bottom<self.screen_rect.bottom):
            self.vertical+=self.ai_settings.ship_speed_factor    
        self.rect.centerx=self.center
        self.rect.centery=self.vertical
    
    def blitme(self):
        self.screen.blit(self.image,self.rect)
    def center_ship(self):
        self.center = self.screen_rect.centerx
        self.vertical = self.screen_rect.bottom
        
        
