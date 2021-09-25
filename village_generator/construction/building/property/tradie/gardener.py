import random

if __name__ == '__main__':
    from tradie import Tradie
else:
    from tradies.tradie import Tradie


class Gardener(Tradie):
    trade = 'gardening'
    trees = []
    veggie_patches = []
    flower_beds = []

    def __init__(self):
        pass

    # External calls
    def build_component(self, component, mc):
        if component.type == 'flower_bed':
            self.flower_beds.append(component)
            self._build_flower_bed(component, mc)
        if component.type == 'veggie_patch':
            self.veggie_patches.append(component)
            self._build_veggie_patch(component, mc)
        if component.type == 'tree':
            self.trees.append(component)
            self._build_tree(component, mc)

    # Internal Methods
    def _build_flower_bed(self, component, mc):
        x, y, z = component.v3
        self._build_plant_case(x, y, z, mc)
        mc.setBlocks(x, y, z, x + 1, y, z + 1, 2)
        # mc.setBlocks(x,y+1,z,x+1,y+1,z+1,175)
        # mc.setBlocks(x,y+2,z,x+1,y+2,z+1,175)
        for i in range(2):
            mc.setBlock(x + i, y + 1, z + i, 38, random.randint(0, 8))
            mc.setBlock(x + 1 - i, y + 1, z + i, 38, random.randint(0, 8))

    def _build_veggie_patch(self, component, mc):
        x, y, z = component.v3
        mc.setBlocks(x, y, z, x + 1, y, z + 1, 60)
        self._build_plant_case(x, y, z, mc)
        for i in range(2):
            mc.setBlocks(x + i, y + 1, z + i, x + i, y + 1, z + i, 142)
            mc.setBlocks(x + 1 - i, y + 1, z + i, x + 1 - i, y + 1, z + i, 141)

    def _build_plant_case(self, x, y, z, mc):
        mc.setBlocks(x - 1, y, z, x - 1, y, z + 1, 167, 6)
        mc.setBlocks(x + 2, y, z, x + 2, y, z + 1, 167, 7)
        mc.setBlocks(x, y, z - 1, x + 1, y, z - 1, 167, 12)
        mc.setBlocks(x, y, z + 2, x + 1, y, z + 2, 167, 13)

    def _build_tree(self, component, mc):
        x, y, z, = component.v3
        y -= 1
        dirt = 3
        height = random.randint(8, 11)
        foliage_height = random.randint(3, 5)
        trunk_block = component.trunk_block
        leaves_block = component.leaves_block
        mc.setBlock(x, y, z, dirt)
        mc.setBlocks(x, y + 1, z, x, y + height, z, trunk_block)
        mc.setBlocks(x - 3, y + height, z - 3, x + 3, y + height + foliage_height, z + 3, leaves_block)
        pass


# TESTING

if __name__ == '__main__':
    import sys

    sys.path.append('../property')
    from components import tree as t
    from components import veggie_patch as v
    from components import flower_bed as f
    from mcpi import minecraft

    mc = minecraft.Minecraft.create()
    # start_v3 = mc.player.getPos()
    # Assign below variables for testing
    end_v3 = None
    end_v3 = None
    trunk_block = None
    leaves_block = None

    x, y, z, = mc.player.getPos()
    gardener = Gardener()
    gardener._build_vege_patch(x, y, z, mc)
    gardener._build_flower_bed(x + 4, y, z, mc)
