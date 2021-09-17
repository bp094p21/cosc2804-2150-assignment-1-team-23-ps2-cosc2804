from mcpi import vec3
import sys
sys.path.append('../property')
# Import property
import property
# Import minecraft
from mcpi import minecraft
# Create connection
mc = minecraft.Minecraft.create()
# Get player's current position
player_pos = mc.player.getPos()
# Set build_pos to 5 blocks in front of player
build_pos = vec3.Vec3(player_pos.x + 5, player_pos.y, player_pos.z)
# Set entrance_edge, biome
entrance_edge = 0
biome = 0

# Initialize object to store properties (Example is array but can be any object such as a matrix)
properties = []
# Instantiate Property object with required arguments
prop = property.Property(build_pos, entrance_edge, biome, mc)
# Append new Property object to properties array
properties.append(prop)
# Build prop
prop.build()