import random

def get_layout(
    house_type: str,
    plot_length: int
    ) -> object:
    if house_type == 'basic':
        return Basic(plot_length)
    elif house_type == 'poolside':
        return PoolSide(plot_length)
    elif house_type == 'dungeon':
        return Dungeon(plot_length)
    return None

class Layout:
    """Returns object with a dictionary of layouts for some of the major property components such as pool, the house, paths etc. It takes a bird's eye view approach for each layout. e_offset represent the offset from the property's entrance_edge; its axis perpendicular to it.\nc_offset represents the offset in the axis parallel to the entrance_edge.\nThe layouts do not consider orientation. The component designer uses the layout for each component, along with the property orientation to properly position each component."""
    name = None
    emoji = '📍'
    plot_length = None
    layout = {}         
    def __init__(
        self,
        plot_length: int
        ):
        self.plot_length = plot_length
        print(f"{self.emoji} Layout initialized.\n")
        print(f"name: {self.name}\n")
        self._randomize_layout()
        return None
    def _randomize_layout(self):
        pass
    def _print(self, item_name, item_properties):
        print(f"{item_name}\n")
        for k, v in item_properties.items():
            print(f"{k}: {v}")
        print()
        return None
class Basic(Layout):
    name = 'basic'
    def _randomize_layout(self):
        self._position_pool()
        self._position_house()
        self._position_paths()
        self._position_internal_walls()
        self._position_internal_doors()
        self._position_windows()
        self._position_beds()
        self._position_outdoor_features()
    def _position_beds(self):
        bed_layouts = []
        house_layout = self.layout['house']
        h_position = house_layout['position']
        h_e_offset = house_layout['e_offset']
        h_c_offset = house_layout['c_offset']
        h_e_len = house_layout['e_len']
        h_c_len = house_layout['c_len']
        if h_position == 'middle':
            bedroom_side = random.choice(['right', 'left'])
            if bedroom_side == 'right':
                house_layout['bedroom_side'] = 'right'
                e_offset = 1
                c_offset = 1
                orientation = 1
                bed_layouts.append({
                    'room': 'right',
                    'orientation': orientation,
                    'e_offset': e_offset,
                    'c_offset': c_offset
                })
                e_offset = h_e_len - 1 - 1
                bed_layouts.append({
                    'room': 'right',
                    'orientation': orientation,
                    'e_offset': e_offset,
                    'c_offset': c_offset
                })
            elif bedroom_side == 'left':
                house_layout['bedroom_side'] = 'left'
                e_offset = 1
                c_offset = h_c_len - 1 - 1
                orientation = 3
                bed_layouts.append({
                    'room': 'left',
                    'orientation': orientation,
                    'e_offset': e_offset,
                    'c_offset': c_offset
                })
                e_offset = h_e_len - 1 - 1
                bed_layouts.append({
                    'room': 'left',
                    'orientation': orientation,
                    'e_offset': e_offset,
                    'c_offset': c_offset
                })
        elif h_position == 'left':
            e_offset = 1
            c_offset = h_c_len - 1 - 1
            orientation = 3
            bed_layouts.append({
                'room': 'front',
                'orientation': orientation,
                'e_offset': e_offset,
                'c_offset': c_offset
            })
            e_offset = h_e_len - 1 - 1
            bed_layouts.append({
                'room': 'back',
                'orientation': orientation,
                'e_offset': e_offset,
                'c_offset': c_offset
            })
        elif h_position == 'right':
            e_offset = 1
            c_offset = 1
            orientation = 1
            bed_layouts.append({
                'room': 'front',
                'orientation': orientation,
                'e_offset': e_offset,
                'c_offset': c_offset
            })
            e_offset = h_e_len - 1 - 1
            bed_layouts.append({
                'room': 'back',
                'orientation': orientation,
                'e_offset': e_offset,
                'c_offset': c_offset
            })
        house_layout['beds'] = bed_layouts
    def _position_pool(self):
        e_offset = None     # offset into property from edge (+z for orientation 0)
        c_offset = None     # offset from entrance corner to corner (+x for orientation 0)
        e_len = None        # length in e  direction
        c_len = None        # length in c direction
        gate_e_offset = None
        gate_c_offset = None
        positions = ['left', 'back', 'right']               # From perpsective of walking onto property from entrance
        random_position = random.choice(positions)
        # random_position = 'back'                          # HARD CODED FOR TESTING
        if random_position == 'back':                       ### BACK POOL ###
            e_offset = 10
            e_len = self.plot_length - e_offset - 1         # POOL DEPTH = 4
            c_offsets = [1, 2, 3, 4]                        # GAP BETWEEN BOUNDARY AND POOL = 0/1/2/3
            c_offset = random.choice(c_offsets)
            c_len = self.plot_length - (c_offset * 2)       # POOL WIDTH = 13/11/9/7
            gate_e_offset = 10
            gate_c_offset = c_offset + c_len // 2
        else:                                               ### SIDE POOL ###
            e_offsets = [6, 7]                              # GAP BETWEEN BOUNDARY AND POOL = 5/6
            e_offset = random.choice(e_offsets)
            e_len = self.plot_length - e_offset - 1         # POOL DEPTH = 8/7
            gate_e_offset = 11
            c_lens = [4, 5]                                 # POOL WIDTH = 4/5/6
            c_len = random.choice(c_lens)
            if random_position == 'right':                  ### RIGHT POOL ###
                c_offset = 1
                gate_c_offset = c_offset + c_len - 1
            elif random_position == 'left':                 ### LEFT POOL
                c_offset = self.plot_length - 1 - c_len
                gate_c_offset = c_offset
        self.layout['pool'] = {
            'position' : random_position,
            'e_offset': e_offset,
            'c_offset': c_offset,
            'e_len': e_len,
            'c_len': c_len,
            'gate_e_offset': gate_e_offset,
            'gate_c_offset': gate_c_offset
        }
        self._print('pool', self.layout['pool'])
        return None
    def _position_house(self):
        # see _position_pool for description of below variables
        position = None             
        e_offset = None
        c_offset = None
        e_len = None
        c_len = None
        pool_door_e_offset = None
        pool_door_c_offset = None
        pool_door_orientation = None
        front_door_e_offset = None
        front_door_c_offset = None
        front_door_orientation = 3
        front_step_e_offset = None
        front_step_c_offset = None
        pool_step_e_offset = None
        pool_step_c_offset = None

        pool_position = self.layout['pool']['position']

        if pool_position == 'back':                                     ### HOUSE MIDDLE POSITION ###
            position = 'middle'                                         
            c_offsets = [2, 3]
            c_offset = random.choice(c_offsets)
            # c_offset = 3        # HARD CODED FOR TESTING
            c_len = self.plot_length - (c_offset * 2)                   # HOUSE WIDTH = 11 or 9
            gap = 1                                                     # GAP BETWEEN POOL AND HOUSE = 1
            e_len_pool = self.layout['pool']['e_len']
            e_offsets = [3, 4]                                          # GAP BETWEEN ENTRANCE AND HOUSE = 2 or 3
            e_offset = random.choice(e_offsets)
            e_len = self.plot_length - e_offset - e_len_pool - gap - 1  # HOUSE DEPTH = 6 or 5
            pool_door_e_offset = e_offset + e_len - 1
            pool_door_c_offset = c_offset + (c_len // 2)
            pool_door_orientation = 1
            pool_step_e_offset = pool_door_e_offset + 1
            pool_step_c_offset = pool_door_c_offset
            front_door_e_offset = e_offset
            front_door_c_offset = c_offset + (c_len // 2)
        else:                                                           ### HOUSE SIDE POSITION ###
            c_len_pool = self.layout['pool']['c_len']
            e_offsets = [6, 7]                                          # GAP BETWEEN ENTRANCE AND HOUSE = 5 or 6
            e_offset = random.choice(e_offsets)
            # e_offset = 6    # HARD CODED FOR TESTING
            e_len = self.plot_length - e_offset - 1                     # HOUSE DEPTH = 8 or 7
            gap = 1                                                     # GAP BETWEEN HOUSE AND POOL = 1
            c_len = self.plot_length - c_len_pool - gap - 2             # HOUSE WIDTH = 8 or 7
            c_offset_pool = self.layout['pool']['c_offset']
            pool_door_e_offset = 11
            pool_step_e_offset = pool_door_e_offset
            front_door_e_offset = e_offset
            if pool_position == 'right':
                position = 'left'
                c_offset = c_offset_pool + c_len_pool + gap             # C_OFFSET = 6/7 or 7/8 or 8/9
                pool_door_c_offset = c_offset
                pool_door_orientation = 2
                pool_step_c_offset = pool_door_c_offset - 1
                front_door_c_offset = c_offset + 2
            elif pool_position == 'left':
                position = 'right'
                c_offset = 1                                            # C_OFFSET = 1, up to 5/6/7/8
                pool_door_c_offset = c_offset + c_len - 1
                pool_door_orientation = 0
                pool_step_c_offset = pool_door_c_offset + 1
                front_door_c_offset = c_offset + c_len - 1 - 2
        front_step_e_offset = e_offset - 1
        front_step_c_offset = front_door_c_offset
        self.layout['house'] = {
            'position' : position,
            'e_offset': e_offset,
            'c_offset': c_offset,
            'e_len': e_len,
            'c_len': c_len,
            'pool_door_e_offset': pool_door_e_offset,
            'pool_door_c_offset': pool_door_c_offset,
            'pool_door_orientation': pool_door_orientation,
            'front_door_e_offset': front_door_e_offset,
            'front_door_c_offset': front_door_c_offset,
            'front_door_orientation': front_door_orientation,
            'front_step_e_offset': front_step_e_offset,
            'front_step_c_offset': front_step_c_offset,
            'pool_step_e_offset': pool_step_e_offset,
            'pool_step_c_offset': pool_step_c_offset,
            'internal_doors': [],
            'internal_walls': [],
            'windows': []
        }
        self._print('house', self.layout['house'])
        return None
    def _position_internal_doors(self):
        internal_door_layouts = []
        house_layout = self.layout['house']
        h_e_len = house_layout['e_len']
        h_c_len = house_layout['c_len']
        if house_layout['position'] == 'middle':
            e_offset = h_e_len // 2
            c_offset = h_c_len // 2 - 1
            internal_door_layouts.append({
                'name': 'right_internal_door',
                'e_offset': e_offset,
                'c_offset': c_offset,
                'orientation': 0
            })
            c_offset = house_layout['c_len'] // 2 + 1
            internal_door_layouts.append({
                'name': 'left_internal_door',
                'e_offset': e_offset,
                'c_offset': c_offset,
                'orientation': 2
            })
        else:
            e_offset = None
            c_offset = None
            if house_layout['position'] == 'left':
                c_offset = 3
                e_offset = 2
                orientation = 2
                internal_door_layouts.append({
                    'name': 'front_room',
                    'e_offset': e_offset,
                    'c_offset': c_offset,
                    'orientation': orientation
                })
                e_offset = h_e_len - 1 - 2
                internal_door_layouts.append({
                    'name': 'back_room',
                    'e_offset': e_offset,
                    'c_offset': c_offset,
                    'orientation': orientation
                })
            if house_layout['position'] == 'right':
                c_offset = h_c_len - 1 - 3
                e_offset = 2
                orientation = 0
                internal_door_layouts.append({
                    'name': 'front_room',
                    'e_offset': e_offset,
                    'c_offset': c_offset,
                    'orientation': orientation
                })
                e_offset = h_e_len - 1 - 2
                internal_door_layouts.append({
                    'name': 'back_room',
                    'e_offset': e_offset,
                    'c_offset': c_offset,
                    'orientation': orientation
                })
        self.layout['house']['internal_doors'] = internal_door_layouts
    def _position_windows(self):
        window_layouts = []
        house_layout = self.layout['house']
        h_e_len = house_layout['e_len']
        h_c_len = house_layout['c_len']
        if house_layout['position'] == 'middle':
            front_window_layouts = []
            e_offset = 0
            c_offset = h_c_len // 4
            front_window_layouts.append ({
                'name': 'front_window',
                'e_offset': e_offset,
                'c_offset': c_offset,
            })
            c_offset = h_c_len - 1 - c_offset
            front_window_layouts.append ({
                'name': 'front_window',
                'e_offset': e_offset,
                'c_offset': c_offset,
            })
            back_window_layouts = []
            e_offset = h_e_len - 1
            back_window_layouts.append ({
                'name': 'front_window',
                'e_offset': e_offset,
                'c_offset': c_offset,
            })
            c_offset = h_c_len // 4
            back_window_layouts.append ({
                'name': 'front_window',
                'e_offset': e_offset,
                'c_offset': c_offset,
            })
            window_layouts = front_window_layouts + back_window_layouts 
        elif house_layout['position'] == 'right':
            front_window_layouts = []
            e_offset = 0
            c_offset = h_c_len // 4
            front_window_layouts.append ({
                'name': 'front_window',
                'e_offset': e_offset,
                'c_offset': c_offset,
            })
            back_window_layouts = []
            e_offset = h_e_len - 1
            back_window_layouts.append ({
                'name': 'front_window',
                'e_offset': e_offset,
                'c_offset': c_offset,
            })
            window_layouts = front_window_layouts + back_window_layouts 
        elif house_layout['position'] == 'left':
            front_window_layouts = []
            e_offset = 0
            c_offset = h_c_len - 1 - (h_c_len // 4)
            front_window_layouts.append ({
                'name': 'front_window',
                'e_offset': e_offset,
                'c_offset': c_offset,
            })
            back_window_layouts = []
            e_offset = h_e_len - 1
            back_window_layouts.append ({
                'name': 'front_window',
                'e_offset': e_offset,
                'c_offset': c_offset,
            })
            window_layouts = front_window_layouts + back_window_layouts 
        self.layout['house']['windows'] = window_layouts
    def _position_internal_walls(self):
        internal_wall_layouts = []
        house_layout = self.layout['house']
        if house_layout['position'] == 'middle':
            corridor_wall_layouts = []
            e_offset = house_layout['e_offset'] + 1
            c_offset = house_layout['front_door_c_offset'] + 1
            e_len = house_layout['e_len'] - 2
            c_len = 1
            corridor_wall_layouts.append({
                'name': 'corridor_wall',
                'e_offset': e_offset,
                'c_offset': c_offset,
                'e_len': e_len,
                'c_len': c_len
            })
            c_offset = house_layout['front_door_c_offset'] - 1
            corridor_wall_layouts.append({
                'name': 'corridor_wall',
                'e_offset': e_offset,
                'c_offset': c_offset,
                'e_len': e_len,
                'c_len': c_len
            })
            for layout in corridor_wall_layouts:
                internal_wall_layouts.append(layout)
        else:
            e_offset = house_layout['e_offset'] + 1
            c_offset = None
            e_len = house_layout['e_len'] - 2
            c_len = 1
            if house_layout['position'] == 'left':
                c_offset = house_layout['front_door_c_offset'] + 1
            elif house_layout['position'] == 'right':
                c_offset = house_layout['front_door_c_offset'] - 1
            internal_wall_layouts.append({
                'name': 'corridor_wall',
                'e_offset': e_offset,
                'c_offset': c_offset,
                'e_len': e_len,
                'c_len': c_len
            })
            if house_layout['c_len'] >= 7:
                room_dividing_wall_layout = {}
                e_offset = house_layout['e_offset'] + (house_layout['e_len'] // 2)
                c_offset = None
                e_len = 1
                c_len = house_layout['c_len'] - 5
                if house_layout['position'] == 'left':
                    c_offset = house_layout['front_door_c_offset'] + 2
                elif house_layout['position'] == 'right':
                    c_offset = house_layout['c_offset'] + 1
                room_dividing_wall_layout = {
                    'name': 'roof_dividing_wall',
                    'e_offset': e_offset,
                    'c_offset': c_offset,
                    'e_len': e_len,
                    'c_len': c_len
                }
                internal_wall_layouts.append(room_dividing_wall_layout)
        self.layout['house']['internal_walls'] = internal_wall_layouts
        pass
    def _position_outdoor_features(self):
        # TODO Read code again and make adjustments
        e_offset_house = self.layout['house']['e_offset']
        feature_house_gaps = [1, 2]
        feature_house_gap = random.choice(feature_house_gaps)
        entrance_feature_gaps = [1, 2]
        entrance_feature_gap = random.choice(entrance_feature_gaps)
        e_len = e_offset_house - feature_house_gap - entrance_feature_gap - 1
        e_offset = 1 + entrance_feature_gap
        boundary_gaps = [1, 2]
        boundary_gap = random.choice(boundary_gaps)
        path_gaps = [1, 2]
        path_gap = random.choice(path_gaps)
        left_feature = random.choice([True, False])
        right_feature = random.choice([True, False])
        self.layout['outdoor_features'] = []
        if left_feature:
            c_offset = 7 + path_gap + 1
            self.layout['outdoor_features'].append({
                'position': 'left',
                'e_offset': e_offset,
                'c_offset': c_offset,
                'e_len': e_len,
                'c_len': self.plot_length - c_offset - boundary_gap - 1 - 1
            })
        if right_feature:
            c_offset = 1 + boundary_gap
            self.layout['outdoor_features'].append({
                'position': 'right',
                'e_offset': e_offset,
                'c_offset': c_offset,
                'e_len': e_len,
                'c_len': 7 - path_gap - 1 - 1 - boundary_gap
            })
        for layout in self.layout['outdoor_features']:
            self._print('outdoor_feature', layout)
        return None
    def _position_paths(self):
        # TODO look for gaps between pool, house, entrance and boundary to create paths
        paths = []
        if self.layout['pool']['position'] == 'back':
            back_path_layout = self._get_back_path_layout(self.layout['pool'])
            paths.append(back_path_layout)
            side_path_layouts = self._get_side_path_layouts(self.layout['house'])
            for side_path_layout in side_path_layouts:
                paths.append(side_path_layout)
        else:
            house_pool_path = self._get_house_pool_path(self.layout['house'])
            paths.append(house_pool_path)
        front_path_layout = self._get_front_path_layout(self.layout['house'])
        paths.append(front_path_layout)
        c_axis_path_layout = self._get_c_axis_path_layout(self.layout['house'])
        paths.append(c_axis_path_layout)
        self.layout['paths'] = paths
    def _get_house_pool_path(self, house_layout):
        name = 'house_pool_path'
        c_offset = None
        if house_layout['position'] == 'left':
            c_offset = house_layout['c_offset'] - 1
        elif house_layout['position'] == 'right':
            c_offset = house_layout['c_offset'] + house_layout['c_len']
        e_offset = house_layout['e_offset']
        c_len = 1
        e_len = 14 - house_layout['e_offset']
        return {
            'name': name,
            'e_offset': e_offset,
            'c_offset': c_offset,
            'e_len': e_len,
            'c_len': c_len
        }
    def _get_side_path_layouts(self, house_layout):
        side_path_layouts = []
        name = 'side_path'
        c_offset = house_layout['c_offset'] - 1
        e_offset = house_layout['e_offset']
        c_len = 1
        e_len = house_layout['e_len']
        side_path_layouts.append({
            'name': name,
            'e_offset': e_offset,
            'c_offset': c_offset,
            'e_len': e_len,
            'c_len': c_len
        })
        c_offset = house_layout['c_offset'] + house_layout['c_len']
        side_path_layouts.append({
            'name': name,
            'e_offset': e_offset,
            'c_offset': c_offset,
            'e_len': e_len,
            'c_len': c_len
        })
        return side_path_layouts
    def _get_back_path_layout(self, pool_layout):
        name = 'back_path'
        c_offset = 1
        e_offset = pool_layout['e_offset'] - 1
        c_len = 13
        e_len = 1
        return {
            'name': name,
            'e_offset': e_offset,
            'c_offset': c_offset,
            'e_len': e_len,
            'c_len': c_len
        }
    def _get_c_axis_path_layout(self, house_layout):
        name = 'c_axis_path'
        c_offset = 1
        e_offset = house_layout['e_offset'] - 1
        c_len = 13
        e_len = 1
        return {
            'name': name,
            'e_offset': e_offset,
            'c_offset': c_offset,
            'e_len': e_len,
            'c_len': c_len
        }
    def _get_front_path_layout(self, house_layout):
        name = 'front_path'
        c_offset = 7
        e_offset = 1
        c_len = 1
        e_len = house_layout['e_offset'] - 1
        return {
            'name': name,
            'e_offset': e_offset,
            'c_offset': c_offset,
            'e_len': e_len,
            'c_len': c_len
        }
class PoolSide(Layout):
    name = 'pool_side'
class Dungeon(Layout):
    name = 'dungeon'

# TESTING
if __name__ == '__main__':
    house_type = 'basic'
    plot_length = 15
    layout = get_layout(house_type, plot_length)
    print(layout)