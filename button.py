# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 14:32:27 2019

@author: Ferdawis
"""

import pygame

class Button():
    def __init__(self, ai_settings, screen, msg):
        """ Initialize the button's properties """
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        # Set the button's size and other features
        self.width, self.height = 200,50
        self.button_color = (0,255,0)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None,48)
        
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center
        
        self.prep_msg(msg)
        
    def prep_msg(self,msg):
        """ Render the message as an image and put it 
            in the center of the button """
        self.msg_image = self.font.render(msg,True,self.text_color,
                                           self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        
    def draw_button(self):
        #draw a button filled with color the draw the text
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)