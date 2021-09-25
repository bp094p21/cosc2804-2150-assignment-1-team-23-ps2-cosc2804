import random
from .misc import Misc
from .block_list import MISC_BLOCKS


class BigTree(Misc):
    def __init__(self, biome, mc):
        super().__init__(biome, mc)
        self.height = random.randint(2, 25)

        if self.theme == 'medi':
            self.wood = (162, 1)
            self.leaves = (161, 1)
        else:
            self.wood = MISC_BLOCKS[self.theme]['plant_stem']
            self.leaves = MISC_BLOCKS[self.theme]['plant_leaves']

    def big_tree_build(self, x, y, z):
        self.build_foundation(x, y, z)
        self.mc.setBlocks(x + 3, y + self.height, z + 3, x + 11, y + self.height + 5, z + 11, self.leaves)
        self.mc.setBlocks(x + 6, y, z + 6, x + 8, y + self.height + 3, z + 8, self.wood)

    def big_branches(self, x, y, z):
        for i in range(3):
            self.mc.setBlocks(x + 6 + i, y + self.height / 2, z + 2 + i, x + 8 - i, y + self.height / 2 - i, z + 5,
                              self.leaves)
            self.mc.setBlocks(x + 6 + i, y + self.height / 3, z + 10 - i, x + 8, y + self.height / 3 - i, z + 12 - i,
                              self.leaves)
            self.mc.setBlocks(x + 8, y + self.height / 4, z + 7 + i, x + 12 - i, y + self.height / 4 - i, z + 9 - i,
                              self.leaves)
            self.mc.setBlocks(x + 3 + i, y + self.height / 1.5, z + 6 + i, x + 5, y + self.height / 1.5 - i, z + 9 - i,
                              self.leaves)  # make leaves go down y axis and shrink by oneblock

    def build(self, x, y, z):
        self.big_tree_build(x, y, z)
        self.big_branches(x, y, z)
        self.build_tree(x, y, z)
