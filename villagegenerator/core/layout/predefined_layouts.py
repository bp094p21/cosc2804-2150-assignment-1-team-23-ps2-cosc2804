from plot import Plot
from villagegenerator.core import village_generator as vg
from villagegenerator.core.village.village_size import VillageSize
from orientation import Orientation as O


# set of global variables to be accessed in the main program.

# TODO - make these only be created if the user requests them. Dont all need to exist. Wrap in some sort of function.
# TODO - all the buildings must both implement the build() method, and they must have a setter to set location.
#  Enforce this later.


def define_layouts(biome, mc_instance, size):
    pass


biome = vg.ply_biome
mc = vg.mc

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
                       [Plot(Property(O.RIGHT, biome, mc))]]

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

size_to_layout = {
    VillageSize.SMALL: (SMALL_VARIATION_ONE, SMALL_VARIATION_TWO),
    VillageSize.MEDIUM: (MED_VARIATION_ONE, MED_VARIATION_TWO),
    VillageSize.LARGE: (LARGE_VARIATION_ONE, LARGE_VARIATION_TWO)
}
