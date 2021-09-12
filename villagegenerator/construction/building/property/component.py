from mcpi import vec3
from mcpi import minecraft
class Component:
    block_list = []
    x_len = None
    y_len = None
    z_len = None
    x_pos = None
    y_pos = None
    z_pos = None
    mc = None
    type = None
    def __init__(self, type=None):
        self.type = type
        pass
    def build(self, location_vec3: vec3.Vec3, mc: minecraft.Minecraft):
        self.x_pos, self.y_pos, self.z_pos = location_vec3
        x = 0
        y = 0
        z = 0
        i = 0
        for block in self.block_list:
            mc.setBlock(self.x_pos + x, self.y_pos + y, self.z_pos + z, block)
            i += 1
            z += 1
            if i % self.z_len == 0:
                z = 0
                x += 1
            if i % (self.z_len * self.x_len) == 0:
                x = 0
                y += 1
        pass

class Entrance(Component):
    designs = {
        'single_story': [],
        'double_story': [],
        'unit': [],
        'apartment': []
    }
    def __init__(self):
        self.type = 'entrance'
    pass