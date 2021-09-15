from mcpi import vec3 as v
import property as p
class Designer:
    name = None
    properties = []
    def __init__(self):
        pass
    def get_specs(self, property):
        pass
    def _design_component(self, item):
        pass
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