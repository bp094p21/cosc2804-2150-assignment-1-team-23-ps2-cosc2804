from .misc import Misc
from .block_list import MISC_BLOCKS


class Art(Misc):
    def __init__(self, biome, mc):
        super().__init__(biome, mc)
    def make_artwork(self,x,y,z):
        self.mc.setBlocks(x+3,y,z+3,x+11,y+8,z+11,MISC_BLOCKS[self.theme]['sub_block'])
        for i in range(10):
            self.mc.setBlocks(x+i,y+i,z+1,x+i+2,y+i+2,z+i+2,self.air)
    def build(self,x,y,z):
        self.build_foundation(x,y,z)
        self.make_artwork(x,y,z)