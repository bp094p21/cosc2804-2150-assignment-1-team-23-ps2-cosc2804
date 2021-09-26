import random

from core.village_layout import predefined_layouts as pl
from core.village_layout import Layout, PlotType
from .village_size import VillageSize
from construction import Architect, MiscBuilder
from core.terraform import *
from mcpi.vec3 import Vec3

"""This module hosts a series of functions that are responsible for generating a village. This is the API for this 
application. A client should interact with this program by simply calling the build_village() function, 
and specifiying the deisred specifications via argument insertion."""


# This module was designed with a functional programming approach, as only local behaviour was required (not state),
# thus deeming an object oriented style less effective. The functions all try to remain as pure as possible to avoid
# unintended side-affects, and to allow for easy unit testing. However, there is a tight coupling between the private
# functions within this module, and thereby, the build_village() function is best tested with its dependencies (
# private functions).


def build_village(size, location, biome, mc):
    """
    Create a custom Minecraft village.

    The main, public function which is the main interface for the client to interact with and create a village.

    Parameters
    ----------
    size : VillageSize
        An enum constant representing the size of the village (SMALL, MEDIUM, LARGE).
    location : Tuple of ints
        The x, y and z coordinates to begin creation.
    biome: str
        The player's biome.
    mc: Minecraft
        The running mcpi Minecraft instance.

    Examples
    --------
    >>> build_village(VillageSize.MEDIUM, mc.player.getPos(), mc.player.getBiome(), mc)
    Generating village...
    Done. Welcome to your new village!

        * You will then be teleported to the village's entrance in-game. *

    >>> build_village(VillageSize.SMALL, mc.player.getTilePos(), mc.player.getBiome(), mc)
    Generating village...
    Done. Welcome to your new village!

        * You will then be teleported to the village's entrance in-game. *
    """

    # Before layouts or anything is defined/built, scan the land and then if appropriate, perform terraform.
    if not scan_terrain(mc, location, size):
        return

    # We no longer require the y-coordinate past this point, hence it is discarded from hereon.
    location = (location[0], location[2])

    mc.postToChat('Generating village...')

    # Define the layout objects and store them.
    _define_layout(size, biome, 'medi', mc)
    # Select a random template from the two layouts just defined.
    selected_template = _select_random_template(size)

    if size is VillageSize.SMALL:
        entrance_location = _build_generic(selected_template, mc, biome, 5, 4, *location)
    elif size is VillageSize.MEDIUM:
        entrance_location = _build_generic(selected_template, mc, biome, 6, 5, *location)
    else:
        entrance_location = _build_generic(selected_template, mc, biome, 7, 6, *location)

    # Teleport the player to the entrance of the village.
    mc.player.setPos(entrance_location[0], entrance_location[1], entrance_location[2])
    mc.postToChat('Done. Welcome to your new village!')


def _define_layout(size, biome, theme, mc):
    if len(Layout.layouts[size]) == 2:
        return

    if size is VillageSize.SMALL:
        pl.define_small(mc, biome, theme, size)
    elif size is VillageSize.MEDIUM:
        pl.define_medium(mc, biome, theme, size)
    else:
        pl.define_large(mc, biome, theme, size)


def _select_random_template(size):
    return random.choice(Layout.layouts[size]).grid


def _build_generic(template, mc, biome, length_z, length_x, x, z):
    max_z = z + 15 * length_z
    max_x = x + 15 * length_x

    # Obtain the highest and lowest y-value within the region specified (depends on size).
    max_y, min_y = mc.getHighestAndLowestYInRegion(x, z, max_x, max_z)

    # Flatten and remove all blocks within this region and plaster the floor with an appropriate block relative to
    # the biome.
    terraform_entire_land(mc, biome, x, min_y, z, max_x, max_y, max_z)

    # Return the entrance coordinates, after first generating the fixed ordinates (grid system for each plot's
    # placement) and then building each plot's item.
    return _build_plots(_generate_fixed_ordinates(length_z, length_x, x, min_y, z), template, mc)


# Responsible for iterating the selected template and building all the items within it.
def _build_plots(fixed_ordinates, template, mc):
    house_builder = Architect()
    misc_builder = MiscBuilder()
    entrance_location = None

    for (i, row) in enumerate(template):
        for (j, plot) in enumerate(row):
            # Set the y-coords to be dynamic.
            coordinates = fixed_ordinates[i][j]

            if plot.plot_type == PlotType.HOUSE:
                house_builder.give_specs(Vec3(*coordinates), plot.item)
                # Terraform only for buildings & roads, to save resources and for it to look more natural with terrain.
                # terraform_house_plot(mc, coordinates, coordinates[0] + 15, coordinates[2] + 15)
            elif plot.plot_type == PlotType.MISC:
                misc_builder.build(plot.item, *coordinates)
            elif plot.plot_type == PlotType.ROAD:
                # terraform_road_plot(mc, coordinates, coordinates[0] + 15, coordinates[2] + 15)
                if plot.entrance is True:
                    entrance_location = _transform_to_entrance_coords(*coordinates)

                plot.build_road(mc, fixed_ordinates[i][j])

    return entrance_location


def _transform_to_entrance_coords(x, y, z):
    return x + 7.5, y, z + 7.5


# Generates a 3-way nested list and tuple structure, such that the innermost structure is a tuple containing
# the x, y and z for a particular plot's leftmost corner block.
def _generate_fixed_ordinates(max_z: int, max_x: int, x_coord: int, y_coord: int, z_coord: int, ) -> list:
    temp = []
    for z in range(0, max_z + 1):
        temp.append([])
        for x in range(0, max_x + 1):
            temp[z].append((x_coord + x * 15, y_coord, z_coord + z * 15))
            
    return temp
