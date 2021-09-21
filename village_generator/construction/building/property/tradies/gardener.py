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
    def _build_flower_bed(self, flower_bed, mc):
        pass
    def _build_veggie_patch(self, flower_bed, mc):
        pass
    def _build_tree(self, flower_bed, mc):
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
    start_v3 = mc.player.getPos()
    # Assign below variables for testing
    end_v3 = None
    end_v3 = None
    trunk_block = None
    leaves_block = None

    tree = t.Tree(start_V3=start_v3, end_v3=end_v3, trunk_block=trunk_block, leaves_block=leaves_block)
    flower_bed = f.FlowerBed(start_V3=start_v3, end_v3=end_v3, trunk_block=trunk_block, leaves_block=leaves_block)
    veggie_patch = v.VeggiePatch(start_V3=start_v3, end_v3=end_v3, trunk_block=trunk_block, leaves_block=leaves_block)

    gardener = Gardener()
    gardener.build_components(tree, mc)