

from misc import Misc

class ParkFountain(Misc):
    # put whatever you need here to build a parkfountain object. this will ultimately be the method that is called
    # from the framework.
    def __init__(self) -> None:
        super().__init__(self)

    def build(self):
        pass

    def build_path(self, x, y, z):
        self.mc.setBlocks(x + 3, y, z + 3, x + 11, y, z + 11, self.slab)

    def build_fountain(self, x, y, z):
        self.mc.setBlocks(x + 4, y, z + 4, x + 10, y - 1, z + 10, self.building_array[0])
        self.mc.setBlocks(x + 5, y, z + 5, x + 9, y, z + 9, self.air)
        self.mc.setBlocks(x+7,y,z+7,x+7,y+5,z+7,self.building_array[1])

        self.mc.setBlocks(x+4,y,z+4,x+4,y,z+4,self.lighting_options[0])
        self.mc.setBlocks(x+10,y,z+10,x+10,y,z+10,self.lighting_options[0])
        self.mc.setBlocks(x+10,y,z+4,x+10,y,z+4,self.lighting_options[0])
        self.mc.setBlocks(x+4,y,z+10,x+4,y,z+10,self.lighting_options[0])

        self.mc.setBlocks(x+7,y+5,z+7,x+7,y+5,z+7,self.water)
    def build_park(self,x,y,z):
        self.build_foundation(x,y,z)
        self.build_tree(x,y,z)
        self.build_path(x,y,z)
        self.build_fountain(x,y,z)

    
thing = ParkFountain()
x, y, z = thing._player_position()
thing.build_park(x,y,z)
