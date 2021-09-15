
from mcpi.minecraft import Minecraft
import random
import sys

import block as b

#types of misc objects{open nature area, park features, statue-like objects}
#theme order{0= modern, 1= mediterranean, 2= magic}


class BuildingBlocks():
    def __init__(self) -> None:
        
        self.blocklist = {
            'ground':[b.GRASS,b.SAND, b.MOSSY_COBBLESTONE],
            "ground_base":[b.STONE,b.SANDSTONE,b.COBBLESTONE],
            'main_block':[b.CONCRETE, b.TERRACOTTA,b.PURPUR_BLOCK],
            'sub_block':[b.PILLAR_QUARTZ,b.TERRACOTTA_WHITE_GLAZED,b.OBSIDIAN],
            'main_slab':[(43,0),(43,1),(204)],
            "wood":[b.WOOD_PLANKS,b.WOOD_PLANKS.withData(4),b.WOOD_PLANKS.withData(5)],
            'plant_stem':[b.TIMBER_LOG,81, 162],
            'plant_leaves':[b.LEAVES,0,b.LEAVES2.withData(1)],
            'main_light_block':[b.SEA_LANTERN,b.SEA_LANTERN,b.GLOWSTONE],
            'torch':[b.TORCH,b.TORCH,b.TORCH_REDSTONE],
            'flower':[b.FLOWER_RED,b.AIR, b.MUSHROOM_RED],
            'shrubs':[b.GRASS_TALL,31,b.GRASS_TALL.withData(2)]
        }
class Misc():# find  imports random misc then misc will casll global function and build that

    types = ["open_nature","park","statue"]
    misc_obj = None
    def __init__(self) -> None:
        self.mc = Minecraft.create()
        self.water = 8
        block_type = None
        self.biome = random.randint(1,3)
        
        """if biome == 'modern':
            block_type = 0
        elif biome == 'sand':
            block_type = 1
        else:
            block_type = 2"""
        if self.biome == 1:
            block_type = 0
        elif self.biome == 2:
            block_type = 1
        else:
            block_type = 2
        blockthing = BuildingBlocks()

        self.air = 0
        self.ground_array = [blockthing.blocklist['ground'][block_type], blockthing.blocklist['ground_base'][block_type] ]
        self.building_array = [blockthing.blocklist['main_block'][block_type],blockthing.blocklist['sub_block'][block_type],blockthing.blocklist['wood'][block_type]]
        self.ground_base = blockthing.blocklist['ground_base'][block_type]
        self.slab = blockthing.blocklist['main_slab'][block_type]
        self.plant_array =[blockthing.blocklist['plant_stem'][block_type],blockthing.blocklist['plant_leaves'][block_type]]
        self.lighting_options = [blockthing.blocklist['main_light_block'][block_type],blockthing.blocklist['torch'][block_type]]
        self.greenery = [blockthing.blocklist['flower'][block_type],blockthing.blocklist['shrubs'][block_type]]
        self.building_wood = blockthing.blocklist['wood'][block_type]
    def _player_position(self):
        x, y, z = self.mc.player.getPos()
        return x, y, z
    
    #def _get_biome(self):
    #    biome = mc.getBiome()

    '''def _select_misc_type(self):
        i = random.randint(0,2)
        type = self.types[i]
        if type == 'park':
            self.misc_obj= Park()
        elif type == "open_nature":
            self.misc_obj = Nature()
        else:
            self.misc_obj = Statue()'''

    def place_flowers(self, x, y, z):
        for i in range(15):
            placement_x, placement_z = self.random_placement(0, 14)
            self.mc.setBlocks(x + placement_x, y, z + placement_z, x + placement_x, y, z + placement_z, self.greenery[0])
    
    def place_grass(self, x, y, z):
        for i in range(15):
            placement_x, placement_z = self.random_placement(0, 14)
            self.mc.setBlocks(x + placement_x, y, z + placement_z, x + placement_x, y, z + placement_z, self.greenery[1])       

    def build_foundation(self, x, y, z):
        self.mc.setBlocks(x,y,z,x+14,y+14,z+14,self.air)
        self.mc.setBlocks(x, y - 1, z, x + 14, y - 14, z + 14, self.ground_array[0])
        self.mc.setBlocks(x,y-14,z,x+14,y-14,z+14,self.ground_base)
        self.place_flowers(x, y, z)
        self.place_grass(x,y,z)

    def random_placement(self, coordinate_one, coordinate_two):
        placement_x = random.randint(coordinate_one, coordinate_two)
        placement_z = random.randint(coordinate_one, coordinate_two)
        return placement_x, placement_z
    def coords_tree(self, x, y, z):
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

    def build_tree(self, x,y,z):  # builds a tree with new coordinates
        a,b,c =self.coords_tree(x,y,z)
        self.mc.setBlocks(a,b,c,a,b,c,self.ground_array[0])
        self.mc.setBlocks(a, b+1, c, a, b + 5, c, self.plant_array[0])
        self.mc.setBlocks(a - 2, b + 5, c - 2, a + 2, b + 7, c + 2, self.plant_array[1])

"""class Park():
    def __init__(self) -> None:  # inbiult random  function for misc will choose one of these, then this class will inherit all of the fuinction from them and thus misc will inherit the pond or soemthing, after that it will build it
                               # perhaps create a new object /class 
                                    # don't actually need a park class, will just import then and then misc will carry out these functions

        import fountain
        import pond
        choice = random.randint(1,2)
        if choice == 1:
            park = fountain()
        else:
            park = pond()
        return park

class Nature():
    def __init__(self) -> None:
        pass
    import big_tree
class Statue():
    def __init__(self) -> None:
        pass
    import modern_art"""



park = Misc()
list = BuildingBlocks()
x,y,z = park._player_position()
#park._get_blocks(BuildingBlocks)
park.build_foundation(x,y,z)
park.build_tree(x,y,z)