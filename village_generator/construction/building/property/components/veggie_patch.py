from components.component import Component
import block as b

class VeggiePatch(Component):
    # Class attributes
    type: str = 'veggie_patch'
    # Instance attributes
    start_v3 = None
    end_v3: int = None
    block: b.Block = None
    def __repr__(self):
        return f"🖨  Printing object.__repr__:\n\n{type(self)}\start_v3: {self.start_v3},\nend_v3: {self.end_v3},\nblock: {self.block}\n"
    def __init__(self, start_v3, end_v3, path_block):
        self.start_v3 = start_v3
        self.end_v3 = end_v3
        self.block = path_block

# TESTING
if __name__ == '__main__':
    from mcpi import minecraft as m
    mc = m.Minecraft.create()
    player_v3 = mc.player.getPos()
    orientation = 0
    entrance = VeggiePatch(start_V3=player_v3, end_v3=player_v3, door_block=b.COBBLESTONE)

#example code that might be used for vegepatch and flowerbed
"""from mcpi.minecraft import Minecraft
import random
def _plant_case(x,y,z,mc):
    
    mc.setBlocks(x-1,y,z,x-1,y,z+1,167,6)
    mc.setBlocks(x+2,y,z,x+2,y,z+1,167,7)
    mc.setBlocks(x,y,z-1,x+1,y,z-1,167,12)
    mc.setBlocks(x,y,z+2,x+1,y,z+2,167,13)
def make_vege_patch(x,y,z,mc):
    mc.setBlocks(x,y,z,x+1,y,z+1,60)
    _plant_case(x,y,z,mc)
    for i in range(2):
        mc.setBlocks(x+i,y+1,z+i,x+i,y+1,z+i,142)
        mc.setBlocks(x+1-i,y+1,z+i,x+1-i,y+1,z+i,141)
    

def make_flowers(x,y,z,mc):
    _plant_case(x,y,z,mc)
    
    mc.setBlocks(x,y,z,x+1,y,z+1,2)
    
    # mc.setBlocks(x,y+1,z,x+1,y+1,z+1,175)
    # mc.setBlocks(x,y+2,z,x+1,y+2,z+1,175)
    for i in range(2):
        mc.setBlocks(x+i,y+1,z+i,x+i,y+1,z+i,38,random.randint(0,8))
        mc.setBlocks(x+1-i,y+1,z+i,x+1-i,y+1,z+i,38,random.randint(0,8))

    
#testing purposes
if __name__ == "__main__":
    mc = Minecraft.create()
    x,y,z, = mc.player.getPos()
    make_vege_patch(x,y,z,mc)   
    make_flowers(x+4,y,z,mc)
"""
	