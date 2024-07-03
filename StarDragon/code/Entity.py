#!/usr/bin/python
#-*- coding: utf-8 -*-
from abc import ABC, abstractmethod

import pygame.image


class Entity:
    def __init__(self):
        self.name = None
        self.surf = None
        self.rect = None

    def move(self):
        pass



