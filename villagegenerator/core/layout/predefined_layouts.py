from plot import Plot
from villagegenerator.core import village_generator as vg
from orientation import Orientation as o
import grid_manager

# set of global variables to be accessed in the main program.

# TODO - make these only be created if the user requests them. Dont all need to exist.

biome = vg.ply_biome


def _generate_fixed_ordinates(max_z: int, max_x: int, x_coord: int, y_coord: int, z_coord: int) -> list:
    temp = []
    for z in range(0, max_z + 1):
        for x in range(0, max_x + 1):
            temp.append((x_coord + x * 15, y_coord, z_coord + z * 15))

    return temp


FIXED_ORDINATES = _generate_fixed_ordinates(12, 6, *vg.ply_coords)

# T = [(X, Y, Z), (X + 15, Y, Z), (X + 30, Y, Z), (X + 45, Y, Z), (X + 60, Y, Z),
#      (X + 75, Y, Z), (X + 90, Y, Z),
#      (X, Y, Z + 15), (X + 15, Y, Z + 15), (X + 30, Y, Z + 15), (X + 45, Y, Z + 15),
#      (X + 60, Y, Z + 15), (X + 75, Y, Z + 15), (X + 90, Y, Z + 15),
#      (X, Y, Z + 30), (X + 15, Y, Z + 30), (X + 30, Y, Z + 30), (X + 45, Y, Z + 30),
#      (X + 60, Y, Z + 30), (X + 75, Y, Z + 30), (X + 90, Y, Z + 30),
#      (X, Y, Z + 45), (X + 15, Y, Z + 45), (X + 30, Y, Z + 45), (X + 45, Y, Z + 45),
#      (X + 60, Y, Z + 45), (X + 75, Y, Z + 45), (X + 90, Y, Z + 45),
#      (X, Y, Z + 60), (X + 15, Y, Z + 60), (X + 30, Y, Z + 60), (X + 45, Y, Z + 60),
#      (X + 60, Y, Z + 60), (X + 75, Y, Z + 60), (X + 90, Y, Z + 60),
#      (X, Y, Z + 75), (X + 15, Y, Z + 75), (X + 30, Y, Z + 75), (X + 45, Y, Z + 75),
#      (X + 60, Y, Z + 75), (X + 75, Y, Z + 75), (X + 90, Y, Z + 75),
#      (X, Y, Z + 90), (X + 15, Y, Z + 90), (X + 30, Y, Z + 90), (X + 45, Y, Z + 90),
#      (X + 60, Y, Z + 90), (X + 75, Y, Z + 90), (X + 90, Y, Z + 90),
#      (X, Y, Z + 105), (X + 15, Y, Z + 105), (X + 30, Y, Z + 105), (X + 45, Y, Z + 105),
#      (X + 60, Y, Z + 105), (X + 75, Y, Z + 105), (X + 90, Y, Z + 105),
#      (X, Y, Z + 120), (X + 15, Y, Z + 120), (X + 30, Y, Z + 120), (X + 45, Y, Z + 120),
#      (X + 60, Y, Z + 120), (X + 75, Y, Z + 120), (X + 90, Y, Z + 120),
#      (X, Y, Z + 135), (X + 15, Y, Z + 135), (X + 30, Y, Z + 135), (X + 45, Y, Z + 135),
#      (X + 60, Y, Z + 135), (X + 75, Y, Z + 135), (X + 90, Y, Z + 135),
#      (X, Y, Z + 150), (X + 15, Y, Z + 150), (X + 30, Y, Z + 150), (X + 45, Y, Z + 150),
#      (X + 60, Y, Z + 150), (X + 75, Y, Z + 150), (X + 90, Y, Z + 150),
#      (X, Y, Z + 165), (X + 15, Y, Z + 165), (X + 30, Y, Z + 165), (X + 45, Y, Z + 165),
#      (X + 60, Y, Z + 165), (X + 75, Y, Z + 165), (X + 90, Y, Z + 165),
#      (X, Y, Z + 180), (X + 15, Y, Z + 180), (X + 30, Y, Z + 180), (X + 45, Y, Z + 180),
#      (X + 60, Y, Z + 180), (X + 75, Y, Z + 180), (X + 90, Y, Z + 180)]


# Small variations.
# Dimensions - 8 * 4 = 32 Elements
# Max Structures - 4
SMALL_VARIATION_ONE = [[],
                       [],
                       [],
                       [],
                       [],
                       [],
                       [],
                       [Plot(Property(biome, FIXED_ORDINATES[0], o.RIGHT))]]

SMALL_VARIATION_TWO = [[],
                       [],
                       [],
                       [],
                       [],
                       [],
                       [],
                       []]

# Medium variations.
# Dimensions - 10 * 5 = 50 Elements
# Max Structures - 6
MED_VARIATION_ONE = [[],
                     [],
                     [],
                     [],
                     [],
                     [],
                     [],
                     [],
                     [],
                     []]

MED_VARIATION_TWO = [[],
                     [],
                     [],
                     [],
                     [],
                     [],
                     [],
                     [],
                     [],
                     []]

# Large variations.
# Dimensions - 12 * 6 = 72 Elements
# Max Structures - 8
LARGE_VARIATION_ONE = [[],
                       [],
                       [],
                       [],
                       [],
                       [],
                       [],
                       [],
                       [],
                       [],
                       [],
                       []]

LARGE_VARIATION_TWO = [[],
                       [],
                       [],
                       [],
                       [],
                       [],
                       [],
                       [],
                       [],
                       [],
                       [],
                       []]
