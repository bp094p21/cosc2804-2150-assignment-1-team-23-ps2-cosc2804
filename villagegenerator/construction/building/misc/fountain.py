# this is a test to see if i can build one, will make it modular later

from mcpi.minecraft import Minecraft
from villagegenerator.construction.building.building import Building

mc = Minecraft.create()


class ParkFountain(Building):
    def __init__(self):
        self.air = 0
        self.ground = 2
        self.tree = 17
        self.leaves = 18
        self.water = 8
        self.slab = 44
        self.stone = 98

    # put whatever you need here to build a parkfountain object. this will ultimately be the method that is called
    # from the framework.
    def build(self):
        pass

    def player_position(self):
        x, y, z = mc.player.getPos()
        return x, y, z

    def build_foundation(self, x, y, z):
        mc.setBlocks(x, y - 1, z, x + 14, y - 14, z + 14, self.ground)

    def build_path(self, x, y, z):
        mc.setBlocks(x + 3, y, z + 3, x + 11, y, z + 11, self.slab)

    def build_fountain(self, x, y, z):
        mc.setBlocks(x + 4, y, z + 4, x + 10, y - 1, z + 10, self.stone)
        mc.setBlocks(x + 5, y, z + 5, x + 9, y, z + 9, self.air)
        mc.setBlocks(x + 7, y, z + 7, x + 7, y + 6, z + 7, self.stone)
        mc.setBlocks(x + 7, y + 6, z + 7, x + 7, y + 6, z + 7, self.water)


park = ParkFountain()
x, y, z = park.player_position()
park.build_foundation(x, y, z)
park.build_path(x, y, z)
park.build_fountain(x, y, z)
