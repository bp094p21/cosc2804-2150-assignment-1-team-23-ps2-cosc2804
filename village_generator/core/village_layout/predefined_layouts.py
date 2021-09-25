from .layout import Layout
from .plot import Plot
from .orientation import Orientation
from construction import *

"""This module hosts 3 functions responsible for defining a different sized template."""

# Small variations. Function will randomly select between the two instantiated templates.
# Dimensions - 5 * 4 = 20 Elements
# Max Structures - 5
def define_small(mc, biome, theme, size):
       #FIXME: TEST CASE 1 WITH JUST HOUSES AND WHITESPACE
       # Layout(size,
       # [[Plot(House(mc, Orientation.NORTH.value, theme)), Plot(House(mc, Orientation.NORTH.value, theme)), Plot(), Plot()],
       # [Plot(), Plot(), Plot(), Plot(House(mc, Orientation.NORTH.value, theme))],
       # [Plot(), Plot(), Plot(), Plot()],
       # [Plot(), Plot(House(mc, Orientation.WEST.value, theme)), Plot(), Plot()],
       # [Plot(), Plot(), Plot(House(mc, Orientation.EAST.value, theme)), Plot()]])

       #FIXME: TEST CASE 2 WITH JUST HOUSES BUT NO WHITESPACE. FEEL FREE TO TEST WITH JUST ONE HOUSE.
       # Layout(size,
       # [[Plot(House(mc, Orientation.NORTH.value, theme)), Plot(House(mc, Orientation.NORTH.value, theme)), Plot(House(mc, Orientation.NORTH.value, theme)), Plot(House(mc, Orientation.NORTH.value, theme))],
       # [Plot(House(mc, Orientation.NORTH.value, theme)), Plot(House(mc, Orientation.NORTH.value, theme)), Plot(House(mc, Orientation.NORTH.value, theme)), Plot(House(mc, Orientation.NORTH.value, theme))],
       # [Plot(House(mc, Orientation.NORTH.value, theme)), Plot(House(mc, Orientation.NORTH.value, theme)), Plot(House(mc, Orientation.NORTH.value, theme)), Plot(House(mc, Orientation.NORTH.value, theme))],
       # [Plot(House(mc, Orientation.NORTH.value, theme)), Plot(House(mc, Orientation.NORTH.value, theme)), Plot(House(mc, Orientation.NORTH.value, theme)), Plot(House(mc, Orientation.NORTH.value, theme))],
       # [Plot(House(mc, Orientation.NORTH.value, theme)), Plot(House(mc, Orientation.NORTH.value, theme)), Plot(House(mc, Orientation.NORTH.value, theme)), Plot(House(mc, Orientation.NORTH.value, theme))]])

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


# Medium variations. Function will randomly select between the two instantiated templates.
# Dimensions - 6 * 5 = 30 Elements
# Max Structures - 7
def define_medium(mc, biome, theme, size):
    # Layout #1
    Layout(size,
           [[Plot(), Plot(), Plot(), Plot(build_intersection_e_ns, True), Plot(House(mc, Orientation.WEST.value, theme))],
            [Plot(), Plot(House(mc, Orientation.SOUTH.value, theme)), Plot(), Plot(build_straight_ns), Plot()],
            [Plot(build_bent_connecting_se), Plot(build_intersection_n_ew), Plot(build_straight_ew), Plot(build_crossintersection), Plot(build_straight_ew)],
            [Plot(build_straight_ns), Plot(Misc(mc, biome)), Plot(), Plot(build_straight_ns), Plot()],
            [Plot(build_straight_ns), Plot(), Plot(House(mc, Orientation.EAST.value, theme)), Plot(build_crossintersection), Plot(House(mc, Orientation.WEST.value, theme))],
            [Plot(House(mc, Orientation.NORTH.value, theme)), Plot(), Plot(), Plot(House(mc, Orientation.NORTH.value, theme)), Plot()]])

    # Layout #2
    Layout(size,
           [[Plot(), Plot(build_intersection_e_ns, True), Plot(build_bent_connecting_sw), Plot(), Plot()],
            [Plot(), Plot(Misc(mc, biome)), Plot(build_intersection_e_ns), Plot(build_straight_ew), Plot(House(mc, Orientation.WEST.value, theme))],
            [Plot(House(mc, Orientation.EAST.value, theme)), Plot(build_straight_ew), Plot(build_intersection_w_ns), Plot(), Plot()],
            [Plot(), Plot(House(mc, Orientation.EAST.value, theme)), Plot(build_crossintersection), Plot(House(mc, Orientation.WEST.value, theme)), Plot()],
            [Plot(), Plot(House(mc, Orientation.EAST.value, theme)), Plot(build_crossintersection), Plot(House(mc, Orientation.WEST.value, theme)), Plot()],
            [Plot(), Plot(), Plot(build_straight_ns), Plot(), Plot()]])


