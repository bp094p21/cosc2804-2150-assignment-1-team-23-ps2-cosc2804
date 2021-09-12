from mcpi import minecraft
class Component:
    block_list = []
    x_len = None
    y_len = None
    z_len = None
    component_pos = (None, None, None)
    mc = None
    type = None
    def __init__(self):
        pass
    def build(self, component_pos, mc):
        self.component_pos = component_pos
        x = 0
        y = 0
        z = 0
        i = 0
        for block in self.block_list:
            mc.setBlock(self.component_pos[0] + x, self.component_pos[1] + y, self.component_pos[2] + z, block)
            i += 1
            z += 1
            if i % self.z_len == 0:
                z = 0
                x += 1
            if i % (self.x_len ** 2) == 0:
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