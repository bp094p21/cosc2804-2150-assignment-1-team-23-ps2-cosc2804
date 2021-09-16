from enum import Enum

from villagegenerator.construction.building.building import Building


# contains the orientation, position and centre of where the construction(s) and road(s) should go.
# this is passed down to the construction/road classes, so that they can position themselves accordingly.
class Plot:
    def __init__(self, item=None, entrance=False):
        self.plot_type = PlotType.EMPTY if item is None else (
            PlotType.BUILDING if item is type(Building) else PlotType.ROAD)
        self.item = item
        # delineates whether this plot will be village entrance
        self.entrance = entrance

    # called to construct each house when iterating through the predefined layout.
    def build_house(self):
        self.item.build()

    # called to construct each road when iterating through the predefined layout.
    def build_road(self, mc, coords):
        self.item(mc, *coords)


class PlotType(Enum):
    EMPTY = 0
    BUILDING = 1
    ROAD = 2
