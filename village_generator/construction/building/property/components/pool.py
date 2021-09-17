from components.component import Component
import block as b
from mcpi import vec3 as v

class Pool(Component):
    # Class attributes
    type = 'pool'
    pool_depth = None
    line_block: b.Block = None
    fill_block: b.Block = None
    line_v3 = {
        'start': None,
        'end': None
    }
    line_z: int = None
    line_x: int = None
    line_y: int = None
    fill_v3 = {
        'start': None,
        'end': None
    }
    def __repr__(self):
        return f"🖨  Printing object.__repr__:\n\n{type(self)}\npool_depth: {self.pool_depth},\nline_block: {self.line_block},\nfill_block: {self.fill_block},\nline_v3 start: {self.line_v3['start']},\nline_v3 end: {self.line_v3['end']},\nfill_v3 start: {self.fill_v3['start']}\nfill_v3 end: {self.fill_v3['end']}\n"
    def __init__(self, v3: v.Vec3, z_len=6, x_len=4, orientation=0, line_block=b.SANDSTONE, fill_block=b.WATER, pool_depth=2, line_raise=1, line_depth=1):
        self.line_v3['start'] = v.Vec3(v3.x, v3.y + (line_raise - 1), v3.z)
        self.line_v3['end'] = v.Vec3(v3.x + (x_len - 1), v3.y - (pool_depth + 1), v3.z + (z_len - 1))
        self.line_z = z_len - 1
        self.line_x = x_len - 1
        self.line_y = pool_depth + line_raise
        self.line_depth = line_depth
        self.fill_v3['start'] = v.Vec3(v3.x + line_depth, v3.y - 1, v3.z + line_depth)
        self.fill_v3['end'] = v.Vec3(v3.x + (x_len - 1 - line_depth), v3.y - 1 - (pool_depth - 1), v3.z + z_len - 1 - line_depth)
        self.orientation = orientation
        self.line_block = line_block
        self.fill_block = fill_block
        pass

# TESTING
if __name__ == '__main__':
    from mcpi import minecraft
    mc = minecraft.Minecraft.create()
    v3 = mc.player.getPos()
    block = b.STONE
    pool = Pool(v3, line_block=block)
    print(pool.line_block)

