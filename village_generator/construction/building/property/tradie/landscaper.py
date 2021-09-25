if __name__ == '__main__':
    from tradie import Tradie
else:
    from tradies.tradie import Tradie


class Landscaper(Tradie):
    trade = 'landscaping'
    paths = []
    foundations = []

    # External calls
    def build_component(self, component, mc):
        if component.type == 'path':
            self.paths.append(component)
            self._build_path(component, mc)

    # Internal Methods
    def _build_path(self, path, mc):
        start_v3 = path.start_v3
        end_v3 = path.end_v3
        block = path.block
        self._fill(start_v3, end_v3, block, mc)


class Lance(Landscaper):
    name = 'Lance'


# TESTING

if __name__ == '__main__':
    pass
    # import sys
    # sys.path.append('../property')
    # from component import floor as f
    # from mcpi import minecraft
    # mc = minecraft.Minecraft.create()
    # v3 = mc.player.getPos()
    # floor = f.Floor(v3)
    # floor_guy = Freddie()
    # floor_guy.build_component(floor, mc)
    # print(dir())
