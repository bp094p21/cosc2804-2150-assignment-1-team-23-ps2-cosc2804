class House:
    theme = None
    type = None
    def __init__(self):
       pass 

# Mediterranean Theme
class Basic(House):
    def __init__(self):
        self.type = 'basic'

# Magic Theme
class Cottage(House):
    def __init__(self):
        self.type = 'cottage'
class Dungeon(House):
    def __init__(self):
        self.type = 'dungeon'
class WitchHouse(House):
    def __init__(self):
        self.type = 'witch_house'

# Modern Theme
class Apartment(House):
    def __init__(self):
        self.type = 'apartment'
class DoubleStory(House):
    def __init__(self):
        self.type = 'double_story'
class Duplex(House):
    def __init__(self):
        self.type = 'duplex'
