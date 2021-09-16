from mcpi import vec3 as v
from tradies.tradie import Tradie     # Remove comment when not running tests
# from tradie import Tradie       # Comment out when not running tests

class Mason(Tradie):
    trade = 'masonry'
    walls = []
    def __init__(self):
        pass
    # External calls
    def build_component(self, wall, mc):
        self.walls.append(wall)
        self.__build_roof(self.walls[-1], mc)
    # Internal Methods
    def __build_roof(self, wall, mc):
        mc.setBlocks(wall.wall_v3['start'], wall.wall_v3['end'], wall.wall_block)
       
        mc.setBlocks(wall.wall_v3['start'].x + 1, 
        wall.wall_v3['start'].y,
        wall.wall_v3['start'].z + 1,
        wall.wall_v3['end'].x - 1,
        wall.wall_v3['end'].y + 5,
        wall.wall_v3['end'].z - 1, 0)



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
