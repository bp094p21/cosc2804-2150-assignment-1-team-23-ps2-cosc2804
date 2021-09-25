from .component import Component
from construction.building.property.block import CARPET
from mcpi import vec3 as v


class Carpet(Component):
    # Class attributes
    type = 'carpet'
    block = None
    v3 = {
        'start': None,
        'end': None
    }

    def __init__(self, block=CARPET):
        self.block = block
