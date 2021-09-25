from mcpi import vec3 as v

from .tradie import Tradie


class Mason(Tradie):
    trade = 'masonry'
    walls = []
    wall_wraps = []

    def __init__(self):
        pass

    # External calls
    def build_component(self, component, mc):
        if component.type == 'wall':
            self.walls.append(component)
            self._build_wall(component, mc)
        elif component.type == 'wall_wrap':
            self.wall_wraps.append(component)
            self._build_wall_wrap(component, mc)

    # Internal Methods
    def _build_wall(self, wall, mc):
        self._fill(wall.start_v3, wall.end_v3, wall.wall_block, mc)

    def _build_wall_wrap(self, wall_wrap, mc):
        mc.setBlocks(wall_wrap.start_v3, wall_wrap.end_v3.x, wall_wrap.end_v3.y, wall_wrap.start_v3.z,
                     wall_wrap.wall_block)
        mc.setBlocks(wall_wrap.start_v3, wall_wrap.start_v3.x, wall_wrap.end_v3.y, wall_wrap.end_v3.z,
                     wall_wrap.wall_block)
        mc.setBlocks(wall_wrap.start_v3.x, wall_wrap.start_v3.y, wall_wrap.end_v3.z, wall_wrap.end_v3,
                     wall_wrap.wall_block)
        mc.setBlocks(wall_wrap.end_v3.x, wall_wrap.start_v3.y, wall_wrap.start_v3.z, wall_wrap.end_v3,
                     wall_wrap.wall_block)


class BigBloke(Mason):
    name = 'BigBloke'


# TESTING

if __name__ == '__main__':
    import sys

    sys.path.append('../property')
    from components import wall as w
    import block as b
    from mcpi import minecraft

    mc = minecraft.Minecraft.create()
    start_v3 = mc.player.getPos()
    end_v3 = v.Vec3(start_v3.x + 3, start_v3.y + 2, start_v3.z)
    wall_block = b.STONE_BRICK
    wall = w.Wall(start_v3, end_v3, wall_block)
    wall_guy = BigBloke()
    wall_guy.build_component(wall, mc)
    print(dir())
