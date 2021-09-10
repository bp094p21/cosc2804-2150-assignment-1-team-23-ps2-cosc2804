#this is a test to see if i can build one, will make it modular later

from mcpi.minecraft import Minecraft 
mc = Minecraft.create()
class park_fountain():
    def __init__(self) -> None:
        self.air = 0
        self.ground = 2
        self.tree = 17
        self.leaves = 18
        self.water = 8
        self.slab = 44
        self.stone = 98
    def playerPosition(self):
        x, y, z = mc.player.getPos()
        return x, y, z
    def buildFoundation(self, x, y, z):
        mc.setBlocks(x, y-1, z, x - 14, y - 14, z - 14, self.ground)
    def buildPath(self,x,y,z):
        mc.setBlocks(x-3,y,z-3,x-11,y,z-11,self.slab)
    def buildFountain(self,x,y,z):
        mc.setBlocks(x-4,y,z-4,x-10,y,z-10,self.stone)
        mc.setBlocks(x-4,y-1,z-4,x-10,y,z-10,self.stone)
        mc.setBlocks(x-5,y,z-5,x-9,y,z-9,self.air)

park = park_fountain()
x,y,z = park.playerPosition()
park.buildFoundation(x,y,z)
park.buildPath(x,y,z)
park.buildFountain(x,y,z)