# basic testing, will make it better later
from mcpi.minecraft import Minecraft 
mc = Minecraft.create()
import random
class park_pond():
    def __init__(self) -> None:
        self.air = 0
        self.ground = 2
        self.tree = 17
        self.leaves = 18
        self.water = 8
        self.slab = 44
        self.lantern = 169
        self.lilypad = 111
    def playerPosition(self): # could take the two functions that create the base and turn that into another module that other classes inherit
        x, y, z = mc.player.getPos()
        return x, y, z
    def buildFoundation(self, x, y, z):
        mc.setBlocks(x, y-1, z, x + 14, y - 14, z + 14, self.ground)
    def makePond(self,x,y,z): #as name suggests, digs pond and fills it
        mc.setBlocks(x+3, y-1, z+3, x + 11, y - 5, z + 11, self.water)
        mc.setBlocks(x+3, y-5, z+3, x + 11, y - 5, z + 11, self.lantern)
        mc.setBlocks(x+2, y, z+2, x + 12, y , z + 12, self.slab)
        mc.setBlocks(x+3, y, z+3, x + 11, y , z + 11, self.air)
        #placement of lilypads
        for i in range(6):
            placement_x = random.randint(4,11) # decides the placement of lilypads for each loop for the x value
            placement_z= random.randint(4,11) # decides placement for z value
            mc.setBlocks(x+placement_x, y, z+placement_z, x + placement_x, y, z + placement_z, self.lilypad)
    def coordsTree(self,x,y,z):
        corner_choice = random.randint(1,4)
        b = y
        if corner_choice == 1:
            a = x+2 
            c = z+2
        elif corner_choice == 2:
            a = x+ 2
            c = z+12
        elif corner_choice == 3:
            a = x+ 12
            c = z+12
        else:
            a = x+ 12
            c = z+2
        return a,b,c
    def buildTree(self,a,b,c):
        mc.setBlocks(a,b,c , a,b+5,c,self.tree)
        mc.setBlocks(a-2,b+5,c-2, a+2,b+7,c+2,self.leaves)
    
pond = park_pond()
x,y,z = pond.playerPosition()
pond.buildFoundation(x,y,z)
pond.makePond(x,y,z)
a,b,c = pond.coordsTree(x,y,z)
pond.buildTree(a,b,c)