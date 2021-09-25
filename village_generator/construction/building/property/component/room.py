from components.component import Component
import block as b
from mcpi import vec3 as v


class Room(Component):
    type = 'room'

    def __init__(self, start_v3: v.Vec3, end_v3: v.Vec3, wall_block=b.TERRACOTTA, level=0, elevation=0, z_len=7,
                 x_len=5, y_len=1):
        self.start_v3 = start_v3
        self.end_v3 = end_v3
        self.wall_block = wall_block
        self.level = level
        self.elevation = elevation
        self.z_len = z_len
        self.x_len = x_len
        self.y_len = y_len
