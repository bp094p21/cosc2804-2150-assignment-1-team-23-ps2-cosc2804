from mcpi import vec3
from mcpi import minecraft

from util import printer

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
    # Initialize print utilities
    p = printer.Printer('Component not yet instantiated')
    p.location_str = "Location not set"
    # Public methods
    def __init__(self, type=None):
        self.type = type
        self.p.status = f"Component instantiated with type: {self.type}"
        self.p.print_status()
    def build(self, location_vec3: vec3.Vec3, mc: minecraft.Minecraft, corner_pos = 0):
        self.x_pos, self.y_pos, self.z_pos = location_vec3
        self.mc = mc
        self.corner_pos = corner_pos
        self.p.location_str = f"\nx: {self.x_pos}\ny: {self.y_pos}\nz: {self.z_pos}"
        self.p.status = f"Commenced building {self.type} at:\n{self.p.location_str}\n"
        self.p.print_status()
        self._build_cuboid(self.corner_pos)
    def _build_cuboid(self, corner_pos = 0):
        print(f"Building with corner pos {corner_pos}")
        inc_mid = 1
        inc_y = 1
        inc_inner = 1
        x_len = self.x_len
        y_len = self.y_len
        z_len = self.z_len
        x_pos = self.x_pos
        y_pos = self.y_pos
        z_pos = self.z_pos
        corner_pos = self.corner_pos
        if corner_pos == 0:
            # Build normally. Just pass
            pass
        elif corner_pos == 1:
            # TODO: Build from top left corner. Meaning, original x and z values will be swapped. x will be inner most loop and increment by +1, z will be middle nested and increment by -1
            x_len, z_len = z_len, x_len
            inc_mid = -1
            pass
        elif corner_pos == 2:
            # TODO: Build from top right corner. Meaning, z will increment by - 1, x will increment by -1.
            inc_inner = -1
            inc_mid = -1
            pass
        elif corner_pos == 3:
            # TODO: Build from bottom right corner. Meaning, original x and z values will be swapped. x will be inner most loop and increment by -1, z will be middle nested loop and increment by +1
            x_len, z_len = z_len, x_len
            inc_inner = -1
            pass
        x = 0
        y = 0
        z = 0
        i = 0
        for block in self.block_list:
            self.mc.setBlock(x_pos + x, y_pos + y, z_pos + z, block)
            z += inc_inner
            i += 1
            if i % z_len == 0:
                z = 0
                x += inc_mid
            if i % (self.z_len * self.x_len) == 0:
                x = 0
                y += inc_y



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