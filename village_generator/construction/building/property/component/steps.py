from components.component import Component


class Steps(Component):
    type = 'steps'

    def __init__(self, v3, block):
        self.v3 = v3
        self.block = block
