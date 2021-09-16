from components.component import Component
import block as b
from mcpi import vec3 as v

class House:
    components = {}
    def __init__(self, components={}):
        self.components = components
