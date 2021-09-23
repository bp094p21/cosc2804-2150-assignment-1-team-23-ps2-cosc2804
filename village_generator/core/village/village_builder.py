import random


import core.village_layout.predefined_layouts as pl

from core.village.village_size import VillageSize
from core.village_layout.layout import Layout
from core.village_layout.plot import PlotType
from core.terraform.terraformer import terraform_house_plot, terraform_road_plot, terraform_entire_land
from core.terraform.terrain_scanner import scan_terrain


# TODO: rewrite this function so that the if-else statements for checking size are only written once.
def build_village(size, location, biome, mc):
    # before layouts or anything is defined/built, scan land and then if appropriate, perform terraform.

    if not scan_terrain(mc, location, size):
        return

    # do not need the y-coordinate.
    location = (location[0], location[2])

    mc.postToChat('Generating village...')

    _define_layout(size, biome, mc)
    selected_template = _select_random_template(size)


    if size is VillageSize.SMALL:
        print('LOG >> BUILDING SMALL')
        entrance_location = _build_small(selected_template, mc, biome, *location)

    elif size is VillageSize.MEDIUM:
        entrance_location = _build_medium(selected_template, mc, biome, *location)
    else:
        entrance_location = _build_large(selected_template, mc, biome, *location)

    mc.player.setPos(entrance_location[0], entrance_location[1], entrance_location[2])
    mc.postToChat('Done. Welcome to your new village!')


def _define_layout(size, biome, mc):
    if len(Layout.layouts[size]) == 2:
        return

    if size is VillageSize.SMALL:
        pl.define_small(mc, biome, size)
    elif size is VillageSize.MEDIUM:
        pl.define_medium(mc, biome, size)
    else:
        pl.define_large(mc, biome, size)


def _select_random_template(size):
    return random.choice(Layout.layouts[size]).grid


def _build_small(template, mc, biome, x, z):
    length_z = 5
    length_x = 4

    max_z = z + 15 * length_z
    max_x = x + 15 * length_x
    max_y, min_y = mc.getHighestAndLowestYInRegion(x, z, max_x, max_z)

    terraform_entire_land(mc, biome, x, min_y, z, max_x, max_y, max_z)

    return _build_plots(_generate_fixed_ordinates(length_z, length_x, x, min_y, z), template, mc)


def _build_medium(template, mc, biome, x, z):
    length_z = 6
    length_x = 5

    max_z = z + 15 * length_z
    max_x = x + 15 * length_x
    max_y, min_y = mc.getHighestAndLowestYInRegion(x, z, max_x, max_z)

    terraform_entire_land(mc, biome, x, min_y, z, max_x, max_y, max_z)
    return _build_plots(_generate_fixed_ordinates(length_z, length_x, x, min_y, z), template, mc)


def _build_large(template, mc, biome, x, z):
    length_z = 7
    length_x = 6

    max_z = z + 15 * length_z
    max_x = x + 15 * length_x
    max_y, min_y = mc.getHighestAndLowestYInRegion(x, z, max_x, max_z)

    terraform_entire_land(mc, biome, x, min_y, z, max_x, max_y, max_z)
    return _build_plots(_generate_fixed_ordinates(length_z, length_x, x, min_y, z), template, mc)


def _build_plots(fixed_ordinates, template, mc):
    entrance_location = None

    print(template)
    for (i, row) in enumerate(template):
        for (j, plot) in enumerate(row):

            print(i, plot, plot.plot_type)

            #Set the y-coords to be dynamic.
            coordinates = fixed_ordinates[i][j]
            
            if plot.plot_type == PlotType.HOUSE:
                #_update_variable_house_height(coordinates, mc)
                # terraform only for buildings & roads, to save resources and for it to look more natural with terrain.
                #terraform_house_plot(mc, coordinates, coordinates[0] + 15, coordinates[2] + 15)
                plot.item.set_location(coordinates)
                plot.build_house()
            elif plot.plot_type == PlotType.MISC:
                plot.build_misc(coordinates)
            elif plot.plot_type == PlotType.ROAD:
                #terraform_road_plot(mc, coordinates, coordinates[0] + 15, coordinates[2] + 15)

                if plot.entrance is True:
                    entrance_location = _transform_to_entrance_coords(*coordinates)

                plot.build_road(mc, fixed_ordinates[i][j])


    return entrance_location


# # TODO: finish and test.
# def _update_variable_house_height(house_location, mc):
#     highest_peak = mc.getHeight(house_location[0], house_location[2])

#     # if the peak is really high up (5 blocks+) then flatten it a bit.
#     # or maybe just let it be high up, and have the roads steeper.
#     # or better yet, with the terraformer, make it clear the land so that the increments of height are shallow and not
#     # super steep. So only increments by 1 at a time, with minimum distance of 2 blocks from the previous level
#     # to the next level. That way it is guaranteed to fit flush. This is a secondary measure.

#     if highest_peak - house_location[1] > 4:
#         # implement some sort of land smoother/flattener/brush tool that will smooth out the land and make it more real.
#         pass

#     house_location[1] = house_location[1] + highest_peak


def _transform_to_entrance_coords(x, y, z):
    return x + 7.5, y, z + 7.5


def _generate_fixed_ordinates(max_z: int, max_x: int, x_coord: int, y_coord: int, z_coord: int, ) -> list:
    temp = []
    print('LOG >> GENERATING FIXED ORDINATES')
    for z in range(0, max_z + 1):
        temp.append([])
        print('LOG >> CREATING NEW ROW OF FIXED ORDINATES')
        for x in range(0, max_x + 1):
            temp[z].append([x_coord + x * 15, y_coord, z_coord + z * 15])
    print('LOG >> FIXED ORDINATES COMPLETE')
    return temp

#      [(X, Y, Z), (X + 15, Y, Z), (X + 30, Y, Z), (X + 45, Y, Z), (X + 60, Y, Z),
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
