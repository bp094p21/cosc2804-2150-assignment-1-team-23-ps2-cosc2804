from enum import Enum

from villagegenerator.construction.building.building import Building


# contains the orientation, position and centre of where the construction(s) and road(s) should go.
# this is passed down to the construction/road classes, so that they can position themselves accordingly.
class Plot:
    def __init__(self, item=None):
        self.plot_type = PlotType.EMPTY if item is None else (
            PlotType.BUILDING if item is type(Building) else PlotType.ROAD)
        self.item = item

    # called to construction each house/road when iterating through the predefined layout.
    def build(self):
        # if its a property, invoke the construction method.
        if type(self.item) is type(Building):
            self.item.build()
            return

        # if its a road, call the function as is.
        self.item()


class PlotType(Enum):
    EMPTY = 0
    BUILDING = 1
    ROAD = 2
