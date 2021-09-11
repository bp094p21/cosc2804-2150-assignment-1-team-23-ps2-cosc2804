import floor, front, house, pool, roof, room, wall
from villagegenerator.construction.building.building import Building


class Property(Building):
    roadside_matrix_el = None

    def __init__(self, x, y, z, matrix_pos, ):
        pass

    # put whatever you need here to build a parkpond object. this will ultimately be the method that is called from the
    # framework.
    def build(self):
        pass
