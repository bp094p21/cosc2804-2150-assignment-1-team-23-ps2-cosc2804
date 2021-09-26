# A map delineating what block should be used to plaster the ground below the village, dependent on the biome.
GROUND_FILLER = {'DESERT': 24,
                 'PLAINS': 2,
                 'REDWOOD': 2,
                 'HILLS': 2,
                 'JUNGLE': 2,
                 'FOREST': 2,
                 'ICE': 78}


def terraform_entire_land(mc, biome, x1, y1, z1, x2, y2, z2):
    mc.setBlocks(x1, y1, z1, x2, y2, z2, 0)

    ground_fill_block = iterate_ground_filler(GROUND_FILLER, biome)
    mc.setBlocks(x1, y1 - 1, z1, x2, y1 - 1, z2, ground_fill_block)

    #Then build a border around the village to clear any liquid seeping in
    # Create a border around the perimeter of the village (1 area difference)
    x, y, z = mc.player.getTilePos()
    block = mc.getBlock(x, y-3, z)
    mc.setBlocks(x1, 40, z1 - 1, x2, y, z1 - 1, block) 
    mc.setBlocks(x1 - 1, 40, z1, x1 - 1, y, z2, block)
    mc.setBlocks(x1, 40, z2 + 1, x2, y, z2 + 1, block)
    mc.setBlocks(x2 + 1, 40, z1, x2 + 1, y, z2, block)


# Searches the dictionary to see if the biome string is in any of the keys, and if it is, return the block id to pave
# the floor.
def iterate_ground_filler(keys, target):
    for i in keys:
        if target in i:
            return keys[i]
    # Default to grass otherwise.
    return 2

# Whilst most of the unused and abaonded code has been deleted from this package, this one was left due to its
# usefulness - especially in future. If the project is ever done correctly, then these functions would be incredibly
# useful along that journey, and they showcase the forked API.

# DISALLOWED_BLOCKS = (17, 18, 81, 86, 106, 161, 162, 175, 37, 38, 39, 40, 30, 10, 11, 31)

# # TIMBER_LOG = 17  (0 Oak, 1 Spruce)
# # LEAVES = 18 (Oak, 1 Spruce, 2 Birch, 3 Jungle)
# # CACTUS = 81
# # PUMPKIN = 86
# # VINE = 106
# # LEAVES2 = 161 (# 0 Acacia, 1 Dark Oak)
# # LOG = 162 (# 0 Acacia, 1 Dark Oak)
# # FLOWERS = 175
# # FLOWER_YELLOW = 37
# # FLOWER_RED = 38
# # MUSHROOM_BROWN = 39
# # MUSHROOM_RED = 40
# # COBWEB = 30
# # LAVA_FLOWING = 10
# # LAVA_STATIONARY = 11
# # GRASS_TALL = 31

# individual terraforming functions to accommodate for both shared and individual functionality.
# def terraform_house_plot(mc, start_loc, x2, z2):
#     print('LOG >> TERRAFORMING HOUSE PLOT')
#     _terraform(mc, start_loc, x2, z2)


# def terraform_road_plot(mc, start_loc, x2, z2):
#     print('LOG >> TERRAFORMING ROAD PLOT')
#     _terraform(mc, start_loc, x2, z2)


# # base terraforming function that handles the shared functionality.
# def _terraform(mc, start_loc, x2, z2):
#     x, y, z = start_loc
#     print('LOG >> GETTING HIGHEST/LOWEST Y')
#     print('X1=' + str(x))
#     print('Y1=' + str(y))
#     print('Z1=' + str(z))
#     print('x2=' + str(x2))
#     print('z2=' + str(z2))
#     y2, y1 = mc.getHighestAndLowestYInRegion(x, z, x2, z2)
#     print('LOG >> RECEIVED HIGHEST/LOWEST Y')
#     start_loc = (x, y1, z)
#     _clear_disallowed_blocks(mc, start_loc, x2, y2, z2)

# def _clear_disallowed_blocks(mc, start_loc, x2, y2, z2):
#     print('LOG >> CLEARING DISALLOWED BLOCKS')
#     x, y, z = start_loc
#     # Implemented on back-end because the transfer between sockets was a big bottleneck and
#     # slowed down program tremendously.
#     mc.removeBlocksInRegion(x, y, z, x2, y2, z2, *DISALLOWED_BLOCKS)
#     print('LOG >> CLEARED DISALLOWED BLOCKS')
