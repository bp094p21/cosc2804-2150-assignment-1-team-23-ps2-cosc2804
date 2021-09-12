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
build_pos = player_pos[0] + 5, player_pos[1], player_pos[2]
y, z, x = build_pos
# Initialize block type
block_type = 0

# Set Stone blocks in x-axis
mc.setBlocks(y,z,x, y,z,x+2, 1)
# Set Grass blocks in y-axis
mc.setBlocks(y,z,x, y+2,z,x, 2)
# Set Wood blocks in z-axis
mc.setBlocks(y,z,x, y,z+2,x, 5)

entrance = component.Entrance()
# Give entrance a block_list
entrance.block_list = [1,1,1,1,1,1,2,2,2,2,2,2]
# Give entrance dimensions
entrance.z_len = 3
entrance.x_len = 2
entrance.y_len = 1
entrance.build(build_pos, mc)