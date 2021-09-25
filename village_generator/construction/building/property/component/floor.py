from mcpi import vec3 as v
from construction.building.property.block import TERRACOTTA, Block
from .component import Component


class Floor(Component):
    # Class attributes
    type = 'floor'
    # Instance attributes
    root_v3: v.Vec3 = None
    floor_block: Block = None
    floor_level: int = None
    elevation: int = None
    z_len: int = None
    x_len: int = None
    floor_v3 = {
        'start': None,
        'end': None
    }

    def __init__(self, root_v3: v.Vec3, end_v3, floor_block=TERRACOTTA, floor_level=0, elevation=0, z_len=7, x_len=5,
                 y_len=1):
        self.root_v3 = root_v3
        self.floor_block = floor_block
        self.floor_level = floor_level
        self.elevation = elevation
        self.z_len = z_len
        self.x_len = x_len
        self.y_len = y_len
        self.floor_v3['start'] = root_v3
        self.floor_v3['end'] = end_v3

    def __repr__(self):
        return f"🖨  Printing object.__repr__:\n\n{type(self)}\nfloor_v3 start: {self.floor_v3['start']}," \
               f"\nfloor_v3 end: {self.floor_v3['end']},\nfloor_level: {self.floor_level},\nelevation : {self.elevation}," \
               f"\nz_len: {self.z_len},\ny_len start: {self.y_len}\nfloor_block: {self.floor_block}"


# TESTING
if __name__ == '__main__':
    from mcpi import minecraft as m

    mc = m.Minecraft.create()
    player_v3 = mc.player.getPos()
    floor = Floor(floor_block=TERRACOTTA, level='ground', name='main')
