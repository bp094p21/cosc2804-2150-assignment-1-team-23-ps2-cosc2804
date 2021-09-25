from mcpi import minecraft
from mcpi import vec3

import component


class Cloner:
    def __init__(self, mc: minecraft.Minecraft, x_len=15, y_len=15, z_len=15):
        self.mc = mc
        self.x_len = x_len
        self.y_len = y_len
        self.z_len = z_len

    def clone(self, original_pos, x=0, y=0, z=15):
        blocks = self.mc.getBlocks(original_pos, original_pos.x + self.x_len - 1, original_pos.y + self.y_len - 1,
                                   original_pos.z + self.z_len - 1)
        clone_pos = vec3.Vec3(original_pos.x + x, original_pos.y + y, original_pos.z + z)
        clone = component.Component('clone')
        clone.block_list = blocks
        clone.x_len = self.x_len
        clone.y_len = self.y_len
        clone.z_len = self.z_len
        clone.build(clone_pos, self.mc, 0)


# TEST
if __name__ == "__main__":
    mc = minecraft.Minecraft.create()
    c = Cloner(mc)
    player_pos = mc.player.getPos()
    original_pos = vec3.Vec3(player_pos.x + 5, player_pos.y, player_pos.z - 8)
    c.clone(original_pos)
