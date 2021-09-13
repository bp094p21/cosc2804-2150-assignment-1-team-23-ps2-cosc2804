from numpy import np
from villagegenerator.core.village.village_size import VillageSize


class Layout:
    layouts = {VillageSize.SMALL: [],
               VillageSize.MEDIUM: [],
               VillageSize.LARGE: []}

    def __init__(self, layout_size, layout_data):
        matrix = np.array(layout_data)
        self.grid = matrix
        self.size = layout_size

        Layout.layouts[layout_size].append(self)  # add the layout as a matrix to the static layouts dict.

# contains a numpy matrix and a bunch of methods for manipulating a particular layout, so that they can just be called.
