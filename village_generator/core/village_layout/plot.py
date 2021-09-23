from enum import Enum
#from construction import Architect, MiscBuilder
from construction import MiscBuilder


# contains the orientation, position and centre of where the construction(s) and road(s) should go.
# this is passed down to the construction/road classes, so that they can position themselves accordingly.
class Plot:
    def __init__(self, item=None, entrance=False):
        if item is None:
            self.plot_type = PlotType.EMPTY
        #elif type(item) is Architect:
            #self.plot_type = PlotType.HOUSE
        elif type(item) is MiscBuilder:
            self.plot_type = PlotType.MISC
        else:
            self.plot_type = PlotType.ROAD
        self.item = item
        # delineates whether this plot will be village entrance
        self.entrance = entrance

    # called to construct each house when iterating through the predefined village_layout.
    def build_house(self):
        self.item.build()

    def build_misc(self, coords):
        self.item.build(*coords)

    # called to construct each road when iterating through the predefined village_layout.
    def build_road(self, mc, coords):
        self.item(mc, *coords)


class PlotType(Enum):
    EMPTY = 0
    HOUSE = 1
    MISC = 2
    ROAD = 3
