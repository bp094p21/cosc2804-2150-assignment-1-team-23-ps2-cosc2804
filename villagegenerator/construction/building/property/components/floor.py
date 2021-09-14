from mcpi import vec3 as v
from mcpi import minecraft as m

import sys
sys.path.append('../property')

import block as b
from component import Component

class Floor(Component):
    # __init__ inputs
    mc: m.Minecraft = None
    root_v3: v.Vec3 = None
    height:int = None
    # Class attributes
    type: str = 'floor'
    # Instance attributes
    floor_block: b.Block = None
    height: int = None
    z_len: int = None
    x_len: int = None
    floor_v3: dict = {
        'start': None,
        'end': None
    }
    def __init__(self, floor_block=b.TERRACOTTA, level='ground', name='main'):
        self.floor_block = floor_block
        self.level = level
        self.name = name
        pass
    def build(self, mc: m.Minecraft, root_v3: v.Vec3, height: int, z_len: int, x_len):
        self.mc = mc
        self.root_v3 = root_v3
        self.height = height
        self.z_len = z_len
        self.x_len = x_len
        self._set_floor_v3()
        self._build_floor(self.floor_v3['start'], self.floor_v3['end'], self.floor_block)
        pass
    def _set_floor_v3(self):
        self.floor_v3['start'] = self.root_v3
        v3 = self.floor_v3['start']
        end_v3 = v.Vec3(v3.x + (self.x_len - 1), v3.y + (self.height -1), v3.z + (self.z_len - 1))
        self.floor_v3['end'] = end_v3
    def _build_floor(self, start_v3, end_v3, block):
        self.mc.setBlocks(start_v3, end_v3, block)
        pass

# TESTING
if __name__ == '__main__':
    mc = m.Minecraft.create()
    player_v3 = mc.player.getPos()
    floor = Floor(floor_block=b.TERRACOTTA, level='ground', name='main')
    floor.build(mc, root_v3=player_v3, height=1, z_len=8, x_len=6)
    pass