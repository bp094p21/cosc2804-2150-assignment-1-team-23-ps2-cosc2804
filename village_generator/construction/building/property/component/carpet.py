from components.component import Component
import block as b
from mcpi import vec3 as v


class Carpet(Component):
    # Class attributes
    type = 'carpet'
    block = None
    v3 = {
        'start': None,
        'end': None
    }

    def __init__(self, block=b.CARPET):
        self.block = block
