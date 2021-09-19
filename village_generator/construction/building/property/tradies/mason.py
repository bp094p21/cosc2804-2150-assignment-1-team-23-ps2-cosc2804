from mcpi import vec3 as v
if __name__ == '__main__':
    from tradie import Tradie      
else:
    from tradies.tradie import Tradie

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
        elif component. type == 'wall_wrap':
            self.wall_wraps.append(component)
            self._build_wall_wrap(component, mc)
    # Internal Methods
    def _build_wall(self, wall, mc):
        pass
    def _build_wall_wrap(self, wall_wrap, mc):
        mc.setBlocks(wall_wrap.start_v3, wall_wrap.end_v3.x, wall_wrap.end_v3.y, wall_wrap.start_v3.z, wall_wrap.wall_block)
        mc.setBlocks(wall_wrap.start_v3, wall_wrap.start_v3.x, wall_wrap.end_v3.y, wall_wrap.end_v3.z, wall_wrap.wall_block)
        mc.setBlocks(wall_wrap.start_v3.x, wall_wrap.start_v3.y, wall_wrap.end_v3.z, wall_wrap.end_v3, wall_wrap.wall_block)
        mc.setBlocks(wall_wrap.end_v3.x, wall_wrap.start_v3.y, wall_wrap.start_v3.z, wall_wrap.end_v3, wall_wrap.wall_block)



class BigBloke(Mason):
    name = 'BigBloke'

# TESTING

if __name__ == '__main__':

    import sys
    sys.path.append('../property')
    from components import wall as w
    from mcpi import minecraft
    mc = minecraft.Minecraft.create()
    v3 = mc.player.getPos()
    wall = w.Wall(v3)
    wall_guy = BigBloke()
    wall_guy.build_component(wall, mc)
    print(dir())
