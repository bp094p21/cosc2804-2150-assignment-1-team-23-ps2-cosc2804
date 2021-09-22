from components.component import Component
import block as b
from mcpi import vec3 as v

class Steps(Component):
    type = 'steps'
    def __init__(self, v3, block):
        self.v3 = v3
        self.block = block
    pass