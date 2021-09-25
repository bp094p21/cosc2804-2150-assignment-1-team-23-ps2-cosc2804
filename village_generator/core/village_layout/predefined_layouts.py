from .layout import Layout
from .plot import Plot
from .orientation import Orientation
from construction import *


# TODO - all the buildings must both implement the build() method, and they must have a setter to set location.
#  Enforce this later.

# TODO - consider path finding to randomise the roads. Do at very end once everything else is finished though.


# Small variations.
# Dimensions - 5 * 4 = 20 Elements
# Max Structures - 5
def define_small(mc, biome, theme, size):
    # Layout #1
    Layout(size,
           [[Plot(), Plot(build_bent_connecting_se), Plot(build_straight_ew), Plot(House(mc, Orientation.WEST.value, theme))],
            [Plot(build_straight_ew, True), Plot(build_intersection_w_ns), Plot(), Plot()],
            [Plot(Misc(mc, biome)), Plot(build_intersection_e_ns), Plot(build_straight_ew), Plot(House(mc, Orientation.WEST.value, theme))],
            [Plot(), Plot(build_straight_ns), Plot(), Plot()],
            [Plot(House(mc, Orientation.EAST.value, theme)), Plot(build_intersection_n_ew), Plot(House(mc, Orientation.WEST.value, theme)), Plot()]])

    # Layout #2
    Layout(size,
           [[Plot(), Plot(), Plot(build_bent_connecting_se), Plot(House(mc, Orientation.WEST.value, theme))],
            [Plot(House(mc, Orientation.EAST.value, theme)), Plot(build_straight_ew), Plot(build_intersection_w_ns), Plot()],
            [Plot(), Plot(Misc(mc, biome)), Plot(build_intersection_e_ns), Plot(House(mc, Orientation.WEST.value, theme))],
            [Plot(House(mc, Orientation.EAST.value, theme)), Plot(build_straight_ew), Plot(build_intersection_w_ns), Plot()],
            [Plot(), Plot(), Plot(build_straight_ns, True), Plot()]])


# Medium variations.
# Dimensions - 6 * 5 = 30 Elements
# Max Structures - 7
def define_medium(mc, biome, theme, size):
    # Layout #1
    Layout(size,
           [[Plot(), Plot(), Plot(), Plot(build_intersection_e_ns, True), Plot()],
            [Plot(), Plot(), Plot(), Plot(build_straight_ns), Plot()],
            [Plot(build_bent_connecting_se), Plot(build_straight_ew), Plot(build_straight_ew), Plot(build_crossintersection), Plot(build_straight_ew)],
            [Plot(build_straight_ns), Plot(Misc(mc, biome)), Plot(), Plot(build_straight_ns), Plot()],
            [Plot(build_straight_ns), Plot(), Plot(), Plot(build_crossintersection), Plot()],
            [Plot(), Plot(), Plot(), Plot(), Plot()]])

    # Layout #2
    Layout(size,
           [[Plot(), Plot(build_intersection_e_ns, True), Plot(build_bent_connecting_sw), Plot(), Plot()],
            [Plot(), Plot(Misc(mc, biome)), Plot(build_intersection_e_ns), Plot(build_straight_ew), Plot()],
            [Plot(), Plot(build_straight_ew), Plot(build_intersection_w_ns), Plot(), Plot()],
            [Plot(), Plot(), Plot(build_crossintersection), Plot(), Plot()],
            [Plot(), Plot(), Plot(build_crossintersection), Plot(), Plot()],
            [Plot(), Plot(), Plot(build_straight_ns), Plot(), Plot()]])


# Large variations.
# Dimensions - 7 * 6 = 42 Elements
# Max Structures - 10
def define_large(mc, biome, theme, size):
    # Layout #1
    Layout(size,
           [[Plot(), Plot(), Plot(), Plot(), Plot(build_straight_ns), Plot()],
            [Plot(), Plot(build_crossintersection), Plot(), Plot(), Plot(build_straight_ns), Plot()],
            [Plot(), Plot(build_intersection_e_ns), Plot(build_straight_ew), Plot(build_straight_ew), Plot(build_crossintersection), Plot(build_straight_ew)],
            [Plot(Misc(mc, biome)), Plot(build_intersection_w_ns), Plot(), Plot(), Plot(build_straight_ns), Plot()],
            [Plot(), Plot(build_straight_ns), Plot(), Plot(), Plot(), Plot()],
            [Plot(), Plot(build_straight_ns), Plot(Misc(mc, biome)), Plot(), Plot(), Plot()],
            [Plot(), Plot(build_bent_connecting_ne), Plot(build_straight_ew), Plot(build_straight_ew), Plot(build_straight_ew), Plot(build_straight_ew, True)]])

    # Layout #2
    Layout(size,
           [[Plot(), Plot(build_straight_ew), Plot(build_bent_connecting_sw), Plot(), Plot(), Plot(build_straight_ns, True)],
            [Plot(), Plot(), Plot(build_bent_connecting_ne), Plot(build_bent_connecting_sw), Plot(), Plot(build_straight_ns)],
            [Plot(), Plot(), Plot(Misc(mc, biome)), Plot(build_straight_ns), Plot(), Plot(build_straight_ns)],
            [Plot(), Plot(build_bent_connecting_se), Plot(build_straight_ew), Plot(build_crossintersection), Plot(build_straight_ew), Plot(build_bent_connecting_nw)],
            [Plot(), Plot(build_straight_ns), Plot(), Plot(build_straight_ns), Plot(), Plot()],
            [Plot(Misc(mc, biome)), Plot(build_straight_ns), Plot(), Plot(build_bent_connecting_ne), Plot(build_straight_ew), Plot(build_bent_connecting_sw)],
            [Plot(), Plot(build_straight_ns), Plot(), Plot(), Plot(), Plot(build_straight_ns)]])
