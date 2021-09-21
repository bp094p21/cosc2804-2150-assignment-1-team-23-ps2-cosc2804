from components.component import Component
import block as b
from mcpi import vec3 as v

class Window(Component):
    # Class attributes
    type = 'window'
    # Instance attributes
    v3: v.Vec3 = None
    block: b.Block = None
    def __init__(self, v3: v.Vec3, block=b.GLASS_PANE):
        self.v3 = v3
        self.block = block


# TESTING
if __name__ == '__main__':
    from mcpi import minecraft as m
    mc = m.Minecraft.create()
    player_v3 = mc.player.getPos()
