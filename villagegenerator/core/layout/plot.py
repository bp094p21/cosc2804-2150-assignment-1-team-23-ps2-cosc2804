from villagegenerator.structure.building.property import property


# contains the orientation, position and centre of where the construction(s) and road(s) should go.
# this is passed down to the construction/road classes, so that they can position themselves accordingly.
class Plot:
    def __init__(self, item):
        self.item = item

    # called to construction each house/road when iterating through the predefined layout.
    def build(self):
        # if its a property, invoke the construction method.
        if type(self.item) is type(property):
            self.item.build()
            return

        # if its a road, call the function as is.
        self.item()
