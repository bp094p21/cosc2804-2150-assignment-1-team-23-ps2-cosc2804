from mcpi import vec3 as v
if __name__ == '__main__':
    from tradie import Tradie      
else:
    from tradies.tradie import Tradie


class PoolInstaller(Tradie):
    trade = 'pool installations'
    pools = []
    def build_component(self, pool, mc):
        self.pools.append(pool)
        self._build_pool(self.pools[-1], mc)
    def _build_pool(self, pool, mc):
        self._line_pool(pool.line_v3, pool.line_block, mc)
        self._air_fill(pool.fill_v3, pool.line_raise, mc)
        self._make_entry()
        self._fill_pool(pool.fill_v3, pool.fill_block, mc)
    def _line_pool(self, v3, block, mc):
        mc.setBlocks(v3['start'], v3['end'], block)
    def _air_fill(self, v3, line_raise, mc):
        x, y, z = v3['start']
        y += line_raise
        x2, y2, z2 = v3['end']
        mc.setBlocks(x,y,z,x2,y2,z2,0)
    def _make_entry(self):
        # TODO: make entry into pool using slabs add adding more lining on entrance edge
        pass
    def _fill_pool(self, v3, block, mc):
        mc.setBlocks(v3['start'], v3['end'], block)
        pass

class Paul(PoolInstaller):
    name = 'Paul'
    pass


# TESTING

if __name__ == '__main__':

    import sys
    sys.path.append('../property')
    from components import pool as p
    from tradies import pool_installer as pi
    from mcpi import minecraft
    mc = minecraft.Minecraft.create()
    v3 = mc.player.getPos()
    pool = p.Pool(v3)
    pool_guy = pi.Paul()
    pool_guy.build_component(pool, mc)
    print(dir())