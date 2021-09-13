from mcpi import vec3
import sys
sys.path.append('../property')
# Import component
import components.component as component
# Import minecraft
from mcpi import minecraft
# Create connection
mc = minecraft.Minecraft.create()
# Get player's current position
player_pos = mc.player.getPos()
# Set build_pos to 5 blocks in front of player
build_pos = vec3.Vec3(player_pos.x + 5, player_pos.y-3, player_pos.z)

wall = component.Component('wall')
# Give wall a block_list
wall.block_list = []
for y_inc in range(3):
    for x_inc in range(15):
        for z_inc in range(1):
            wall.block_list.append(4)
# Give wall dimensions
wall.z_len = 1
wall.x_len = 15
wall.y_len = 3
# Build four walls with 4 different orientations
for i in range(4):
    wall.build(build_pos, mc, i)

# door = component.Component('door')
# door.block_list = []
# door.z_len = 1
# door.x_len = 2
# door.y_len = 2
# for i in range(door.y_len):
#     for j in range(door.x_len):
#         for k in range(door.z_len):
#             door.block_list.append(46)
# door.build(vec3.Vec3(build_pos.x+7, build_pos.y, build_pos.z), mc, 1)
