from tradies.tradie import Tradie

class Tiler(Tradie):
    trade = 'tiling'
    def __init__(self):
        pass
    def build_component(component, mc):
        pass

class Theo(Tiler):
    designs = {
        '235': {
            (2, 4): [
                [3, 0, 1, 2, 0, 3, 2, 1],
                [0, 3, 2, 1, 3, 0, 1, 2]
            ],
            (4, 2): [
                [3, 1, 0, 2, 0, 2, 3, 1],
                [0, 2, 3, 1, 3, 1, 0, 2]
            ]
        },
        '236': [],
    }

    pass

class Tessa(Tiler):
    designs = {
        '238': [],

    }


# TESTING
if __name__ == '__main__':
    from mcpi import minecraft
    mc = minecraft.Minecraft.create()
    v3 = mc.player.getPos()
    tiler = Theo()
    print(tiler.designs['235'][(2,4)])