from mcpi.minecraft import Minecraft
import random


class Misc():
    types = ['park', 'statue', 'fountain', 'library']
    misc_obj = None

    # Public Method
    def __init__(self):

        # self.mc = Minecraft.create()
        self.air = 0
        self.ground = 2
        self.tree = 17
        self.leaves = 18
        self.water = 8
        self.slab = 44
        self.stone = 98
        self.lantern = 169
        self.flower = 38
        self.grass_plant = 31

    def build(self):
        print(1)
        self._randomly_select_misc_type()
        self.misc_obj.build()

    # Internal Methods
    def _randomly_select_misc_type(self):
        type = None
        # Randomly select item from self.types and assign return value to type

        if type == 'park':
            self.misc_obj = Park()
        elif type == 'statue':
            self.misc_obj = Statue()

    def _player_position(self):
        x, y, z = self.mc.player.getPos()
        return x, y, z

    def _place_flowers(self, x, y, z):
        for i in range(15):
            placement_x, placement_z = self.random_placement(0, 14)
            self.mc.setBlocks(x + placement_x, y, z + placement_z, x + placement_x, y, z + placement_z, self.flower, 2)

    def _place_grass(self, x, y, z):
        for i in range(15):
            placement_x, placement_z = self.random_placement(0, 14)
            self.mc.setBlocks(x + placement_x, y, z + placement_z, x + placement_x, y, z + placement_z,
                              self.grass_plant, 1)

    def _build_foundation(self, x, y, z):
        self.mc.setBlocks(x, y, z, x + 14, y + 14, z + 14, self.air)
        self.mc.setBlocks(x, y - 1, z, x + 14, y - 14, z + 14, self.ground)
        self._place_flowers(x, y, z)
        self._place_grass(x, y, z)

    def random_placement(self, coordinate_one, coordinate_two):
        placement_x = random.randint(coordinate_one, coordinate_two)
        placement_z = random.randint(coordinate_one, coordinate_two)
        return placement_x, placement_z

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
        a, b, c = self.coords_tree(x, y, z)
        self.mc.setBlocks(a, b, c, a, b + 5, c, self.tree)
        self.mc.setBlocks(a - 2, b + 5, c - 2, a + 2, b + 7, c + 2, self.leaves)


class Park(Misc):
    def build(self):
        pass


class Statue(Misc):
    pass


park = Park()
park.build()
