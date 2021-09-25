from mcpi import minecraft


class Tradie:
    trade = 'general'
    name = None
    emoji = '🦺'
    msg = 'gday'

    def __init__(self):
        print(f"{self.emoji} Tradie created.\n")
        if self.name:
            print(f"tradie.name: {self.name}\n")

    # All Tradie sub-classes should have same build_component signature. They can have different code running inside
    # it based on what they're building.
    def build_component(self, component, mc: minecraft.Minecraft):
        self._fill(component.start_v3, component.end_v3, component.block, mc)

    def _air(self, start_v3, end_v3, mc):
        mc.setBlocks(start_v3, end_v3, 0)

    def _one_block(self, v3, block, mc):
        mc.setBlock(v3, block)

    def _wrap(self, start_v3, end_v3, block, mc):
        mc.setBlocks(start_v3, end_v3.x, end_v3.y, start_v3.z, block)
        mc.setBlocks(start_v3, start_v3.x, end_v3.y, end_v3.z, block)
        mc.setBlocks(start_v3.x, start_v3.y, end_v3.z, end_v3, block)
        mc.setBlocks(end_v3.x, start_v3.y, start_v3.z, end_v3, block)

    def _fill(self, start_v3, end_v3, block, mc):
        mc.setBlocks(start_v3, end_v3, block)
    # TODO: Have basic build functions that can be used by multiple tradie below
    # IGNORE _build_cuboid for now.
    # def _build_cuboid(self, corner_pos = 0):
    #     print(f"Building with corner pos {corner_pos}")
    #     inc_mid = 1
    #     inc_y = 1
    #     inc_inner = 1
    #     x_len = self.x_len
    #     y_len = self.y_len
    #     z_len = self.z_len
    #     x_pos = self.x_pos
    #     y_pos = self.y_pos
    #     z_pos = self.z_pos
    #     corner_pos = self.corner_pos
    #     if corner_pos == 0:
    #         # Build normally. Just pass
    #         pass
    #     elif corner_pos == 1:
    #         # TODO: Build from top left corner. Meaning, original x and z values will be swapped. x will be inner most loop and increment by +1, z will be middle nested and increment by -1
    #         x_len, z_len = z_len, x_len
    #         inc_mid = -1
    #         pass
    #     elif corner_pos == 2:
    #         # TODO: Build from top right corner. Meaning, z will increment by - 1, x will increment by -1.
    #         inc_inner = -1
    #         inc_mid = -1
    #         pass
    #     elif corner_pos == 3:
    #         # TODO: Build from bottom right corner. Meaning, original x and z values will be swapped. x will be inner most loop and increment by -1, z will be middle nested loop and increment by +1
    #         x_len, z_len = z_len, x_len
    #         inc_inner = -1
    #         pass
    #     x = 0
    #     y = 0
    #     z = 0
    #     i = 0
    #     for block in self.block_list:
    #         self.mc.setBlock(x_pos + x, y_pos + y, z_pos + z, block)
    #         z += inc_inner
    #         i += 1
    #         if i % z_len == 0:
    #             z = 0
    #             x += inc_mid
    #         if i % (self.z_len * self.x_len) == 0:
    #             x = 0
    #             y += inc_y
