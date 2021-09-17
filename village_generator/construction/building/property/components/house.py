from components.component import Component
import block as b
from mcpi import vec3 as v

class House:
    components = {}
    position = None
    orientation = None
    theme = None
    total_levels = None
    floor_elevations = []
    house_v3: v.Vec3 = None
    z_len: int = None
    x_len: int = None
    def __init__(self, components={}):
        self.components = components
