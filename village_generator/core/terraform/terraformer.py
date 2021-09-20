# terraformer

DISALLOWED_BLOCKS = (17, 18, 81, 86, 126)


# individual terraforming functions to accommodate for both shared and individual functionality.

def terraform_house_plot(mc, start_loc, max_x, max_z):
    _terraform(mc, start_loc, max_x, max_z)


def terraform_road_plot(mc, start_loc, max_x, max_z):
    _terraform(mc, start_loc, max_x, max_z)


# base terraforming function that handles the shared functionality.
def _terraform(mc, start_loc, max_x, max_z):
    x, y, z = start_loc

    max_y = _get_highest_point(mc, x, z, max_x, max_z)

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
    x, y, z = start_loc
    mc.removeBlocksInRegion(x, y, z, max_x, max_y, max_z, *DISALLOWED_BLOCKS)


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
def _get_highest_point(mc, x, z, max_x, max_z) -> int:
    # excessive calls to mc's methods are too expensive and slow. test speed difference with this vs backend re-write.
    # this guess may be off too and could cause problems. consider re-writing on backend.
    return mc.getHighestYInRegion(x, z, max_x, max_z)
