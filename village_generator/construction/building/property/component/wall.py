from .component import Component
from construction.building.property.block import Block, STONE_BRICK, WOOD_PLANKS
from mcpi import vec3 as v


class Wall(Component):
    # Class attributes
    type = 'wall'
    # Instance attributes
    wall_block: Block = None
    level: int = None
    name: str = None
    elevation: int = None

    def __init__(self, start_v3: v.Vec3, end_v3: v.Vec3, wall_block=STONE_BRICK, level=0, name=''):
        self.start_v3 = start_v3
        self.end_v3 = end_v3
        self.wall_block = wall_block
        self.level = level
        self.name = name


class WallWrap(Wall):
    type = 'wall_wrap'


# TESTING
if __name__ == '__main__':
    from mcpi import minecraft as m

    mc = m.Minecraft.create()
    player_v3 = mc.player.getPos()
    wall = Wall(wall_block=WOOD_PLANKS, level='ground', name='main')
