# basic testing, will make it better later
from mcpi.minecraft import Minecraft
from villagegenerator.construction.building.building import Building
import random

mc = Minecraft.create()


class ParkPond(Building):
    def __init__(self):
        self.air = 0
        self.ground = 2
        self.tree = 17
        self.leaves = 18
        self.water = 8
        self.slab = 44
        self.lantern = 169
        self.lilypad = 111
        self.flower = 38

    # put whatever you need here to build a parkpond object. this will ultimately be the method that is called from the
    # framework.
    def build(self):
        pass

    # could take the two functions that create the base and turn that into another module that other classes inherit
    def player_position(self):
        x, y, z = mc.player.getPos()
        return x, y, z

    def build_foundation(self, x, y, z):
        mc.setBlocks(x, y - 1, z, x + 14, y - 14, z + 14, self.ground)

    # decides placements of items in a range specified by user
    def random_placement(self, coordinate_one, coordinate_two):
        placement_x = random.randint(coordinate_one, coordinate_two)
        placement_z = random.randint(coordinate_one, coordinate_two)
        return placement_x, placement_z

    def place_flowers(self, x, y, z):
        for i in range(15):
            placement_x, placement_z = self.random_placement(0, 14)
            mc.setBlocks(x + placement_x, y, z + placement_z, x + placement_x, y, z + placement_z, self.flower, 2)

    def fill_pond(self, x, y, z):  # as name suggests, digs pond and fills it
        mc.setBlocks(x + 3, y - 1, z + 3, x + 11, y - 5, z + 11, self.water)
        mc.setBlocks(x + 3, y - 5, z + 3, x + 11, y - 5, z + 11, self.lantern)
        mc.setBlocks(x + 2, y, z + 2, x + 12, y, z + 12, self.slab)
        mc.setBlocks(x + 3, y, z + 3, x + 11, y, z + 11, self.air)
        # placement of lilypads
        for i in range(6):
            placement_x, placement_z = self.random_placement(4, 11)
            mc.setBlocks(x + placement_x, y, z + placement_z, x + placement_x, y, z + placement_z, self.lilypad)

    # picks a number from 1 to four and uses that to pick a corner for the tree, stores coordinates to variables a,b,c
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

    def build_tree(self, a, b, c):  # builds a tree with new coordinates
        mc.setBlocks(a, b, c, a, b + 5, c, self.tree)
        mc.setBlocks(a - 2, b + 5, c - 2, a + 2, b + 7, c + 2, self.leaves)

    def build_pond(self, x, y, z):  # combines functions and makes whole structure
        self.place_flowers(x, y, z)
        self.build_foundation(x, y, z)
        self.fill_pond(x, y, z)
        a, b, c = self.coords_tree(x, y, z)
        self.build_tree(a, b, c)


pond = ParkPond()
x, y, z = pond.player_position()
pond.build_pond(x, y, z)
