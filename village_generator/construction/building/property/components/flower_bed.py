from components.component import Component
import block as b

class FlowerBed(Component):
    # Class attributes
    type: str = 'flower_bed'
    # Instance attributes
    v3 = None
    x_len: int = None
    z_len: int = None
    def __repr__(self):
        return f"🖨  Printing object.__repr__:\n\n{type(self)}\nv3: {self.v3},\nx_len: {self.x_len},\nz_len: {self.z_len}\n"
    def __init__(self, v3, x_len, z_len):
        self.v3 = v3
        self.x_len = x_len
        self.z_len = z_len

# TESTING
if __name__ == '__main__':
    from mcpi import minecraft as m
    mc = m.Minecraft.create()
    player_v3 = mc.player.getPos()
    orientation = 0
	