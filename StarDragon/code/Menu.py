#!/usr/bin/python
#-*- coding: utf-8 -*-
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH


class Menu:
    def __init__(self, window):
        self.Window: Surface = window
        self.Surf = pygame.image.load('./asset/MenuBG.png')
        self.rect = self.Surf.get_rect(left=-500, top=-200)

    def run(self):
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)
        while True:
            self.Window.blit(source=self.Surf, dest=self.rect)
            self.menu_text(80, "Dragon", (236, 28, 36), ((WIN_WIDTH/2), 100))
            pygame.display.flip()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='Lucida Sans Typewriter', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.Window.blit(source=text_surf, dest=text_rect)

