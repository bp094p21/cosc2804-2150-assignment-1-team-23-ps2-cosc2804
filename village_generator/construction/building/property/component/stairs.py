from components.component import Component


class Stairs(Component):
    type = 'stairs'
    start_v3 = None
    orientation = None

    def __init__(self, start_v3, orientation, block_up, block_down):
        self.start_v3 = start_v3
        self.block_up = block_up
        self.block_down = block_down
        self.orientation = orientation