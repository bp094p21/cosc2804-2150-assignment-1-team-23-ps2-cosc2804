from mcpi import vec3 as v
from tradies.tradie import Tradie     # Remove comment when not running tests
# from tradie import Tradie       # Comment out when not running tests


class PoolInstaller(Tradie):
    trade = 'pool installations'
    pools = []
    def __init__(self):
        pass
    def build_component(self, pool, mc):
        self.pools.append(pool)
        self._build_pool(self.pools[-1], mc)
    def _build_pool(self, pool, mc):
        self._line_pool(pool.line_v3, pool.line_depth, pool.line_x, pool.line_y, pool.line_z, pool.line_block,  mc)
        self._make_entry()
        self._fill_pool(pool.fill_v3, pool.fill_block, mc)
        pass
    def _line_pool(self, v3, line_depth, x, y, z, block, mc):
        root = v3['start']
        start = v.Vec3(root.x + line_depth, root.y - y, root.z + line_depth)
        end = v.Vec3(root.x + (x - 1), root.y - y, root.z + (z - 1))
        mc.setBlocks(start, end, block)
        start = v3['start']
        end = v.Vec3(start.x + x - 1, start.y - y, start.z)
        mc.setBlocks(start, end, block)
        start = v.Vec3(end.x + 1, end.y, end.z)
        end = v.Vec3(start.x, start.y + y, start.z + z - 1)
        mc.setBlocks(start, end, block)
        start = v.Vec3(end.x, end.y, end.z + 1)
        end = v.Vec3(start.x - (x - 1), start.y - y, start.z)
        mc.setBlocks(start, end, block)
        start = v.Vec3(end.x - 1, end.y, end.z)
        end = v.Vec3(start.x, start.y + y, start.z - (z - 1))
        mc.setBlocks(start, end, block)
        pass
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