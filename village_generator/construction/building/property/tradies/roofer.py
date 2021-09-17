from mcpi import vec3 as v
from tradies.tradie import Tradie
# from tradie import Tradie

class Roofer(Tradie):
    trade = 'roofing'
    roofs = []
    def build_component(self, roof, mc):
        self.roofs.append(roof)
        self._build_roof(self.roofs[-1], mc)
    def _build_roof(self, roof, mc):
        for number in range(0, 3):
            mc.setBlocks(roof.roof_v3['start'].x+number, 
            roof.roof_v3['start'].y+number,
            roof.roof_v3['start'].z+number, 
            roof.roof_v3['end'].x-number, 
            roof.roof_v3['end'].y+number, 
            roof.roof_v3['end'].z-number,  
            roof.roof_block)

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

