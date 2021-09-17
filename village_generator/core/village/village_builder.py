import random
import core.village_layout.predefined_layouts as pl

from core.village.village_size import VillageSize
from core.village_layout.layout import Layout
from core.village_layout.plot import PlotType
from core.terraform.terrain_scanner import scan_terrain


def build_village(size, location, biome, mc):
    # before layouts or anything is defined/built, scan land and then if appropriate, perform terraform.

    if not scan_terrain(mc, location, size):
        return
    
    mc.postToChat('Generating village...')
    _define_layout(size, biome, mc)
    selected_template = _select_random_template(size)

    if size is VillageSize.SMALL:
        entrance_location = _build_small(location, selected_template, mc)

    elif size is VillageSize.MEDIUM:
        entrance_location = _build_medium(location, selected_template, mc)
    else:
        entrance_location = _build_large(location, selected_template, mc)

    entity_ids = mc.getPlayerEntityIds()
    print(entrance_location)
    #mc.player.setTilePos(entity_ids[0], entrance_location[0], entrance_location[1], entrance_location[2])
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


def _build_small(location, template, mc):
    return _build_plots(_generate_fixed_ordinates(5, 4, *location), template, mc)


def _build_medium(location, template, mc):
    return _build_plots(_generate_fixed_ordinates(6, 5, *location), template, mc)


def _build_large(location, template, mc):
    return _build_plots(_generate_fixed_ordinates(7, 6, *location), template, mc)


def _build_plots(fixed_ordinates, template, mc):
    entrance_location = None

    print(template)
    for (i, row) in enumerate(template):
        for (j, plot) in enumerate(row):
            print(i, plot, plot.plot_type)
            if plot.plot_type == PlotType.BUILDING:
                plot.item.set_location(fixed_ordinates[i][j])
                plot.build_house()
            elif plot.plot_type == PlotType.ROAD:
                if plot.entrance is True:
                    entrance_location = _transform_to_entrance_coords(*fixed_ordinates[i][j])
                plot.build_road(mc, fixed_ordinates[i][j])

    return entrance_location


def _transform_to_entrance_coords(x, y, z):
    return x + 7.5, y, z + 7.5


def _generate_fixed_ordinates(max_z: int, max_x: int, x_coord: int, y_coord: int, z_coord: int) -> list:
    temp = []
    for z in range(0, max_z + 1):
        temp.append([])
        for x in range(0, max_x + 1):
            temp[z].append((x_coord + x * 15, y_coord, z_coord + z * 15))

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