# Large variations. Function will randomly select between the two instantiated templates.
# Dimensions - 7 * 6 = 42 Elements
# Max Structures - 10
def define_large(mc, biome, theme, size):
    # Layout #1
    Layout(size,
           [[Plot(), Plot(House(mc, Orientation.SOUTH.value, theme)), Plot(), Plot(), Plot(build_straight_ns), Plot(House(mc, Orientation.WEST.value, theme))],
            [Plot(House(mc, Orientation.EAST.value, theme)), Plot(build_crossintersection), Plot(House(mc, Orientation.WEST.value, theme)), Plot(), Plot(build_straight_ns), Plot(House(mc, Orientation.WEST.value, theme))],
            [Plot(), Plot(build_intersection_e_ns), Plot(build_straight_ew), Plot(build_straight_ew), Plot(build_crossintersection), Plot(build_straight_ew)],
            [Plot(Misc(mc, biome)), Plot(build_intersection_w_ns), Plot(), Plot(), Plot(build_straight_ns), Plot()],
            [Plot(), Plot(build_straight_ns), Plot(), Plot(House(mc, Orientation.EAST.value, theme)), Plot(build_crossintersection), Plot(House(mc, Orientation.WEST.value, theme))],
            [Plot(), Plot(build_straight_ns), Plot(Misc(mc, biome)), Plot(), Plot(House(mc, Orientation.NORTH.value, theme)), Plot()],
            [Plot(), Plot(build_bent_connecting_ne), Plot(build_straight_ew), Plot(build_straight_ew), Plot(build_straight_ew), Plot(build_straight_ew, True)]])

    # Layout #2
    Layout(size,
           [[Plot(House(mc, Orientation.EAST.value, theme)), Plot(build_straight_ew), Plot(build_bent_connecting_sw), Plot(), Plot(House(mc, Orientation.EAST.value, theme)), Plot(build_intersection_w_ns, True)],
            [Plot(), Plot(), Plot(build_bent_connecting_ne), Plot(build_bent_connecting_sw), Plot(House(mc, Orientation.EAST.value, theme)), Plot(build_intersection_w_ns)],
            [Plot(), Plot(), Plot(Misc(mc, biome)), Plot(build_straight_ns), Plot(House(mc, Orientation.EAST.value, theme)), Plot(build_intersection_w_ns)],
            [Plot(), Plot(build_bent_connecting_se), Plot(build_straight_ew), Plot(build_crossintersection), Plot(build_straight_ew), Plot(build_bent_connecting_nw)],
            [Plot(House(mc, Orientation.EAST.value, theme)), Plot(build_crossintersection), Plot(House(mc, Orientation.EAST.value, theme)), Plot(build_crossintersection), Plot(House(mc, Orientation.WEST.value, theme)), Plot()],
            [Plot(Misc(mc, biome)), Plot(build_straight_ns), Plot(), Plot(build_bent_connecting_ne), Plot(build_straight_ew), Plot(build_bent_connecting_sw)],
            [Plot(House(mc, Orientation.EAST.value, theme)), Plot(build_intersection_w_ns), Plot(), Plot(), Plot(), Plot(build_straight_ns)]])
