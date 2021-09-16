# Jim's Fencing specialises in fencing
from tradies.tradie import Tradie
from mcpi import minecraft as m
from mcpi import vec3 as v

class JimsFencing(Tradie):
    trade = 'fencing'
    def build_component(self, object, mc: m.Minecraft):
        self.mc = mc
        if object.type == 'entrance':
            fence_v3 = self._get_fence_v3(object)
            gate_v3 = self._get_gate_v3(object)
            self._build_fence(fence_v3['start'], fence_v3['end'], object.fence_block)
            self._build_gate(gate_v3['start'], gate_v3['end'], object.gate_block)
        elif object.type == 'boundary':
            self._build_boundary(object)
    def _get_fence_v3(self, object):
        start_v3 = object.root_v3
        fence_v3 = {
            'start': start_v3,
            'end': None
        }
        end_v3 = None
        if object.orientation == 0:
            end_v3 = v.Vec3(start_v3.x + object.length - 1, start_v3.y + object.height - 1, start_v3.z)
        elif object.orientation == 1:
            end_v3 = v.Vec3(start_v3.x, start_v3.y + object.height - 1, start_v3.z + object.length - 1)
        elif object.orientation == 2:
            end_v3 = v.Vec3(start_v3.x - (object.length - 1), start_v3.y + object.height - 1, start_v3.z)
        elif object.orientation == 3:
            end_v3 = v.Vec3(start_v3.x, start_v3.y + object.height - 1, start_v3.z - (object.length - 1))
        fence_v3['end'] = end_v3
        return fence_v3
    def _get_gate_v3(self, object):
        v3 = object.root_v3
        h = object.height
        start_v3 = None
        end_v3 = None
        if object.orientation == 0:
            start_v3 = v.Vec3(v3.x + (object.length // 2), v3.y, v3.z)
            end_v3 = v.Vec3(start_v3.x, start_v3.y + object.height - 1, start_v3.z)
        elif object.orientation == 1:
            start_v3 = v.Vec3(v3.x, v3.y, v3.z + (object.length // 2))
            end_v3 = v.Vec3(start_v3.x, start_v3.y + object.height - 1, start_v3.z)
        elif object.orientation == 2:
            start_v3 = v.Vec3(v3.x - (object.length // 2), v3.y, v3.z)
            end_v3 = v.Vec3(start_v3.x, start_v3.y + object.height - 1, start_v3.z)
        elif object.orientation == 3:
            start_v3 = v.Vec3(v3.x, v3.y, v3.z - (object.length // 2))
            end_v3 = v.Vec3(start_v3.x, start_v3.y + object.height - 1, start_v3.z)
        gate_v3 = {
            'start': start_v3,
            'end': end_v3
        }
        return gate_v3
    def _build_fence(self, start_v3, end_v3, block):
        self.mc.setBlocks(start_v3, end_v3, block)
        pass
    def _build_gate(self, start_v3, end_v3, block):
        self.mc.setBlocks(start_v3, end_v3, block)
    def _build_boundary(self, object):
        pass