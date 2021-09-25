from .misc import Misc
from .block_list import MISC_BLOCKS


class ParkFountain(Misc):
 
    def __init__(self, biome, mc_instance):
        super().__init__(biome, mc_instance)
   
    def build_path(self, x, y, z):
        self.mc.setBlocks(x + 3, y, z + 3, x + 11, y, z + 11, MISC_BLOCKS[self.theme]['main_slab'])

    def build_fountain(self, x, y, z):
        self.mc.setBlocks(x + 4, y, z + 4, x + 10, y - 1, z + 10, MISC_BLOCKS[self.theme]['main_block'])
        self.mc.setBlocks(x + 5, y, z + 5, x + 9, y, z + 9, self.air)
        self.mc.setBlocks(x+7,y,z+7,x+7,y+5,z+7,MISC_BLOCKS[self.theme]['sub_block'])

        self.mc.setBlocks(x+4,y,z+4,x+4,y,z+4,MISC_BLOCKS[self.theme]['main_light_block'])
        self.mc.setBlocks(x+10,y,z+10,x+10,y,z+10,MISC_BLOCKS[self.theme]['main_light_block'])
        self.mc.setBlocks(x+10,y,z+4,x+10,y,z+4,MISC_BLOCKS[self.theme]['main_light_block'])
        self.mc.setBlocks(x+4,y,z+10,x+4,y,z+10,MISC_BLOCKS[self.theme]['main_light_block'])

        self.mc.setBlocks(x+7,y+5,z+7,x+7,y+5,z+7,MISC_BLOCKS[self.theme]['fountain_liquid'])
    def build(self,x,y,z):
        self.build_foundation(x,y,z)
        self.build_tree(x,y,z)
        self.build_path(x,y,z)
        self.build_fountain(x,y,z)
