from .component import Component
from construction.building.property.block import Block, STAIRS_WOOD
from mcpi import vec3 as v


class Roof(Component):
    # Class attributes
    type = 'roof'
    # Instance attributes
    stair_block: Block = None
    slab_block: Block = None
    cube_block: Block = None
    elevation: int = None
    roof_v3 = {
        'start': None,
        'end': None
    }

    def __init__(self, start_v3: v.Vec3, end_v3: v.Vec3, stair_block, slab_block, cube_block):
        self.roof_v3['start'] = start_v3
        self.roof_v3['end'] = end_v3
        self.stair_block = stair_block
        self.slab_block = slab_block
        self.cube_block = cube_block


if __name__ == '__main__':
    from mcpi import minecraft as m

    mc = m.Minecraft.create()
    player_v3 = mc.player.getPos()
    roof = Roof(roof_block=STAIRS_WOOD)
