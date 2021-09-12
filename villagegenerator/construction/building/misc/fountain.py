# this is a test to see if i can build one, will make it modular later
from villagegenerator.construction.building.misc.park import Park

class ParkFountain(Park):
    
    # put whatever you need here to build a parkfountain object. this will ultimately be the method that is called
    # from the framework.
    def __init__(self) -> None:
        Park.__init__(self)

    def build(self):
        pass

    def build_path(self, x, y, z):
        self.mc.setBlocks(x + 3, y, z + 3, x + 11, y, z + 11, self.slab)

    def build_fountain(self, x, y, z):
        self.mc.setBlocks(x + 4, y, z + 4, x + 10, y - 1, z + 10, self.stone)
        self.mc.setBlocks(x + 5, y, z + 5, x + 9, y, z + 9, self.air)
        self.mc.setBlocks(x + 7, y, z + 7, x + 7, y + 6, z + 7, self.stone)
        self.mc.setBlocks(x + 7, y + 6, z + 7, x + 7, y + 6, z + 7, self.water)


thing = ParkFountain()
x, y, z = thing.player_position()
thing.build_foundation(x, y, z)
thing.build_path(x, y, z)
thing.build_fountain(x, y, z)
