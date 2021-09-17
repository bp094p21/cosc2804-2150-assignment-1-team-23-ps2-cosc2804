from components.component import Component
import block as b

class Entrance(Component):
    # Class attributes
    type: str = 'entrance'
    length: int = 15
    # Instance attributes
    root_v3 = None
    orientation: int = None
    height:int = None
    fence_block: b.Block = None
    gate_block: b.Block = None
    def __repr__(self):
        return f"🖨  Printing object.__repr__:\n\n{type(self)}\nlength: {self.length},\nroot_v3: {self.root_v3},\norientation: {self.orientation},\nheight: {self.height},\nfence_block: {self.fence_block},\ngate_block: {self.gate_block}\n"
    def __init__(self, root_v3=None, orientation=0, height=2, fence_block=b.STONE, gate_block=b.AIR):
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
    entrance = Entrance(root_v3=player_v3, fence_block=b.TERRACOTTA, gate_block=b.AIR)
    pass
	