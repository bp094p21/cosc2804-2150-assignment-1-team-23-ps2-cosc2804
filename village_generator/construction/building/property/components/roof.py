from components.component import Component
import block as b
from mcpi import vec3 as v

class Roof(Component):
    # Class attributes
    type = 'roof'
    # Instance attributes
    root_v3: v.Vec3 = None
    roof_block: b.Block = None
    elevation: int = None
    z_len: int = None
    x_len: int = None
    roof_v3 = {
        'start': None,
        'end': None
    }
    def __init__(self, root_v3: v.Vec3, roof_block=b.STONE_BRICK, z_len=7, x_len=5, y_len=1):
        self.root_v3 = root_v3
        self.roof_block = roof_block
        self.z_len = z_len
        self.x_len = x_len
        self.y_len = y_len
        self.roof_v3['start'] = self.root_v3
        v3 = self.roof_v3['start']
        end_v3 = v.Vec3(v3.x + (self.x_len - 1), v3.y + (self.y_len - 1), v3.z + (self.z_len - 1))
        self.roof_v3['end'] = end_v3

if __name__ == '__main__':
    from mcpi import minecraft as m
    mc = m.Minecraft.create()
    player_v3 = mc.player.getPos()
    roof = Roof(roof_block=b.STONE_BRICK)