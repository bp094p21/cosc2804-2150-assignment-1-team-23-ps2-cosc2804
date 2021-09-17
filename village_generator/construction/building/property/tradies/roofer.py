from mcpi import vec3 as v
#from tradies.tradie import Tradie
from tradie import Tradie

class Roofer(Tradie):
    trade = 'roofing'
    roofs = []
    def build_component(self, roof, mc):
        self.roofs.append(roof)
        self._build_roof(self.roofs[-1], mc)
    def _build_roof(self, roof, mc):
        x_difference = int(roof.roof_v3['end'].x - roof.roof_v3['start'].x)
        z_difference = int(roof.roof_v3['end'].z - roof.roof_v3['start'].z)
        abs(x_difference)
        abs(z_difference)
        for i in range(x_difference + 1):
            move_up_x = roof.roof_v3['start'].x + i
            if z_difference % 2 == 0:
                for j in range(int(z_difference / 2) + 1):
                    mc.setBlock(move_up_x, roof.roof_v3['start'].y - 1 + j, roof.roof_v3['start'].z - 1 + j, 53, 2)
                    mc.setBlock(move_up_x, roof.roof_v3['start'].y - 1 + j, roof.roof_v3['start'].z + 1 + z_difference - j, 53, 3)
                    mc.setBlock(move_up_x, roof.roof_v3['start'].y + (z_difference / 2), roof.roof_v3['start'].z + (z_difference / 2), 44, 2)
                    mc.setBlocks(roof.roof_v3['start'].x, roof.roof_v3['start'].y - 1 + j, roof.roof_v3['start'].z + j, roof.roof_v3['start'].x, roof.roof_v3['start'].y - 1 + j, roof.roof_v3['start'].z + z_difference - j, 5)   
                    mc.setBlocks(roof.roof_v3['end'].x, roof.roof_v3['start'].y - 1 + j, roof.roof_v3['start'].z + j, roof.roof_v3['end'].x, roof.roof_v3['start'].y - 1 + j, roof.roof_v3['start'].z + z_difference - j, 5)           
            else:
                pass


class Freddie(Roofer):
    name = 'Freddie'
    pass

if __name__ == '__main__':

    import sys
    sys.path.append('../property')
    from components import roof as r
    from mcpi import minecraft
    mc = minecraft.Minecraft.create()
    v3 = mc.player.getPos()
    roof = r.Roof(v3)
    roof_guy = Freddie()
    roof_guy.build_component(roof, mc)
    print(dir())

