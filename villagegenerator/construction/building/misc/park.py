from mcpi.minecraft import Minecraft
from villagegenerator.construction.building.building import Building

class Park():
    def __init__(self) -> None:
        self.mc = Minecraft.create()
        self.air = 0
        self.ground = 2
        self.tree = 17
        self.leaves = 18
        self.water = 8
        self.slab = 44
        self.stone = 98
    def player_position(self):
        x, y, z = self.mc.player.getPos()
        return x, y, z

    def build_foundation(self, x, y, z):
        self.mc.setBlocks(x, y - 1, z, x + 14, y - 14, z + 14, self.ground)