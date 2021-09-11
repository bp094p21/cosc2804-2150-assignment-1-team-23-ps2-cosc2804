#this is a test to see if i can build one, will make it modular later
import random
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
        self.lantern = 169
        self.flower = 38
    def playerPosition(self):
        x, y, z = mc.player.getPos()
        return x, y, z
    def buildFoundation(self, x, y, z):
        mc.setBlocks(x, y-1, z, x + 14, y - 14, z + 14, self.ground)
    def buildPath(self,x,y,z):
        mc.setBlocks(x+3,y,z+3,x+11,y,z+11,self.slab)
    def random_placement(self,coordinate_one, coordinate_two): # decides placements of items in a range specified by user 
        placement_x = random.randint(coordinate_one,coordinate_two)
        placement_z = random.randint(coordinate_one,coordinate_two)
        return placement_x, placement_z
    def place_flowers(self,x,y,z):
        for i in range(15):
            placement_x ,placement_z = self.random_placement(0, 14)
            mc.setBlocks(x+placement_x, y, z+placement_z, x+placement_x, y , z+placement_z, self.flower,2)
    def buildFountain(self,x,y,z):
        mc.setBlocks(x+4,y,z+4,x+10,y-1,z+10,self.stone)
        mc.setBlocks(x+5,y,z+5,x+9,y,z+9,self.air)
        mc.setBlocks(x+7,y,z+7,x+7,y+5,z+7,self.stone)

        mc.setBlocks(x+4,y,z+4,x+4,y,z+4,self.lantern)
        mc.setBlocks(x+10,y,z+10,x+10,y,z+10,self.lantern)
        mc.setBlocks(x+10,y,z+4,x+10,y,z+4,self.lantern)
        mc.setBlocks(x+4,y,z+10,x+4,y,z+10,self.lantern)

        mc.setBlocks(x+7,y+5,z+7,x+7,y+5,z+7,self.water)
park = park_fountain()
x,y,z = park.playerPosition()
park.buildFoundation(x,y,z)
park.place_flowers(x,y,z)
park.buildPath(x,y,z)
park.buildFountain(x,y,z)