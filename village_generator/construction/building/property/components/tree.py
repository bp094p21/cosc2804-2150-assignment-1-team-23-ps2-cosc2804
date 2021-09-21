from components.component import Component
import block as b

class Tree(Component):
    # Class attributes
    type: str = 'tree'
    # Instance attributes
    start_v3 = None
    end_v3: int = None
    trunk_block: b.Block = None
    leaves_block: b.Block = None
    def __repr__(self):
        return f"🖨  Printing object.__repr__:\n\n{type(self)}\start_v3: {self.start_v3},\nend_v3: {self.end_v3},\nblock: {self.block}\n"
    def __init__(self, start_v3, end_v3, trunk_block, leaves_block):
        self.start_v3 = start_v3
        self.end_v3 = end_v3
        self.trunk_block = trunk_block
        self.leaves_block = leaves_block

# TESTING
if __name__ == '__main__':
    from mcpi import minecraft as m
    mc = m.Minecraft.create()
    player_v3 = mc.player.getPos()
    # Assign objects to below 3 variables for testing
    end_v3 = None
    trunk_block = None
    leaves_block = None

    entrance = Tree(start_V3=player_v3, end_v3=player_v3, trunk_block=trunk_block, leaves_block=leaves_block)
	