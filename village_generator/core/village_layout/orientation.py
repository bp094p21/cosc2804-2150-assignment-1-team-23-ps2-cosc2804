from enum import Enum

"""The orientation of each plot's entrance. Depending on the selected orientation, the houses will be facing this 
direction. """


class Orientation(Enum):
    WEST = 0
    NORTH = 1
    EAST = 2
    SOUTH = 3
