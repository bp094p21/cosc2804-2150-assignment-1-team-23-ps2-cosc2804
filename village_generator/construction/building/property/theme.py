import random

def get_theme(theme):
    if theme == 'medi':
        return Mediterranean()
    elif theme == 'magic':
        return Magic()
    elif theme == 'modern':
        return Modern()

class Theme:
    name: str = None
    house_type: str = None
    def __init__(self):
        self._randomly_select_house_type()
    def _randomly_select_house_type(self):
        self.house_type = random.choice(HOUSE_TYPES[self.name])
class Mediterranean(Theme):
    name = 'medi'
class Magic(Theme):
    name = 'magic'
class Modern(Theme):
    name = 'modern'

HOUSE_TYPES = {
    'medi': [
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
    theme_str = 'medi'
    theme_obj = get_theme(theme_str)
    print(type(theme_obj))
    print(theme_obj.house_type)