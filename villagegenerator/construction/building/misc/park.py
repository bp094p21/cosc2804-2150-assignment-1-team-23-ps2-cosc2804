from mcpi.minecraft import Minecraft

import random
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
        self.lantern = 169
        self.flower = 38
    def player_position(self):
        x, y, z = self.mc.player.getPos()
        return x, y, z
    def place_flowers(self, x, y, z):
        for i in range(15):
            placement_x, placement_z = self.random_placement(0, 14)
            self.mc.setBlocks(x + placement_x, y, z + placement_z, x + placement_x, y, z + placement_z, self.flower, 2)

    def build_foundation(self, x, y, z):
        self.mc.setBlocks(x, y - 1, z, x + 14, y - 14, z + 14, self.ground)
        self.place_flowers(x, y, z)

    def random_placement(self, coordinate_one, coordinate_two):
        placement_x = random.randint(coordinate_one, coordinate_two)
        placement_z = random.randint(coordinate_one, coordinate_two)
        return placement_x, placement_z

    