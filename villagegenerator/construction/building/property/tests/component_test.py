from mcpi import vec3
import sys
sys.path.append('../property')
# Import component
import component
# Import minecraft
from mcpi import minecraft
# Create connection
mc = minecraft.Minecraft.create()
# Get player's current position
player_pos = mc.player.getPos()
# Set build_pos to 5 blocks in front of player
build_pos = vec3.Vec3(player_pos.x + 5, player_pos.y, player_pos.z)

entrance = component.Entrance()
# Give entrance a block_list
entrance.block_list = []
for y_inc in range(3):
    for x_inc in range(15):
        for z_inc in range(1):
            entrance.block_list.append(4)
# Give entrance dimensions
entrance.z_len = 1
entrance.x_len = 15
entrance.y_len = 3
entrance.build(build_pos, mc)

door = component.Component('door')
door.block_list = []
door.z_len = 1
door.x_len = 2
door.y_len = 2
for i in range(door.y_len):
    for j in range(door.x_len):
        for k in range(door.z_len):
            door.block_list.append(46)
door.build(vec3.Vec3(build_pos.x+7, build_pos.y, build_pos.z), mc)
all_blocks = component.Component('all_blocks')

all_blocks.block_list = []
all_blocks.z_len = 1
for i in range(256):
    mc.setBlock(build_pos.x, build_pos.y, build_pos.z + i, i)
