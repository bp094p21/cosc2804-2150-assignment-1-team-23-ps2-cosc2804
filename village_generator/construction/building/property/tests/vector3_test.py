# Import minecraft
from mcpi import minecraft

# Create connection
mc = minecraft.Minecraft.create()
# Get player's current position
player_pos = mc.player.getPos()
x_player, y_player, z_player = player_pos
# Set build_pos to 5 blocks in front of player
build_pos = x_player + 5, y_player, z_player
y, z, x = build_pos
# Initialize block type
block_type = 0

# Set Stone blocks in x-axis
mc.setBlocks(y, z, x, y, z, x + 2, 1)
# Set Grass blocks in y-axis
mc.setBlocks(y, z, x, y + 2, z, x, 2)
# Set Wood blocks in z-axis
mc.setBlocks(y, z, x, y, z + 2, x, 5)
