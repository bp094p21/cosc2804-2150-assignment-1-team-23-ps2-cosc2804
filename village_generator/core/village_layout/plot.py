from enum import Enum
from construction import House, Misc

"""A data class containing a particular type of first-class citizen (road, house or misc function/object), and the type the plot contains.
This represents the atomic unit of each item within a template and is how each block of land will be represented. Each plot is 15x15 in dimensions."""


class Plot:
    def __init__(self, item=None, entrance=False):
        if item is None:
            self.plot_type = PlotType.EMPTY
        elif type(item) is House:
            self.plot_type = PlotType.HOUSE
        elif type(item) is Misc:
            self.plot_type = PlotType.MISC
        else:
            self.plot_type = PlotType.ROAD

        self.item = item
        # Delineates whether this plot will be the village entrance
        self.entrance = entrance

    # Called to construct each misc building when iterating through the predefined village_layout.
    def build_misc(self, coords):
        self.item.build(*coords)

    # Called to construct each road when iterating through the predefined village_layout.
    def build_road(self, mc, coords):
        self.item(mc, *coords)


"""An enum representing the type of Plot, so that it can be easily identified throughout the code."""


class PlotType(Enum):
    EMPTY = 0
    HOUSE = 1
    MISC = 2
    ROAD = 3
