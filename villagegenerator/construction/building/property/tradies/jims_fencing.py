# Jim's Fencing specialises in fencing
from tradies.tradie import Tradie
from mcpi import minecraft as m
from mcpi import vec3 as v

class JimsFencing(Tradie):
    trade = 'fencing'
    def __init__(self):
        pass
    def build_component(self, mc: m.Minecraft, root_v3: v.Vec3, orientation: int, height: int):
        self.mc = mc
        self.root_v3 = root_v3
        self.orientation = orientation
        self.height = height
        self._set_fence_v3()
        self._set_gate_v3()
        self._build_fence(self.fence_v3['start'], self.fence_v3['end'], self.fence_block)
        self._build_gate(self.gate_v3['start'], self.gate_v3['end'], self.gate_block)
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