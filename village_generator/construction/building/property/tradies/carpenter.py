from mcpi import minecraft as m

if __name__ == '__main__':
    from tradie import Tradie      
else:
    from tradies.tradie import Tradie

class Carpenter(Tradie):
    trade = 'carpentry'
    def build_component(self, component, mc):
        self._build_stairs(component, mc)
        self._make_headroom(component, mc)
        pass
    def _make_headroom(self, stairs, mc):
        x, y, z = stairs.start_v3
        y += 3
        air_block = 0
        for i in range(4):
            mc.setBlock(x, y, z + i, air_block)

    def _build_stairs(self, stairs, mc):
        x,y,z = stairs.start_v3
        block_up = stairs.block_up
        block_down = stairs.block_down
        for i in range(3):
            mc.setBlock(x, y + i, z + i, block_up)
            mc.setBlock(x, y + i, z + i + 1, block_down)
        mc.setBlock(x, y + i + 1, z + i + 1, block_up)
        pass

if __name__ == '__main__':
    import sys
    sys.path.append('../property')
    from components import stairs as s
    import block as b
    from mcpi import minecraft
    mc = minecraft.Minecraft.create()
    mc = m.Minecraft.create()
    v3 = mc.player.getPos()
    x, y, z = v3
    block_up = b.OPTIONS['medi']['stairs']['basic'][0].withData(2)
    block_down = b.OPTIONS['medi']['stairs']['basic'][0].withData(7)
    stairs = s.Stairs(v3, block_up, block_down)
    print(type(stairs))
    carpenter = Carpenter()
    carpenter.build_component(stairs, mc)