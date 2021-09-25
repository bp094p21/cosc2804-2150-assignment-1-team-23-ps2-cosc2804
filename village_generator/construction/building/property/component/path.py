from components.component import Component
import block as b


class Path(Component):
    # Class attributes
    type: str = 'path'
    # Instance attributes
    start_v3 = None
    end_v3: int = None
    block: b.Block = None

    def __repr__(self):
        return f"🖨  Printing object.__repr__:\n\n{type(self)}\start_v3: {self.start_v3},\nend_v3: {self.end_v3}," \
               f"\nblock: {self.block}\n"

    def __init__(self, start_v3, end_v3, path_block):
        self.start_v3 = start_v3
        self.end_v3 = end_v3
        self.block = path_block


# TESTING
if __name__ == '__main__':
    from mcpi import minecraft as m

    mc = m.Minecraft.create()
    player_v3 = mc.player.getPos()
    orientation = 0
    entrance = Path(start_V3=player_v3, end_v3=player_v3, door_block=b.COBBLESTONE)
