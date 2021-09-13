class Theme:
    name = None
    options = {}
    def __init__(self):
        pass

class Basic(Theme):
    def __init__(self):
        self.name = 'basic'
        self.options['house'] = []

        

class Magic(Theme):
    def __init__(self):
        type = 'magic'

class Modern(Theme):
    def __init__(self):
        type = 'modern'