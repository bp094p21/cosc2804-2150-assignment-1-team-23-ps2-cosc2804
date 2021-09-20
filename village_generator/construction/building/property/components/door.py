from components.component import Component
import block as b

class Door(Component):
    # Class attributes
    type: str = 'door'
    # Instance attributes
    root_v3 = None
    orientation: int = None
    door_block: b.Block = None
    def __repr__(self):
        return f"🖨  Printing object.__repr__:\n\n{type(self)}\nroot_v3: {self.root_v3},\norientation: {self.orientation},\ndoor_block: {self.door_block}\n"
    def __init__(self, root_v3, orientation, door_block):
        self.root_v3 = root_v3
        self.orientation = orientation
        self.door_block = door_block

# TESTING
if __name__ == '__main__':
    from mcpi import minecraft as m
    mc = m.Minecraft.create()
    player_v3 = mc.player.getPos()
    orientation = 0
    entrance = Door(root_v3=player_v3, orientation=0, door_block=b.AIR)
    pass
	