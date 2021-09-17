misc_list = ['chess_statue','big_tree','fountain','pond','modern_art']
from chess_statue import ChessBoard
from pond import ParkPond
from modern_art import Art
from big_tree import bigTree
from fountain import ParkFountain
from mcpi.minecraft import Minecraft

import random
#have code that 
# create misc object instead 

class Builder:
    def __init__(self) -> None:
        pass
    def build(self,x,y,z ):
        misc_obj = None
        i = random.randint(0,4)
        
        # i = 4
       
        if misc_list[i] == 'chess_statue':
            misc_obj = ChessBoard()
            misc_obj.build(x,y,z)
        elif misc_list[i] == 'big_tree':
            misc_obj = bigTree()
            misc_obj.build(x,y,z)
        elif misc_list[i] == 'fountain':
            misc_obj = ParkFountain()
            misc_obj.build(x,y,z)
        elif misc_list[i] == 'pond':
            misc_obj = ParkPond()
            misc_obj.build(x,y,z)
        else:
            misc_obj = Art()
            misc_obj.build(x,y,z) 
thing = Builder()
mc = Minecraft.create()
x,y,z, = mc.player.getPos()
thing.build(x,y,z)