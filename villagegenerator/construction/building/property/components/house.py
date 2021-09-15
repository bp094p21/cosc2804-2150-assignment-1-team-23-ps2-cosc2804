from components.component import Component
import block as b
from mcpi import vec3 as v

class House:
    type = None
    components = {}
    def __init__(self, components):
        self.components = components

# Mediterranean Theme
class Basic(House):
    type = 'basic'

# Magic Theme
class Cottage(House):
    type = 'cottage'
class Dungeon(House):
    type = 'dungeon'
class WitchHouse(House):
    type = 'witch_house'

# Modern Theme
class Apartment(House):
    type = 'apartment'
class DoubleStory(House):
    type = 'double_story'
class Duplex(House):
    type = 'duplex'
