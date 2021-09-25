from .misc import Misc
from .block_list import MISC_BLOCKS


class ChessBoard(Misc):
    def __init__(self, biome, mc):
        super().__init__(biome, mc)
        self.back_piece = 198
        self.front = 140

    def build(self, x, y, z):
        self.build_foundation(x, y, z)
        self.mc.setBlocks(x + 3, y, z + 3, x + 11, y, z + 11, MISC_BLOCKS[self.theme]['ground_base'])
        counter = 0
        for i in range(9):
            for j in range(9):
                if counter % 2 == 1:
                    self.mc.setBlocks(x + i + 3, y, z + j + 3, x + i + 3, y, z + j + 3,
                                      MISC_BLOCKS[self.theme]['main_light_block'])
                counter += 1
        self.mc.setBlocks(x + 3, y + 1, z + 3, x + 11, y + 1, z + 11, self.back_piece)
        self.mc.setBlocks(x + 4, y + 1, z + 3, x + 10, y + 1, z + 11, self.front)
        self.mc.setBlocks(x + 5, y + 1, z + 3, x + 9, y + 1, z + 11, self.air)
        self.build_tree(x, y, z)
