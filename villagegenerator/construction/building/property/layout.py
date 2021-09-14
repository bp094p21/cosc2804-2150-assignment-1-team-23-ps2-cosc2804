from mcpi import vec3
def get_layout(house_type):
    if house_type == 'basic':
        return Basic()
    elif house_type == 'dungeon':
        return PoolSide()
class Layout:
    name = ''
    def __init__(self, name = 'basic'):
        if name == 'basic':
            pass
class Basic(Layout):
    def __init__(self):
        self.name = 'basic'
        self.boundary = {
            'start': {
                'z': 0,
                'x': 0
            },
            'end': {
                'z': 14,
                'x': 14
            }
        }
        self.entrance = {
            'start': {
                'z': 0,
                'x': 0
            },
            'end': {
                'z': 0,
                'x': 14
            }
        }
        self.front = {
            'start': {
                'z': 1,
                'x': 1
            },
            'end': {
                'z': 3,
                'x': 14
            }
        }
        self.house = {
            'start': {
                'z': 4,
                'x': 3
            },
            'end': {
                'z': 10,
                'x': 11
            }
        }
        self.sides = [
            {
                'start': {
                    'z': 4,
                    'x': 1
                },
                'end': {
                    'z': 10,
                    'x': 2
                }
            },
            {
                'start': {
                    'z': 4,
                    'x': 12
                },
                'end': {
                    'z': 10,
                    'x': 13
                }
            }
        ]
        self.back = {
            'start': {
                'z': 11,
                'x': 1
            },
            'end': {
                'z': 13,
                'x': 13
            }
        }
        self.pool = {
            'start': {
                'z': 11,
                'x': 1
            },
            'end': {
                'z': 13,
                'x': 4
            }
        }
class PoolSide(Layout):
    def __init__(self):
        self.name = 'pool_side'
        self.boundary = {
            'start': {
                'z': 0,
                'x': 0
            },
            'end': {
                'z': 14,
                'x': 14
            }
        }
        self.entrance = {
            'start': {
                'z': 0,
                'x': 0
            },
            'end': {
                'z': 0,
                'x': 14
            }
        }
        self.front = {
            'start': {
                'z': 1,
                'x': 1
            },
            'end': {
                'z': 4,
                'x': 13
            }
        }
        self.house = {
            'start': {
                'z': 5,
                'x': 1
            },
            'end': {
                'z': 13,
                'x': 6
            }
        }
        self.sides = [
            {
                'start': {
                    'z': 5,
                    'x': 7
                },
                'end': {
                    'z': 13,
                    'x': 13
                }
            }
        ]
        self.back = None
        self.pool = {
            'start': {
                'z': 6,
                'x': 8
            },
            'end': {
                'z': 12,
                'x': 12
            }
        }

# TESTING

if __name__ == '__main__':
    layout = Basic()
    print(f'Entrance starting point:')
    print(f'z: {layout.entrance["start"]["z"]}')
    print(f'x: {layout.entrance["start"]["x"]}')
    print(f'\nEntrance end point:')
    print(f'z: {layout.entrance["end"]["z"]}')
    print(f'z: {layout.entrance["end"]["x"]}')