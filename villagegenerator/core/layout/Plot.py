# contains the orientation, position and centre of where the structure(s) and road(s) should go.
# this is passed down to the structure/road classes, so that they can position themselves accordingly.
class Plot:
    def __init__(self, contained):
        self.contained = contained

    # called to build each house/road when iterating through the predefined layout.
    def build(self):
        pass
