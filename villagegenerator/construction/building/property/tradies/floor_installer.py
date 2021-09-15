from mcpi import vec3 as v
from tradie import Tradie

class FloorInstaller(Tradie):
    trade = 'flooring'
    floors = []
    def __init__(self):
        pass
    def assign_floor(self, floor, mc):
        self.floors.append(floor)
        self._build_floor(self.floors[-1], mc)
    def _build_floor(self, floor, mc):
        mc.setBlocks(floor.floor_v3['start'], floor.floor_v3['end'], floor.floor_block)
        pass

class Freddie(FloorInstaller):
    name = 'Freddie'
    pass


# TESTING

if __name__ == '__main__':

    import sys
    sys.path.append('../property')
    from components import floor as f
    from tradies import floor_installer as fi
    from mcpi import minecraft
    mc = minecraft.Minecraft.create()
    v3 = mc.player.getPos()
    floor = f.Floor(v3)
    floor_guy = fi.Freddie()
    floor_guy.assign_floor(floor, mc)
    print(dir())