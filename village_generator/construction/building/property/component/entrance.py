from .component import Component
from construction.building.property.block import Block, STONE, AIR, TERRACOTTA


class Entrance(Component):
    # Class attributes
    type: str = 'entrance'
    length: int = 15
    # Instance attributes
    root_v3 = None
    orientation: int = None
    height: int = None
    fence_block: Block = None
    gate_block: Block = None

    def __repr__(self):
        return f"🖨  Printing object.__repr__:\n\n{type(self)}\nlength: {self.length},\nroot_v3: {self.root_v3}," \
               f"\norientation: {self.orientation},\nheight: {self.height},\nfence_block: {self.fence_block}," \
               f"\ngate_block: {self.gate_block}\n"

    def __init__(self, root_v3=None, orientation=0, height=2, fence_block=STONE, gate_block=AIR):
        self.root_v3 = root_v3
        self.orientation = orientation
        self.height = height
        self.fence_block = fence_block
        self.gate_block = gate_block


# TESTING
if __name__ == '__main__':
    from mcpi import minecraft as m

    mc = m.Minecraft.create()
    player_v3 = mc.player.getPos()
    entrance = Entrance(root_v3=player_v3, fence_block=TERRACOTTA, gate_block=AIR)
    pass
