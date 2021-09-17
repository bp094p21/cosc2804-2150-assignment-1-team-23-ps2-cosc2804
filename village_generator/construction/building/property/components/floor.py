from mcpi import vec3 as v
import block as b
from components.component import Component

class Floor(Component):
    # Class attributes
    type = 'floor'
    # Instance attributes
    root_v3: v.Vec3 = None
    floor_block: b.Block = None
    level: int = None
    elevation: int = None
    z_len: int = None
    x_len: int = None
    floor_v3 = {
        'start': None,
        'end': None
    }
    def __init__(self, root_v3: v.Vec3, floor_block=b.TERRACOTTA, level=0, elevation = 0, z_len=7, x_len=5, y_len=1):
        self.root_v3 = root_v3
        self.floor_block = floor_block
        self.level = level
        self.elevation = elevation
        self.z_len = z_len
        self.x_len = x_len
        self.y_len = y_len
        self.floor_v3['start'] = v.Vec3(self.root_v3.x, self.root_v3.y, self.root_v3.z)
        v3 = self.floor_v3['start']
        end_v3 = v.Vec3(v3.x + (self.x_len - 1), v3.y + (self.y_len - 1), v3.z + (self.z_len - 1))
        self.floor_v3['end'] = end_v3
    def __repr__(self):
        return f"🖨  Printing object.__repr__:\n\n{type(self)}\nfloor_v3 start: {self.floor_v3['start']},\nfloor_v3 end: {self.floor_v3['end']},\nlevel: {self.level},\nelevation : {self.elevation},\nz_len: {self.z_len},\ny_len start: {self.y_len}\nfloor_block: {self.floor_block}"

# TESTING
if __name__ == '__main__':
    from mcpi import minecraft as m
    mc = m.Minecraft.create()
    player_v3 = mc.player.getPos()
    floor = Floor(floor_block=b.TERRACOTTA, level='ground', name='main')