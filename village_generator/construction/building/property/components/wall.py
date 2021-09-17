from components.component import Component
import block as b
from mcpi import vec3 as v

class Wall(Component):
    # Class attributes
    type = 'wall'
    # Instance attributes
    root_v3: v.Vec3 = None
    wall_block: b.Block = None
    level: str = None
    name: str = None
    elevation: int = None
    z_len: int = None
    x_len: int = None
    wall_v3 = {
        'start': None,
        'end': None
    }
    def __init__(self, root_v3: v.Vec3, wall_block=b.WOOD_PLANKS, level='ground', name='main', elevation = 0, z_len=7, x_len=5, y_len=4):
        self.root_v3 = root_v3
        self.wall_block = wall_block
        self.level = level
        self.name = name
        self.elevation = elevation
        self.z_len = z_len
        self.x_len = x_len
        self.y_len = y_len
        self.wall_v3['start'] = self.root_v3
        v3 = self.wall_v3['start']
        end_v3 = v.Vec3(v3.x + (self.x_len - 1), v3.y + (self.y_len - 1), v3.z + (self.z_len - 1))
        self.wall_v3['end'] = end_v3


# TESTING
if __name__ == '__main__':
    from mcpi import minecraft as m
    mc = m.Minecraft.create()
    player_v3 = mc.player.getPos()
    wall = Wall(wall_block=b.WOOD_PLANKS, level='ground', name='main')