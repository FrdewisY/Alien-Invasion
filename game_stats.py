# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 03:23:33 2019

@author: Ferdawis
"""

class GameStats():
    """ Track statistics for Alien Invasion. """
    def __init__(self,ai_settings):
	 
        self.ai_settings = ai_settings
        self.reset_stats()
        self.high_score = 0
		#Start Alien Invasion in an active state.
        self.game_active = False
        
    def reset_stats(self):
	    #Initialize statistics that can change during the game.
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
    
        