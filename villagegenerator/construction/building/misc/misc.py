from mcpi.minecraft import Minecraft
import random
import sys
import block as b
sys.path.append('../')
import themes

misc_list = ['chess_statue','big_tree','fountain','pond','modern_art']
from chess_statue import ChessBoard
from pond import ParkPond
from modern_art import Art
from big_tree import bigTree
from fountain import ParkFountain
from mcpi.minecraft import Minecraft

#types of misc objects{open nature area, park features, statue-like objects}
#theme order{0= modern, 1= mediterranean, 2= magic}


class BuildingBlocks():
    def __init__(self) -> None:
        self.blocklist = {
            'ground':[b.GRASS,b.SAND, b.BRICKS_NETHER_RED],
            "ground_base":[b.STONE,b.SANDSTONE,b.COBBLESTONE],
            'main_block':[b.CONCRETE, b.TERRACOTTA,b.PURPUR_BLOCK],
            'sub_block':[b.PILLAR_QUARTZ,b.TERRACOTTA_WHITE_GLAZED,b.OBSIDIAN],
            'main_slab':[(43,0),(43,1),(204)],
            "wood":[b.WOOD_PLANKS,b.WOOD_PLANKS.withData(4),b.WOOD_PLANKS.withData(5)],
            'plant_stem':[b.TIMBER_LOG,81, b.LOG.withData(1)],
            'plant_leaves':[b.LEAVES,0,213],
            'main_light_block':[b.SEA_LANTERN,b.SEA_LANTERN,b.GLOWSTONE],
            'torch':[b.TORCH,b.TORCH,b.TORCH_REDSTONE],
            'flower':[b.FLOWER_RED,b.AIR, b.MUSHROOM_RED],
            'shrubs':[b.GRASS_TALL,31,31]
        }
    
class Misc():
    def __init__(self) -> None:
        self.mc = Minecraft.create()
        self.air = 0
        block_type = None
        self.biome = random.randint(1,3)
        self.balls = b.MISC_BLOCKS['modern']['ground']
        """if biome == 'modern':
            block_type = 0
        elif biome == 'sand':
            block_type = 1
        else:
            block_type = 2"""


        """self.air = 0
        self.ground_array = [blockthing.blocklist['ground'][block_type], blockthing.blocklist['ground_base'][block_type] ]
        self.building_array = [blockthing.blocklist['main_block'][block_type],blockthing.blocklist['sub_block'][block_type],blockthing.blocklist['wood'][block_type]]
        self.ground_base = blockthing.blocklist['ground_base'][block_type]
        self.slab = blockthing.blocklist['main_slab'][block_type]
        self.plant_array =[blockthing.blocklist['plant_stem'][block_type],blockthing.blocklist['plant_leaves'][block_type]]
        self.lighting_options = [blockthing.blocklist['main_light_block'][block_type],blockthing.blocklist['torch'][block_type]]
        self.greenery = [blockthing.blocklist['flower'][block_type],blockthing.blocklist['shrubs'][block_type]]
        self.building_wood = blockthing.blocklist['wood'][block_type]"""
    
    def _player_position(self):
        x, y, z = self.mc.player.getPos()
        return x, y, z
    
    def random_placement(coordinate_one, coordinate_two):
                placement_x = random.randint(coordinate_one, coordinate_two)
                placement_z = random.randint(coordinate_one, coordinate_two)
                return placement_x, placement_z
    def build(self,x,y,z,theme,mc):
        misc_obj = None
        #i = random.randint(0,4)
        
        i = 0
       
        def place_flowers( x, y, z,theme):
            for i in range(15):
                placement_x, placement_z = self.random_placement(0, 14)
                mc.setBlocks(x + placement_x, y, z + placement_z, x + placement_x, y, z + placement_z, b.MISC_BLOCKS[theme]['flower'])
    
        def place_grass( x, y, z):
            for i in range(15):
                placement_x, placement_z = self.random_placement(0, 14)
                mc.setBlocks(x + placement_x, y, z + placement_z, x + placement_x, y, z + placement_z, b.MISC_BLOCKS[theme]['shrubs'])       

        def build_foundation(self,x, y, z):
            mc.setBlocks(x,y,z,x+14,y+14,z+14,self.air)
            mc.setBlocks(x, y - 1, z, x + 14, y - 14, z + 14, b.MISC_BLOCKS[theme]['ground'])
            mc.setBlocks(x,y-14,z,x+14,y-14,z+14,b.MISC_BLOCKS[theme]['ground_base'])
            place_flowers(x, y, z)
            place_grass(x,y,z)
            build_tree(x,y,z)

        
            
        def coords_tree(x, y, z):
            corner_choice = random.randint(1, 4)
            b = y
            if corner_choice == 1:
                a = x + 2
                c = z + 2
            elif corner_choice == 2:
                a = x + 2
                c = z + 12
            elif corner_choice == 3:
                a = x + 12
                c = z + 12
            else:
                a = x + 12
                c = z + 2
            return a, b, c

        def build_tree(x,y,z):  # builds a tree with new coordinates
            x2,y2, z2 =coords_tree(x,y,z)
            mc.setBlocks(x2,y2,z2, b.MISC_BLOCKS[theme]['ground'])
            mc.setBlocks(x2, y2+1, z2, x2, y2 + 5, z2, b.MISC_BLOCKS[theme]['plant_stem'])
            mc.setBlocks(x2 - 2, y2 + 5, z2 - 2, x2 + 2, y2 + 7, z2 + 2, b.MISC_BLOCKS[theme]['plant_leaves'])

        build_foundation(x,y,z)
        if misc_list[i] == 'chess_statue':
            misc_obj = ChessBoard()
            misc_obj.build(x,y,z,theme)
        elif misc_list[i] == 'big_tree':
            misc_obj = bigTree()
            misc_obj.build()
        elif misc_list[i] == 'fountain':
            misc_obj = ParkFountain()
            misc_obj.build()
        elif misc_list[i] == 'pond':
            misc_obj = ParkPond()
            misc_obj.build()
        else:
            misc_obj = Art()
            misc_obj.build() 


park = Misc()
list = BuildingBlocks()
x,y,z = 1,1,1
theme = 'modern'
mc = Minecraft.create()
park.build(x,y,z,theme,mc)
