from .chess_statue import ChessBoard
from .pond import ParkPond
from .modern_art import Art
from .big_tree import BigTree
from .fountain import ParkFountain

import random

misc_list = ['chess_statue', 'big_tree', 'fountain', 'pond', 'modern_art']


class MiscBuilder:
    def build(self, misc_object, x, y, z):
        biome = misc_object.biome
        mc_instance = misc_object.mc_instance
        i = random.randint(0, 4)

        if misc_list[i] == 'chess_statue':
            misc_obj = ChessBoard(biome, mc_instance)
        elif misc_list[i] == 'big_tree':
            misc_obj = BigTree(biome, mc_instance)
        elif misc_list[i] == 'fountain':
            misc_obj = ParkFountain(biome, mc_instance)
        elif misc_list[i] == 'pond':
            misc_obj = ParkPond(biome, mc_instance)
        else:
            misc_obj = Art(biome, mc_instance)

        misc_obj.build(x, y, z)
