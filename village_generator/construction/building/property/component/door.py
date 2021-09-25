from .component import Component
from construction.building.property.block import Block


class Door(Component):
    # Class attributes
    type: str = 'door'
    # Instance attributes
    v3 = None
    orientation: int = None
    top_block: Block = None
    bot_block: Block = None

    def __repr__(self):
        return f"🖨  Printing object.__repr__:\n\n{type(self)}\nv3: {self.v3},\norientation: {self.orientation}," \
               f"\ntop_block: {self.top_block}\nbot_block: {self.bot_block}\n"

    def __init__(self, v3, top_block, bot_block, orientation):
        self.v3 = v3
        self.top_block = top_block
        self.bot_block = bot_block
        self.orientation = orientation


# TESTING
if __name__ == '__main__':
    from mcpi import minecraft as m

    mc = m.Minecraft.create()
    player_v3 = mc.player.getPos()
    orientation = 0
