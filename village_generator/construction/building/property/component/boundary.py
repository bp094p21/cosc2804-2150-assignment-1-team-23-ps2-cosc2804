from components.component import Component
import block as b
from mcpi import vec3 as v


class Boundary(Component):
    # Class attributes
    type = 'boundary'
    length: int = 15
    # Instance attributes
    block: b.Block = None

    ## Height and stepping frequency dependent on Entrance
    def __init__(self, block=b.STONE):
        self.block = block

    def __repr__(self):
        return f"🖨  Printing object.__repr__:\n\n{type(self)}\n\length: {self.length},\nblock: {self.block}\n"
