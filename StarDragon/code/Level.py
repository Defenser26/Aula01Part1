#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Entity import Entity


class Level:

    def __int__(self, window, name, menu_option):
        self.window = window
        self.name = name
        self.mode = menu_option
        self.entity_list: list[Entity] = []



    def run(self, ):
        pass
