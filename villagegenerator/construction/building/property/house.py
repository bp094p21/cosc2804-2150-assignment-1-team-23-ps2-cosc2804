class House:
    type = None
    def __init__(self):
       pass 

class SingleStory(House):
    def __init__(self):
        self.type = 'single_story'

class DoubleStory(House):
    def __init__(self):
        self.type = 'double_story'

class Unit(House):
    def __init__(self):
        self.type = 'unit'

class Apartment(House):
    def __init__(self):
        self.type = 'apartment'