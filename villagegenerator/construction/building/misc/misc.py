
from mcpi.minecraft import Minecraft
import random
import sys
sys.path.append('../../building')
import property.block as b

#types of misc objects{open nature area, park features, statue-like objects}
#theme order{0= modern, 1= mediterranean, 2= magic}
mc = Minecraft.create()

class BuildingBlocks():
    blocklist = {
        'ground':[b.GRASS,b.SAND, b.MOSSY_COBBLESTONE],
        "ground_base":[b.STONE,b.SANDSTONE,b.COBBLESTONE],
        'main_block':[b.CONCRETE, b.TERRACOTTA,b.PURPUR_BLOCK],
        'sub_block':[b.PILLAR_QUARTZ,b.TERRACOTTA_WHITE_GLAZED,b.OBSIDIAN],
        'main_slab':[b.STONE_SLAB,b.STONE_SLAB.withData(1),b.PURPUR_SLAB],
        "wood":[b.WOOD_PLANKS,b.WOOD_PLANKS.withData(4),b.WOOD_PLANKS.withData(5)],
        'plant_stem':[b.TIMBER_LOG,b.CACTUS, b(162.1)],
        'plant_leaves':[b.LEAVES,b.LEAVES2,b.LEAVES2.withData(1)],
        'main_light_block':[b.SEA_LANTERN,b.SEA_LANTERN,b.GLOWSTONE],
        'torch':[b.TORCH,b.TORCH,b.TORCH_REDSTONE],
        'flower':[b.FLOWER_RED,b.AIR, b.MUSHROOM_RED],
        'shrubs':[b.GRASS_TALL.withData(1),b.GRASS_TALL,b.GRASS_TALL.withData(2)],
    }
class Misc():
    types = ["open_nature","park","statue"]
    misc_obj = None
    def __init__(self) -> None:
        biome = None
        block_type = None
        if biome == 'modern':
            block_type = 0
        elif biome == 'mediterranean':
            block_type = 1
        else:
            block_type = 2
        blocklist = BuildingBlocks()
        self.air = 1
        self.ground_array = [blocklist['ground'][block_type], blocklist['ground_base'][block_type] ]
        self.building_array = [blocklist['main_block'][block_type],blocklist['sub_block'][block_type],blocklist['wood'][block_type]]
        self.slab = blocklist['main_slab'][block_type]
        self.plant_array =[blocklist['plant_stem'][block_type],blocklist['plant_leaves'][block_type]]
        self.lighting_options = [blocklist['main_light_block'][block_type],blocklist['torch'][block_type]]
        self.greenery = [blocklist['flower'][block_type],blocklist['shrubs'][block_type]]

    def _player_position(self):
        x, y, z = mc.player.getPos()
        return x, y, z
    
    def _get_biome(self):
        biome = mc.getBiome()

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
            mc.setBlocks(x + placement_x, y, z + placement_z, x + placement_x, y, z + placement_z, self.greenery[0])
    
    def place_grass(self, x, y, z):
        for i in range(15):
            placement_x, placement_z = self.random_placement(0, 14)
            mc.setBlocks(x + placement_x, y, z + placement_z, x + placement_x, y, z + placement_z, self.greenery[1], 1)       

    def build_foundation(self, x, y, z):
        mc.setBlocks(x,y,z,x+14,y+14,z+14,self.air)
        mc.setBlocks(x, y - 1, z, x + 14, y - 14, z + 14, self.ground_array[0])
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
        mc.setBlocks(a, b, c, a, b + 5, c, self.plant_array[0])
        mc.setBlocks(a - 2, b + 5, c - 2, a + 2, b + 7, c + 2, self.plant_array[1])

park = Misc()
park.build_foundation
park.build_tree    