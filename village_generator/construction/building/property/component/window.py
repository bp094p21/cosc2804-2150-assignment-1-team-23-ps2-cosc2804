from .component import Component
from construction.building.property.block import Block, GLASS_PANE
from mcpi import vec3 as v


class Window(Component):
    # Class attributes
    type = 'window'
    # Instance attributes
    v3: v.Vec3 = None
    block: Block = None

    def __init__(self, v3: v.Vec3, block=GLASS_PANE):
        self.v3 = v3
        self.block = block


# TESTING
if __name__ == '__main__':
    from mcpi import minecraft as m

    mc = m.Minecraft.create()
    player_v3 = mc.player.getPos()
