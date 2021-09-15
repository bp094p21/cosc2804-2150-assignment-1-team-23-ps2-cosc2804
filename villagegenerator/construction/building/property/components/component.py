from mcpi import vec3 as v
import sys
sys.path.append('../property')

import block as b

class Component:
    type = None
    root_v3: v.Vec3 = None
    block: b.Block = None
    z_len = None
    x_len = None
    y_len = None
    block_list = None
    orientation = None
    is_built = False
    # Init
    def __init__(self, type, root_v3: v.Vec3, block=b.STONE, z_len=1, x_len=1, y_len=1, block_list=[], orientation=0):
        self.type = type
        self.root_v3 = root_v3
        self.block = block
        self.z_len = z_len
        self.x_len = x_len
        self.y_len = y_len
        self.block_list = block_list
        self.orientation = orientation
    def __repr__(self):
        return f"🖨  Printing object.__repr__:\n\n{type(self)}\ntype: {self.type},\nroot_v3: {self.root_v3},\nblock: \"{self.block}\",\nz_len: {self.z_len},\nx_len: {self.x_len},\ny_len: {self.y_len},\nblock_list: {self.block_list},\norientation: {self.orientation},\nis_built: {self.is_built}"

# TESTING
if __name__ == '__main__':
    from mcpi import minecraft
    mc = minecraft.Minecraft.create()
    v3 = mc.player.getPos()
    custom_component = Component('custom', v3)
    print(custom_component)
