from .tradie import Tradie


class WindowMaker(Tradie):
    trade = 'windows'
    windows = []

    def __init__(self):
        pass

    # External calls
    def build_component(self, component, mc):
        self.windows.append(component)
        self._set_window(component, mc)

    # Internal Methods
    def _set_window(self, window, mc):
        self._one_block(window.v3, window.block, mc)
        pass


# TESTING

# if __name__ == '__main__':
#     import sys

#     sys.path.append('../property')
#     from components import wall as w
#     import block as b
#     from mcpi import minecraft

#     mc = minecraft.Minecraft.create()
#     start_v3 = mc.player.getPos()
#     print(dir())
