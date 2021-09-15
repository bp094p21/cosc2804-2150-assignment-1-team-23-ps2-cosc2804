# basic testing, will make it better later

from misc import Misc

class ParkPond(Misc):
    def __init__(self)->None:
        super().__init__()
        self.lilypad = 111
    
    def build(self):
        pass
    
    def fill_pond(self, x, y, z):  # as name suggests, digs pond and fills it
        self.mc.setBlocks(x + 3, y - 1, z + 3, x + 11, y - 5, z + 11, self.water)
        self.mc.setBlocks(x + 3, y - 5, z + 3, x + 11, y - 5, z + 11, self.lighting_options[0])
        self.mc.setBlocks(x + 2, y, z + 2, x + 12, y, z + 12, self.slab)
        self.mc.setBlocks(x + 3, y, z + 3, x + 11, y, z + 11, self.air)
        # placement of lilypads
        for i in range(6):
            placement_x, placement_z = self.random_placement(4, 11)
            self.mc.setBlocks(x + placement_x, y, z + placement_z, x + placement_x, y, z + placement_z, self.lilypad)
    

    def build_pond(self, x, y, z):  # combines functions and makes whole structure
        self.build_foundation(x, y, z)
        self.fill_pond(x, y, z)
        
        self.build_tree(x, y, z)

pond = ParkPond()
x, y, z = pond._player_position()
pond.build_pond(x, y, z)
