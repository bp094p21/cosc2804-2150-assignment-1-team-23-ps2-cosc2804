from .component import Component
from construction.building.property.block import Block, STONE
from mcpi import vec3 as v


class Boundary(Component):
    # Class attributes
    type = 'boundary'
    length: int = 15
    # Instance attributes
    block: Block = None

    ## Height and stepping frequency dependent on Entrance
    def __init__(self, start_v3, end_v3, block=STONE):
        self.block = block
        self.start_v3 = start_v3
        self.end_v3 = end_v3

    def __repr__(self):
        return f"🖨  Printing object.__repr__:\n\n{type(self)}\n\length: {self.length},\nblock: {self.block}\n"
