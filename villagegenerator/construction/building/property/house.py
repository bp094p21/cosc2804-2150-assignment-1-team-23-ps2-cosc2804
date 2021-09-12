class House:
    type = None
    def __init__(self):
       pass 

class SingleStory(House):
    def __init__(self):
        self.type = 'Single Story House'

class DoubleStory(House):
    def __init__(self):
        self.type = 'Double Story House'

class Unit(House):
    def __init__(self):
        self.type = 'Unit'

class Apartment(House):
    def __init__(self):
        self.type = 'Apartment'