class House:
    type = None
    def __init__(self):
       pass 

# Basic Theme
class Cabin(House):
    def __init__(self):
        self.type = 'cabin'
class Simpleton(House):
    def __init__(self):
        self.type = 'simpleton'
class Tent(House):
    def __init__(self):
        self.type = 'tent'

# Magic Theme
class Cottage(House):
    def __init__(self):
        self.type = 'cottage'
class Dungeon(House):
    def __init__(self):
        self.type = 'dungeon'
class WithHouse(House):
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
