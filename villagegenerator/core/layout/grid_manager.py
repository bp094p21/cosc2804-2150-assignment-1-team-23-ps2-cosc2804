# module providing a set of useful functions to manage the incrementing/decrementing of the grid system.

# todo - impure functions. revise this setup, as it is not going to be thread-safe nor practical for testing.
# TODO - only need to have a quick way of incrementing/setting the z coordinate for the different sizes and layouts.

class GridManager:
    instance = None
    _x = 0
    z = 0

    def __init__(self, x, z):
        GridManager._x = x
        GridManager.z = z
        # raise Exception('You cannot instantiate the GridManager via the constructor!\nUse the static factory.')

    @staticmethod
    def instantiate(x: int, z: int):
        if GridManager.instance is None:
            GridManager.instance = GridManager(x, z)

        return GridManager.instance

    @staticmethod
    def increment_z():
        GridManager.z += 15

