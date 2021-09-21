from mcpi import minecraft as m

if __name__ == '__main__':
    from tradie import Tradie      
else:
    from tradies.tradie import Tradie

class Carpenter(Tradie):
    trade = 'carpentry'
    def build_component(self, component, mc):
        if component.type == 'stairs':
            self._build_stairs(component, mc)
            self._make_headroom(component, mc)
        elif component.type == 'door':
            self._set_door(component, mc)
        pass
    def _set_door(self, door, mc):
        x, y, z = door.root_v3
        self._air((x, y, z), (x, y + 1, z), mc)
        self._one_block(door.root_v3, door.door_block, mc)
        # self._one_block((x, y + 1, z), door.door_block, mc)
        pass
    def _make_headroom(self, stairs, mc):
        x, y, z = stairs.start_v3
    def _build_stairs(self, stairs, mc):
        x,y,z = stairs.start_v3
        block_up = stairs.block_up
        block_down = stairs.block_down
        if stairs.orientation == 0:
            for i in range(3):
                mc.setBlock(x, y + i, z + i, block_up)
                mc.setBlock(x, y + i, z + i + 1, block_down)
            mc.setBlock(x, y + i + 1, z + i + 1, block_up)
            y += 3
            air_block = 0
            for i in range(3):
                mc.setBlock(x, y, z + i, air_block)
        if stairs.orientation == 1:
            for i in range(3):
                mc.setBlock(x - i, y + i, z, block_up)
                mc.setBlock(x - i - 1, y + i, z, block_down)
            mc.setBlock(x - i - 1, y + i + 1, z, block_up)
            y += 3
            air_block = 0
            for i in range(3):
                mc.setBlock(x - i, y, z, air_block)
        if stairs.orientation == 2:
            for i in range(3):
                mc.setBlock(x, y + i, z - i, block_up)
                mc.setBlock(x, y + i, z - i - 1, block_down)
            mc.setBlock(x, y + i + 1, z - i - 1, block_up)
            y += 3
            air_block = 0
            for i in range(3):
                mc.setBlock(x, y, z - i, air_block)
        if stairs.orientation == 3:
            for i in range(3):
                mc.setBlock(x + i, y + i, z, block_up)
                mc.setBlock(x + i + 1, y + i, z, block_down)
            mc.setBlock(x + i + 1, y + i + 1, z, block_up)
            y += 3
            air_block = 0
            for i in range(3):
                mc.setBlock(x + i, y, z, air_block)

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