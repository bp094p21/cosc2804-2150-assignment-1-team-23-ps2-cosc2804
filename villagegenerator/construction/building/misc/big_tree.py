from misc import Misc
import random
class bigTree(Misc):
    def __init__(self) -> None:
        super().__init__()
        self.height = random.randint(2,25)
        if self.biome == 2:
            self.wood = self.building_wood
        else:
            self.wood = self.plant_array[0]
    def big_tree_build(self,x,y,z):
        self.build_foundation(x,y,z)
        self.mc.setBlocks(x+3,y+self.height,z+3,x+11,y+self.height+5,z+11,self.plant_array[1])
        self.mc.setBlocks(x+6,y,z+6,x+8,y+self.height+3,z+8,self.wood)
    def big_branches(self,x,y,z):
        for i in range(3):
            self.mc.setBlocks(x+6+i,y + self.height/2 ,z+2+i ,x+8-i, y+self.height/2-i,z+5,self.plant_array[1])
            self.mc.setBlocks(x+6+i,y + self.height/3 ,z+10-i ,x+8, y+self.height/3-i,z+12-i,self.plant_array[1])
            self.mc.setBlocks(x+8,y + self.height/4 ,z+7+i ,x+12-i, y+self.height/4-i,z+9-i,self.plant_array[1])
            self.mc.setBlocks(x+3+i,y + self.height/1.5 ,z+6+i ,x+5, y+self.height/1.5-i,z+9-i,self.plant_array[1]) #make leaves go down y axis and shrink by oneblock
    def build(self, x,y,z):
            self.big_tree_build(x, y, z)
            self.big_branches(x,y,z)
            self.build_tree(x,y,z)

tree = bigTree()
x, y, z = tree._player_position()
tree.build(x,y,z)