# Mediterranean, Magic, Modern
import block as b

class BlockList:
    def __init__(self):
        pass
    def setBlockList(self):
        pass


class Mediterranean(BlockList):
    blocklist = {
        'ground': [b.GRASS_PATH, b.SOUL_SAND],
        'tree_trunk': [b.TIMBER_LOG]
    }
    pass


class Misc:
    def __init__(self, biome=0):
        self.biome = biome
        print(1)
        # DO STUFF
        pass
    def basic(self):
        print(2)
        pass
    def build(self, biome):
        if biome == 'dessert':
            blocklist = Mediterranean()
            ground_block_array = blocklist['ground']
    def setGroundBlock(self):
        pass


class Park(Misc):
    # def basic(self):
    #     print(3)
    components = {
        'trees': [tree],
        'main_footpath': None,
        'benches': [],

    }
    def basic(self):
        print('overwrote basic')
    pass 

class Statue(Misc):
    pass

class Tree(Misc):
    pass

park = Park()
park.basic()