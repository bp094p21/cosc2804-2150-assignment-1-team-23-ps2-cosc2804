from mcpi import vec3 as v
from mcpi import minecraft as m

import sys
sys.path.append('../property')

import block as b
from component import Component

class Entrance(Component):
    # __init__ inputs
    mc: m.Minecraft = None
    root_v3: v.Vec3 = None
    orientation: int = None
    height:int = None
    # Class attributes
    type: str = 'entrance'
    length: int = 15
    # Instance attributes
    fence_block: b.Block = None
    gate_block: b.Block = None
    fence_v3: dict = {
        'start': None,
        'end': None
    }
    gate_v3: dict = {
        'start': None,
        'end': None
    }
    def __init__(self, fence_block=b.STONE, gate_block=b.AIR):
        self.fence_block = fence_block
        self.gate_block = gate_block
        pass
    def build(self, mc: m.Minecraft, root_v3: v.Vec3, orientation: int, height: int):
        self.mc = mc
        self.root_v3 = root_v3
        self.orientation = orientation
        self.height = height
        self._set_fence_v3()
        self._set_gate_v3()
        self._build_fence(self.fence_v3['start'], self.fence_v3['end'], self.fence_block)
        self._build_gate(self.gate_v3['start'], self.gate_v3['end'], self.gate_block)
        pass
    def _set_fence_v3(self):
        self.fence_v3['start'] = self.root_v3
        v3 = self.fence_v3['start']
        end_v3 = None
        if self.orientation == 0:
            end_v3 = v.Vec3(v3.x + self.length - 1, v3.y + self.height - 1, v3.z)
        elif self.orientation == 1:
            end_v3 = v.Vec3(v3.x, v3.y + self.height - 1, v3.z + self.length - 1)
        elif self.orientation == 2:
            end_v3 = v.Vec3(v3.x - (self.length - 1), v3.y + self.height - 1, v3.z)
        elif self.orientation == 3:
            end_v3 = v.Vec3(v3.x, v3.y + self.height - 1, v3.z - (self.length - 1))
        self.fence_v3['end'] = end_v3
    def _set_gate_v3(self):
        v3 = self.fence_v3['start']
        h = self.height
        start_v3 = None
        end_v3 = None
        if self.orientation == 0:
            start_v3 = v.Vec3(v3.x + (self.length // 2), v3.y, v3.z)
            end_v3 = v.Vec3(start_v3.x, start_v3.y + self.height - 1, start_v3.z)
        elif self.orientation == 1:
            start_v3 = v.Vec3(v3.x, v3.y, v3.z + (self.length // 2))
            end_v3 = v.Vec3(start_v3.x, start_v3.y + self.height - 1, start_v3.z)
        elif self.orientation == 2:
            start_v3 = v.Vec3(v3.x - (self.length // 2), v3.y, v3.z)
            end_v3 = v.Vec3(start_v3.x, start_v3.y + self.height - 1, start_v3.z)
        elif self.orientation == 3:
            start_v3 = v.Vec3(v3.x, v3.y, v3.z - (self.length // 2))
            end_v3 = v.Vec3(start_v3.x, start_v3.y + self.height - 1, start_v3.z)
        self.gate_v3['start'] = start_v3
        self.gate_v3['end'] = end_v3
    def _build_fence(self, start_v3, end_v3, block):
        self.mc.setBlocks(start_v3, end_v3, block)
        pass
    def _build_gate(self, start_v3, end_v3, block):
        self.mc.setBlocks(start_v3, end_v3, block)
        pass

# TESTING
if __name__ == '__main__':
    mc = m.Minecraft.create()
    player_v3 = mc.player.getPos()
    entrance = Entrance(fence_block=b.TERRACOTTA, gate_block=b.AIR)
    entrance.build(mc, root_v3=player_v3, orientation=3, height=2)
    pass
	