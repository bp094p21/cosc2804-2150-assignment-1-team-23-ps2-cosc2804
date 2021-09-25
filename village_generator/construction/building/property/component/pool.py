from components.component import Component
import block as b


class Pool(Component):
    # Class attributes
    type = 'pool'
    pool_depth = None
    line_raise = None
    line_block: b.Block = None
    fill_block: b.Block = None
    line_v3 = None
    fill_v3 = None
    fence_v3 = None

    def __repr__(self):
        return f"🖨  Printing object.__repr__:\n\n{type(self)}\npool_depth: {self.pool_depth}," \
               f"\nline_raise: {self.line_raise}\nline_block: {self.line_block},\nfill_block: {self.fill_block}," \
               f"\nline_v3 start: {self.line_v3['start']},\nline_v3 end: {self.line_v3['end']}," \
               f"\nfill_v3 start: {self.fill_v3['start']}\nfill_v3 end: {self.fill_v3['end']}\n"

    def __init__(self, line_v3, fill_v3, fence_v3, gate_v3, line_block=b.SANDSTONE, fill_block=b.WATER,
                 fence_block=b.FENCE_ACACIA, gate_block=b.FENCE_GATE_ACACIA, pool_depth=2, line_raise=1, line_depth=1):
        self.line_v3 = line_v3
        self.fill_v3 = fill_v3
        self.fence_v3 = fence_v3
        self.gate_v3 = gate_v3
        self.line_raise = line_raise
        self.line_depth = line_depth
        self.line_block = line_block
        self.fill_block = fill_block
        self.fence_block = fence_block
        self.gate_block = gate_block
        self.pool_depth = pool_depth


# TESTING
if __name__ == '__main__':
    from mcpi import minecraft

    mc = minecraft.Minecraft.create()
    v3 = mc.player.getPos()
    block = b.STONE
    pool = Pool(v3, line_block=block)
    print(pool.line_block)
