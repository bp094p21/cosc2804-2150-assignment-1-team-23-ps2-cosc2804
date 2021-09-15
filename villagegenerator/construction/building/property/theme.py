import random
def get_theme(theme):
    if theme == 'medi':
        return Mediterranean()
    elif theme == 'magic':
        return Magic()
class Theme:
    name = None
    options = {}
    def __init__(self):
        pass
    def _randomly_select_house_type(self):
        self.house_type = random.choice(HOUSE_TYPES[self.name])
        pass


class Mediterranean(Theme):
    def __init__(self):
        self.name = 'mediterranean'
        self._randomly_select_house_type()

class Magic(Theme):
    def __init__(self):
        self.name = 'magic'
        self.house_types = [
            'cottage',
            'dungeon',
            'witch_house'
        ]

class Modern(Theme):
    def __init__(self):
        self.name = 'modern'
        self.house_types = [
            'apartment',
            'double_story',
            'duplex'
        ]
        pass

HOUSE_TYPES = {
    'mediterranean': [
        'basic',
    ],
    'magic': [
        'cottage',
        'dungeon',
        'witch_house'
    ],
    'modern': [
        'apartment',
        'double_story',
        'duplex'
    ]
}


# TESTING
if __name__ == '__main__':
    theme = Mediterranean()
    print(theme.house_type)