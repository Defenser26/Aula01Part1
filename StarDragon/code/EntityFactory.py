#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Background import  Background


class EntityFactory:

    @staticmethod
    def get_entity(self, entity_name: str, position: tuple):
        match entity_name:
            case    'Level1Bg':
                Background(f'Level1Bg0', position)
        pass

