from .component import Component


class Bed(Component):
    # Class attributes
    type: str = 'bed'
    # Instance attributes
    v3 = None
    block: int = None

    def __repr__(self):
        return f"🖨  Printing object.__repr__:\n\n{type(self)}\nv3: {self.v3},\nblock: {self.block}"

    def __init__(self, v3, block):
        self.v3 = v3
        self.block = block


# TESTING
if __name__ == '__main__':
    from mcpi import minecraft as m

    mc = m.Minecraft.create()
    player_v3 = mc.player.getPos()
    orientation = 0
