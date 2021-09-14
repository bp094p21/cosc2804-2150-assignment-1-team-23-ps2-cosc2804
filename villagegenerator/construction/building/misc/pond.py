# basic testing, will make it better later

from park import Park

class ParkPond(Park):
    def __init__(self):
        Park.__init__(self)
        self.lilypad = 111
    # put whatever you need here to build a parkpond object. this will ultimately be the method that is called from the
    # framework.
    def build(self):
        pass
    # could take the two functions that create the base and turn that into another module that other classes inherit
    def player_position(self):
        x, y, z = self.mc.player.getPos()
        return x, y, z
    def fill_pond(self, x, y, z):  # as name suggests, digs pond and fills it
        self.mc.setBlocks(x + 3, y - 1, z + 3, x + 11, y - 5, z + 11, self.water)
        self.mc.setBlocks(x + 3, y - 5, z + 3, x + 11, y - 5, z + 11, self.lantern)
        self.mc.setBlocks(x + 2, y, z + 2, x + 12, y, z + 12, self.slab)
        self.mc.setBlocks(x + 3, y, z + 3, x + 11, y, z + 11, self.air)
        # placement of lilypads
        for i in range(6):
            placement_x, placement_z = self.random_placement(4, 11)
            self.mc.setBlocks(x + placement_x, y, z + placement_z, x + placement_x, y, z + placement_z, self.lilypad)
    # picks a number from 1 to four and uses that to pick a corner for the tree, stores coordinates to variables a,b,c

    def build_pond(self, x, y, z):  # combines functions and makes whole structure
        self.build_foundation(x, y, z)
        self.fill_pond(x, y, z)
        
        self.build_tree(x, y, z)

pond = ParkPond()
x, y, z = pond.player_position()
pond.build_pond(x, y, z)
