from construction.building.misc.misc import Misc
import construction.building.misc.block_list as b
class Art(Misc):
    def __init__(self) -> None:
        super().__init__()
    def make_artwork(self,x,y,z):
        self.mc.setBlocks(x+3,y,z+3,x+11,y+8,z+11,b.MISC_BLOCKS[self.theme_string]['sub_block'])
        for i in range(10):
            self.mc.setBlocks(x+i,y+i,z+1,x+i+2,y+i+2,z+i+2,self.air)
    def build(self,x,y,z):
        self.build_foundation(x,y,z)
        self.make_artwork(x,y,z)
    
"""park = Art()    
x,y,z = park._player_position()
park.build(x,y,z)"""
        