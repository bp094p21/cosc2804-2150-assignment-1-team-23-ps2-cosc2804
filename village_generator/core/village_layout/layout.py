import numpy as np
from core.village import VillageSize

"""A layout class representing an entire matrix of plots for a particular size. This is a data class at its finest, and it stores all layouts created, so that they can be cached
and inexpensively created later if need be  (memoization). This feature did not deem useful in the submission of this project, however, it would be useful if all the features were completed as 
intended."""

class Layout:
    layouts = {VillageSize.SMALL: [],
               VillageSize.MEDIUM: [],
               VillageSize.LARGE: []}

    def __init__(self, layout_size, layout_data):
        matrix = np.array(layout_data)
        self.grid = matrix
        self.size = layout_size

        Layout.layouts[layout_size].append(self)  # Add the village_layout as a matrix to the static layouts dict.