from mcpi import vec3 as v
#from tradies.tradie import Tradie     # Remove comment when not running tests
from tradie import Tradie       # Comment out when not running tests

class FloorInstaller(Tradie):
    trade = 'flooring'
    floors = []
    # External calls
    def build_component(self, floors, mc):
        #for floor in floors:
            self.floors.append(floor)
            self._build_floor(self.floors[-1], mc)
    # Internal Methods
    def _build_floor(self, floor, mc):
        s = floor.floor_v3['start']
        e = floor.floor_v3['end']
        mc.setBlocks(s.x, s.y + floor.elevation - 1, s.z, e.x, e.y + floor.elevation - 1, e.z, floor.floor_block)
        pass

class Freddie(FloorInstaller):
    name = 'Freddie'
    pass


# TESTING

if __name__ == '__main__':

    import sys
    sys.path.append('../property')
    from components import floor as f
    from mcpi import minecraft
    mc = minecraft.Minecraft.create()
    v3 = mc.player.getPos()
    floor = f.Floor(v3)
    floor_guy = Freddie()
    floor_guy.build_component(floor, mc)
    print(dir())