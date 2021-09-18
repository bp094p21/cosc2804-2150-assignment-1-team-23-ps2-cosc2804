# terraformer

DISALLOWED_BLOCKS = (17, 18, 81, 86, 126)


def terraform(mc, start_loc, max_x, max_z):
    x, y, z = start_loc

    # when sorted, use this instead of assuming y + 15.
    max_y = _get_highest_point(mc, start_loc, max_x, max_z)

    _clear_disallowed_blocks(mc, start_loc, max_x, max_y, max_z)


# responsible for flattening some land and smoothing it out in a crater sort of fashion.
# TODO: Make a realistic crater, such that it digs into the ground a little bit, but realistically, and plop the
#  village in there. If it is on a mountain, just level parts of the mountain. Depending on biome and other
#  mathematically derived heuristics.
def flatten_and_smooth():
    pass


# removes any trees and logs.
def _clear_disallowed_blocks(mc, start_loc, max_x, max_y, max_z):
    x, y, z = start_loc
    mc.removeBlocksInRegion(x, y, z, max_x, max_y, max_z, *DISALLOWED_BLOCKS)


# clears any randomly placed blocks that are going to be in the section of the build.
# for ex: if there are floating blocks of dirt or things that will be on the road or above it, clear it.
# clear anything above a certain height, but dont cut out the land.
def _clear_random_blocks():
    pass


def _get_highest_point(mc, start_loc, max_x, max_z) -> int:
    # excessive calls to mc's methods are too expensive and slow. test speed difference with this vs backend re-write.
    # this guess may be off too and could cause problems. consider re-writing on backend.
    pass
