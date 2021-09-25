from .component import Component


class FlowerBed(Component):
    # Class attributes
    type: str = 'flower_bed'
    # Instance attributes
    v3 = None

    def __repr__(self):
        return f"🖨  Printing object.__repr__:\n\n{type(self)}\nv3: {self.v3}\n"

    def __init__(self, v3):
        self.v3 = v3


# TESTING
if __name__ == '__main__':
    from mcpi import minecraft as m

    mc = m.Minecraft.create()
    player_v3 = mc.player.getPos()
    orientation = 0
