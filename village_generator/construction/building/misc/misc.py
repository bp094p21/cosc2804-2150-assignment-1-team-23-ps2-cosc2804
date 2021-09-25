import random
from .block_list import MISC_BLOCKS
from .theme import get_player_theme


class Misc:
    def __init__(self, biome, mc_instance) -> None:
        self.mc = mc_instance
        self.air = 0

        self.theme = get_player_theme(biome)

    def random_placement(self, coordinate_one, coordinate_two):
        placement_x = random.randint(coordinate_one, coordinate_two)
        placement_z = random.randint(coordinate_one, coordinate_two)
        return placement_x, placement_z

    def place_flowers(self, x, y, z, ):
        for i in range(15):
            placement_x, placement_z = self.random_placement(0, 14)
            self.mc.setBlocks(x + placement_x, y, z + placement_z, x + placement_x, y, z + placement_z,
                              MISC_BLOCKS[self.theme]['flower'])

    def place_grass(self, x, y, z):
        for i in range(15):
            placement_x, placement_z = self.random_placement(0, 14)
            self.mc.setBlocks(x + placement_x, y, z + placement_z, x + placement_x, y, z + placement_z,
                              MISC_BLOCKS[self.theme]['shrubs'])

    def build_foundation(self, x, y, z):
        self.mc.setBlocks(x, y, z, x + 14, y + 14, z + 14, self.air)
        self.mc.setBlocks(x, y - 1, z, x + 14, y - 14, z + 14, MISC_BLOCKS[self.theme]['ground'])
        self.mc.setBlocks(x, y - 14, z, x + 14, y - 14, z + 14, MISC_BLOCKS[self.theme]['ground_base'])
        self.place_flowers(x, y, z)
        self.place_grass(x, y, z)

    def coords_tree(self, x, y, z):
        corner_choice = random.randint(1, 4)
        b = y
        if corner_choice == 1:
            a = x + 2
            c = z + 2
        elif corner_choice == 2:
            a = x + 2
            c = z + 12
        elif corner_choice == 3:
            a = x + 12
            c = z + 12
        else:
            a = x + 12
            c = z + 2
        return a, b, c

    def build_tree(self, x, y, z):  # builds a tree with new coordinates
        x2, y2, z2 = self.coords_tree(x, y, z)
        self.mc.setBlocks(x2, y2, z2, x2, y2, z2, MISC_BLOCKS[self.theme]['ground'])
        self.mc.setBlocks(x2, y2 + 1, z2, x2, y2 + 5, z2, MISC_BLOCKS[self.theme]['plant_stem'])
        self.mc.setBlocks(x2 - 2, y2 + 5, z2 - 2, x2 + 2, y2 + 7, z2 + 2, MISC_BLOCKS[self.theme]['plant_leaves'])
