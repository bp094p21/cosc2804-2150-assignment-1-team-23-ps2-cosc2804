from core.village_layout.layout import Layout
from core.village_layout.plot import Plot
from construction import *


# TODO - all the buildings must both implement the build() method, and they must have a setter to set location.
#  Enforce this later.

# TODO - consider path finding to randomise the roads. Do at very end once everything else is finished though.


# Small variations.
# Dimensions - 5 * 4 = 20 Elements
# Max Structures - 5
def define_small(mc, biome, size):
    # Layout #1
    
    Layout(size,
           [[Plot(), Plot(build_bent_connecting_se), Plot(build_straight_ew), Plot()],
            [Plot(build_straight_ew, True), Plot(build_intersection_w_ns), Plot(), Plot()],
            [Plot(), Plot(build_intersection_e_ns), Plot(build_straight_ew), Plot()],
            [Plot(), Plot(build_straight_ns), Plot(), Plot()],
            [Plot(), Plot(build_intersection_n_ew), Plot(), Plot()]])

    # Layout #2
    Layout(size,
           [[Plot(), Plot(), Plot(build_bent_connecting_se), Plot()],
            [Plot(), Plot(build_straight_ew), Plot(build_intersection_w_ns), Plot()],
            [Plot(), Plot(), Plot(build_intersection_e_ns), Plot()],
            [Plot(), Plot(build_straight_ew), Plot(build_intersection_w_ns), Plot()],
            [Plot(), Plot(), Plot(build_straight_ns, True), Plot()]])


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
