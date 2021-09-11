from numpy import np
from villagegenerator.core.village.village_size import VillageSize as size


class Layout:
    layouts = {size.SMALL: [],
               size.MEDIUM: [],
               size.LARGE: []}

    def __init__(self, layout_size, layout_data):
        matrix = np.array(layout_data)
        self.grid = matrix
        self.size = layout_size

        Layout.layouts[layout_size].append(matrix)  # add the layout as a matrix to the static layouts dict.

# contains a numpy matrix and a bunch of methods for manipulating a particular layout, so that they can just be called.
