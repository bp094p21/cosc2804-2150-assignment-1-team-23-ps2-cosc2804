import sys

sys.path.append('../property')
import components.component as component

from mcpi import vec3
from mcpi import minecraft

mc = minecraft.Minecraft.create()
player_pos = mc.player.getPos()
build_pos = vec3.Vec3(player_pos.x + 5, player_pos.y, player_pos.z)

all_blocks_component = component.Component('all_blocks')
all_blocks_component.block_list = []
all_blocks_component.z_len = 256
all_blocks_component.y_len = 1
all_blocks_component.x_len = 1
for i in range(256):
    all_blocks_component.block_list.append(i)
all_blocks_component.build(build_pos, mc)
