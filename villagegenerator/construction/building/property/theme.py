class Theme:
    name = None
    options = {}
    def __init__(self):
        pass

class Basic(Theme):
    def __init__(self):
        self.name = 'basic'
        self.house_types = [
            'simpleton',
            'tent',
            'cabin'
        ]

class Magic(Theme):
    def __init__(self):
        self.name = 'magic'
        self.house_types = [
            'witch_house',
            'cottage',
            'dungeon'
        ]

class Modern(Theme):
    def __init__(self):
        self.name = 'modern'
        self.house_types = [
            'double_story',
            'duplex',
            'apartment'
        ]