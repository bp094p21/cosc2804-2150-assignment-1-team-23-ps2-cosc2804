
from construction.building.misc.misc import Misc
import construction.building.misc.block_list as b

class ParkPond(Misc):
    def __init__(self)->None:
        super().__init__()
        self.lilypad = 111
    
    def fill_pond(self, x, y, z):  # as name suggests, digs pond and fills it
        self.mc.setBlocks(x + 3, y - 1, z + 3, x + 11, y - 5, z + 11, b.MISC_BLOCKS[self.theme_string]['pond_liquid'])
        self.mc.setBlocks(x + 3, y - 5, z + 3, x + 11, y - 5, z + 11, b.MISC_BLOCKS[self.theme_string]['main_light_block'])
        self.mc.setBlocks(x + 2, y, z + 2, x + 12, y, z + 12, b.MISC_BLOCKS[self.theme_string]['main_slab'])
        self.mc.setBlocks(x + 3, y, z + 3, x + 11, y, z + 11, self.air)
        # placement of lilypads
        for i in range(6):
            placement_x, placement_z = self.random_placement(4, 11)
            self.mc.setBlocks(x + placement_x, y, z + placement_z, x + placement_x, y, z + placement_z, self.lilypad)
    

    def build(self, x, y, z):  # combines functions and makes whole structure
        self.build_foundation(x, y, z)
        self.fill_pond(x, y, z)
        
        self.build_tree(x, y, z)

# pond = ParkPond()
# x, y, z = pond._player_position()
# pond.build(x, y, z)
