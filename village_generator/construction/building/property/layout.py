import random
from mcpi import vec3 as v

def get_layout(house_type, entrance_edge, orientation, plot_length):
    if house_type == 'basic':
        return Basic(entrance_edge, orientation, plot_length)
    elif house_type == 'poolside':
        return PoolSide(entrance_edge, orientation, plot_length)
    elif house_type == 'dungeon':
        return Dungeon(entrance_edge, orientation, plot_length)

class Layout:
    name = None
    emoji = '📍'
    layout = {}         
    def __init__(self):
        print(f"{self.emoji} Layout initialized.\n")
        if self.name:
            print(f"layout.name: {self.name}\n")

class Basic(Layout):
    name = 'basic'
    def __init__(self, entrance_edge, orientation, plot_length):
        self.entrance_edge = entrance_edge
        self.orientation = orientation
        self.plot_length = plot_length
        self._randomize_layout()
    def _print(self, item_name, item_properties):
        print(f"{item_name}\n")
        for k, v in item_properties.items():
            print(f"{k}: {v}")
        print()
    def _randomize_layout(self):
        self._position_pool()
        self._print('pool', self.layout['pool'])
        self._position_house()
        self._print('house', self.layout['house'])
        self._position_path()
        self._print('path', self.layout['path'])
        self._position_outdoor_features()
        for k, v in self.layout['outdoor_features'].items():
            self._print(k, v)
    def _position_pool(self):
        e_offset = None     # e_offset = offset into property from edge (+z for orientation 0)
        c_offset = None     # c_offset = offset from entrance corner to corner (+x for orientation 0)
        e_len = None        # e_len = length in e  direction
        c_len = None        # c_len = length in c direction
        positions = ['left', 'back', 'right']     # From perpsective of walking onto property from entrance
        random_position = random.choice(positions)
        if random_position == 'back':
            e_offset = 10
            e_len = self.plot_length - e_offset
            c_offsets = [1, 2, 3, 4]
            c_offset = random.choice(c_offsets)
            c_len = self.plot_length - (c_offset * 2)
        else:
            e_offsets = [7, 8]
            e_offset = random.choice(e_offsets)
            e_len = self.plot_length - e_offset - 1
            c_lens = [4, 5, 6]
            c_len = random.choice(c_lens)
            if random_position == 'right':
                c_offset = 1
            elif random_position == 'left':
                c_offset = self.plot_length - 1 - c_len
        self.layout['pool'] = {
            'position' : random_position,
            'e_offset': e_offset,
            'c_offset': c_offset,
            'e_len': e_len,
            'c_len': c_len
        }
    def _position_house(self):
        position = None
        e_offset = None
        c_offset = None
        e_len = None
        c_len = None

        pool_position = self.layout['pool']['position']
        if pool_position == 'back':
            position = 'middle'
            c_offsets = [2, 3]
            c_offset = random.choice(c_offsets)
            c_len = self.plot_length - (c_offset * 2)
            gap = 1
            e_len_pool = self.layout['pool']['e_len']
            e_offsets = [3,4]
            e_offset = random.choice(e_offsets)
            e_len = self.plot_length - e_offset - e_len_pool - gap 
        else:
            c_len_pool = self.layout['pool']['c_len']
            e_offsets = [6, 7]
            e_offset = random.choice(e_offsets)
            e_len = self.plot_length - e_offset - 1
            house_pool_gaps = [1, 2]
            gap = random.choice(house_pool_gaps)
            c_len = self.plot_length - c_len_pool - gap - 2
            c_offset_pool = self.layout['pool']['c_offset']
            if pool_position == 'right':
                position = 'left'
                c_offset = c_offset_pool + c_len_pool + gap
            elif pool_position == 'left':
                position = 'right'
                c_offset = 1
        self.layout['house'] = {
            'position' : position,
            'e_offset': e_offset,
            'c_offset': c_offset,
            'e_len': e_len,
            'c_len': c_len
        }
        
    def _position_path(self):
        e_offset = 1
        c_offset = self.plot_length // 2    # Always middle
        e_len = None
        c_len = 1        # Always 1 wide
        e_offset_house = self.layout['house']['e_offset']
        e_len = e_offset_house - e_offset
        self.layout['path'] = {
            'e_offset': e_offset,
            'c_offset': c_offset,
            'e_len': e_len,
            'c_len': c_len
        }
    def _position_external_doors(self):
        self._position_front_door()
        self._position_poolside_door()
        pass
    def _position_front_door(self):
        pass
    def _position_poolside_door(self):
        pass
    def _position_outdoor_features(self):
        e_offset_house = self.layout['house']['e_offset']
        feature_house_gaps = [1, 2]
        feature_house_gap = random.choice(feature_house_gaps)
        entrance_feature_gaps = [0, 1]
        entrance_feature_gap = random.choice(entrance_feature_gaps)
        e_len = e_offset_house - feature_house_gap - entrance_feature_gap - 1
        e_offset = 1 + entrance_feature_gap
        boundary_gaps = [0, 1]
        boundary_gap = random.choice(boundary_gaps)
        path_gaps = [0, 1]
        path_gap = random.choice(path_gaps)
        left_feature_option = [True, False]
        right_feature_option = [True, False]
        left_feature = random.choice(left_feature_option)
        right_feature = random.choice(right_feature_option)
        self.layout['outdoor_features'] = {}
        if left_feature:
            c_offset = self.layout['path']['c_offset'] + path_gap + 1
            self.layout['outdoor_features']['outdoor_feature_left'] = {
                'e_offset': e_offset,
                'c_offset': c_offset,
                'e_len': e_len,
                'c_len': self.plot_length - c_offset - boundary_gap - 1 - 1
            }
        if right_feature:
            c_offset = 1 + boundary_gap
            self.layout['outdoor_features']['outdoor_feature_right'] = {
                'e_offset': e_offset,
                'c_offset': c_offset,
                'e_len': e_len,
                'c_len': self.layout['path']['c_offset'] - path_gap - 1 - 1 - boundary_gap
            }


        
        pass


