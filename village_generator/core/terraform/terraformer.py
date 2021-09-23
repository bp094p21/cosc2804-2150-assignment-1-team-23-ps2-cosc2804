# terraformer

DISALLOWED_BLOCKS = (17, 18, 81, 86, 106, 161, 162, 175, 37, 38, 39, 40, 30, 10, 11, 31)
# TIMBER_LOG = 17  (0 Oak, 1 Spruce)
# LEAVES = 18 (Oak, 1 Spruce, 2 Birch, 3 Jungle)
# CACTUS = 81
# PUMPKIN = 86
# VINE = 106
# LEAVES2 = 161 (# 0 Acacia, 1 Dark Oak)
# LOG = 162 (# 0 Acacia, 1 Dark Oak)
# FLOWERS = 175
# FLOWER_YELLOW = 37
# FLOWER_RED = 38
# MUSHROOM_BROWN = 39
# MUSHROOM_RED = 40
# COBWEB = 30
# LAVA_FLOWING = 10
# LAVA_STATIONARY = 11
# GRASS_TALL = 31


# individual terraforming functions to accommodate for both shared and individual functionality.

def terraform_entire_land(mc, biome, x1, y1, z1, x2, y2, z2):
    mc.setBlocks(x1, y1, z1, x2, y2, z2, 0)
    
    ground_fill_block = iterate_ground_filler(GROUND_FILLER, biome)
    mc.setBlocks(x1, y1 - 1, z1, x2, y1 - 1, z2, ground_fill_block)

# searches the dictionary to see if the biome string is in any of the keys, and if it is, return the block id to pave the floor.
def iterate_ground_filler(keys, target):
    for i in keys:
        if target in i:
            return keys[i]
    # default to grass otherwise.
    return 2

GROUND_FILLER = {'DESERT': 24,
'PLAINS': 2,
'REDWOOD': 2,
'HILLS': 2,
'JUNGLE': 2,
'FOREST': 2,
'ICE': 78}

def terraform_house_plot(mc, start_loc, max_x, max_z):
    print('LOG >> TERRAFORMING HOUSE PLOT')
    _terraform(mc, start_loc, max_x, max_z)


def terraform_road_plot(mc, start_loc, max_x, max_z):
    print('LOG >> TERRAFORMING ROAD PLOT')
    _terraform(mc, start_loc, max_x, max_z)


# base terraforming function that handles the shared functionality.
def _terraform(mc, start_loc, max_x, max_z):
    x, y, z = start_loc
    print('LOG >> GETTING HIGHEST/LOWEST Y')
    print('X1=' + str(x))
    print('Y1=' + str(y))
    print('Z1=' + str(z))
    print('MAX_X=' + str(max_x))
    print('MAX_Z=' + str(max_z))
    max_y, min_y = mc.getHighestAndLowestYInRegion(x, z, max_x, max_z)
    print('LOG >> RECEIVED HIGHEST/LOWEST Y')
    start_loc = (x, min_y, z)
    _clear_disallowed_blocks(mc, start_loc, max_x, max_y, max_z)


# responsible for flattening some land and smoothing it out in a crater sort of fashion.
# TODO: Make a realistic crater, such that it digs into the ground a little bit, but realistically, and plop the
#  village in there. If it is on a mountain, just level parts of the mountain. Depending on biome and other
#  mathematically derived heuristics.
def flatten_and_smooth():
    pass


# Implemented on back-end because the transfer between sockets was a big bottleneck and slowed down program tremendously.

# removes any trees and logs.
def _clear_disallowed_blocks(mc, start_loc, max_x, max_y, max_z):
    print('LOG >> CLEARING DISALLOWED BLOCKS')
    x, y, z = start_loc
    mc.removeBlocksInRegion(x, y, z, max_x, max_y, max_z, *DISALLOWED_BLOCKS)
    print('LOG >> CLEARED DISALLOWED BLOCKS')


# clears any randomly placed blocks that are going to be in the section of the build.
# for ex: if there are floating blocks of dirt or things that will be on the road or above it, clear it.
# clear anything above a certain height, but dont cut out the land.
def _clear_random_blocks():
    pass


# this will ensure that the terrain does not jump by two blocks, because if it does, then the user will not be able
# to walk up the road (players can only jump one block).
# FIXME - consider making this function essentially "flatten" the land or make it unsuitable terrain for the terrain scanner
#  if there are more than x > 1 block jumps or something.
def _enforce_single_height_increments(mc, x, ):
    pass


# TODO - make a get_lowest_point for the houses, so that they are built at the lowest point to avoid them being very
#  high up in the air. Cause this would mean roads could not reach it without incrementing more than one block. Also
#  need to consider that the position where the roads and houses integrate may be off. Moreover, the house may take up
#  all of the 15x15 and this idea would no longer be feasible.
# def _get_highest_point(mc, x, z, max_x, max_z) -> int:
#     # excessive calls to mc's methods are too expensive and slow. test speed difference with this vs backend re-write.
#     # this guess may be off too and could cause problems. consider re-writing on backend.
#     return 
