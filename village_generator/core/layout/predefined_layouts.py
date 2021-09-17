from plot import Plot
from layout import Layout
from village_generator.construction import *


# TODO - all the buildings must both implement the build() method, and they must have a setter to set location.
#  Enforce this later.


# Small variations.
# Dimensions - 5 * 4 = 20 Elements
# Max Structures - 5
def define_small(mc, biome, size):
    # Layout #1
    Layout(size,
           [[Plot(), Plot(build_bent_connecting_ne), Plot(build_straight_ew), Plot()],
            [Plot(build_straight_ew), Plot(build_crossintersection), Plot(), Plot()],
            [Plot(), Plot(build_crossintersection), Plot(build_straight_ew), Plot()],
            [Plot(), Plot(build_straight_ns), Plot(), Plot()],
            [Plot(), Plot(build_crossintersection), Plot(), Plot()]])

    # Layout #2
    Layout(size,
           [[Plot(), Plot(), Plot(build_bent_connecting_se), Plot()],
            [Plot(), Plot(build_straight_ew), Plot(build_crossintersection), Plot()],
            [Plot(), Plot(), Plot(build_crossintersection), Plot()],
            [Plot(), Plot(build_straight_ew), Plot(build_crossintersection), Plot()],
            [Plot(), Plot(), Plot(build_straight_ns), Plot()]])


# Medium variations.
# Dimensions - 6 * 5 = 30 Elements
# Max Structures - 7
def define_medium(mc, biome, size):
    # Layout #1
    Layout(size,
           [[],
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
            []])


# Large variations.
# Dimensions - 7 * 6 = 42 Elements
# Max Structures - 10
def define_large(mc, biome, size):
    # Layout #1
    Layout(size,
           [[],
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
            []])
