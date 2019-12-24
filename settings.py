# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 12:26:27 2019

@author: Ferdawis
"""

class Settings():
    """To store all the settings in the game 'alien_invasion'"""
    def __init__(self):
        # Screen settings
        self.screen_width=1200
        self.screen_height=600
        self.bg_color=(230,230,230)
           
        # Ship settings
        self.ship_limit = 3
        
        # Bullet settings
        self.bullet_width = 3
        self.bullet_height= 15
        self.bullet_color = 35,60,67
        self.bullets_allowed = 4
               
        # Alien settings
        self.fleet_drop_speed = 10
        self.alien_points = 50
        self.score_scale = 2
        
        # How quickly the game speeds up.
        self.speedup_scale = 1.2
      
        
        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
           """Initialize settings that change throughout the game."""
           self.ship_speed_factor = 1.5
           self.bullet_speed_factor = 3
           self.alien_speed_factor = 1
           # fleet_direction of 1 represents right, -1 represents left.
           self.fleet_direction = 1
       
    def increase_speed(self):
            """ Increase all the speeds """
            self.ship_speed_factor *= self.speedup_scale
            self.bullet_speed_factor *= self.speedup_scale
            self.alien_speed_factor *= self.speedup_scale
            self.alien_points = int(self.alien_points * self.score_scale)
    
        