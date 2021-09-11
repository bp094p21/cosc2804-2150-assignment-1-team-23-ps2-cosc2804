from villagegenerator.structure.property import property


# contains the orientation, position and centre of where the structure(s) and road(s) should go.
# this is passed down to the structure/road classes, so that they can position themselves accordingly.
class Plot:
    def __init__(self, item):
        self.item = item

    # called to build each house/road when iterating through the predefined layout.
    def build(self):
        # if its a property, invoke the build method.
        if type(self.item) is type(property):
            self.item.build()
            return

        # if its a road, call the function as is.
        self.item()
