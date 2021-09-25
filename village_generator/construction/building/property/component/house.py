from components.component import Component
from mcpi import vec3 as v


class House(Component):
    type = 'house'
    components = []
    position = None
    layout = None
    orientation = None
    theme = None
    total_levels = None
    floor_elevations = []
    property_v3: v.Vec3 = None
    house_v3: v.Vec3 = None
    end_v3: v.Vec3 = None

    def __init__(self, components=[]):
        self.components = components