# class Basic(Layout):
#     def __init__(self):
#         self.name = 'basic'
#         self.boundary = {
#             'start': {
#                 'z': 0,
#                 'x': 0
#             },
#             'end': {
#                 'z': 14,
#                 'x': 14
#             }
#         }
#         self.entrance = {
#             'start': {
#                 'z': 0,
#                 'x': 0
#             },
#             'end': {
#                 'z': 0,
#                 'x': 14
#             }
#         }
#         self.front = {
#             'start': {
#                 'z': 1,
#                 'x': 1
#             },
#             'end': {
#                 'z': 3,
#                 'x': 14
#             }
#         }
#         self.house = {
#             'start': {
#                 'z': 4,
#                 'x': 3
#             },
#             'end': {
#                 'z': 10,
#                 'x': 11
#             }
#         }
#         self.sides = [
#             {
#                 'start': {
#                     'z': 4,
#                     'x': 1
#                 },
#                 'end': {
#                     'z': 10,
#                     'x': 2
#                 }
#             },
#             {
#                 'start': {
#                     'z': 4,
#                     'x': 12
#                 },
#                 'end': {
#                     'z': 10,
#                     'x': 13
#                 }
#             }
#         ]
#         self.back = {
#             'start': {
#                 'z': 11,
#                 'x': 1
#             },
#             'end': {
#                 'z': 13,
#                 'x': 13
#             }
#         }
#         self.pool = {
#             'start': {
#                 'z': 11,
#                 'x': 1
#             },
#             'end': {
#                 'z': 13,
#                 'x': 4
#             }
#         }
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
class Dungeon(Layout):
    pass

# TESTING

if __name__ == '__main__':
# def get_layout(house_type, entrance_edge, orientation, plot_length):
    house_type = 'basic'
    entrance_edge = {
        'start': v.Vec3(0, 0, 0),
        'end': v.Vec3(14, 0, 0)
    }
    orientation = 0
    plot_length = 15
    layout = get_layout(house_type, entrance_edge, orientation, plot_length)