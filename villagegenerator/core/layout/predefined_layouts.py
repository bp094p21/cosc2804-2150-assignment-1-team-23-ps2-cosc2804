from plot import Plot
from orientation import Orientation as O
from villagegenerator.core.layout.layout import Layout


# TODO - all the buildings must both implement the build() method, and they must have a setter to set location.
#  Enforce this later.


# Small variations.
# Dimensions - 8 * 4 = 32 Elements
# Max Structures - 4
def define_small(mc, biome, size):
    # Layout #1
    Layout(size,
           [[],
            [],
            [],
            [],
            [],
            [],
            [],
            [Plot(Property(O.RIGHT, biome, mc))]])

    # Layout #2
    Layout(size,
           [[],
            [],
            [],
            [],
            [],
            [],
            [],
            []])


# Medium variations.
# Dimensions - 10 * 5 = 50 Elements
# Max Structures - 6
def define_medium(mc, biome, size):
    # Layout #1
    Layout(size,
           [[],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            []])

    # Layout #2
    Layout(size,
           [[],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            []])


# Large variations.
# Dimensions - 12 * 6 = 72 Elements
# Max Structures - 8
def define_large(mc, biome, size):
    # Layout #1
    Layout(size,
           [[],
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
            []])
    # Layout #2
    Layout(size,
           [[],
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
            []])
