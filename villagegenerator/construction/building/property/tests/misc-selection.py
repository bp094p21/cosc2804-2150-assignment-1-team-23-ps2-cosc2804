import random

class Misc:
    TYPES = {
    'medi': [],
    'magic': [],
    'modern': []
    }
    def __init__self():
        pass
    def build(self, theme):
        self.theme = theme
        self._select_misc_type(theme)
    def _select_misc_type(self, theme):
        self.type = random.choices(self.TYPES[theme])



