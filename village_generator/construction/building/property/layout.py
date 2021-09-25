import random


def get_layout(house_type: str, plot_length: int) -> object:
    """Takes house type in string and plot length in int to return a object with a dictionary of layouts for various
    component of a property. """

    if house_type == 'basic':
        return Basic(plot_length)
    elif house_type == 'poolside':
        return PoolSide(plot_length)
    elif house_type == 'dungeon':
        return Dungeon(plot_length)


class Layout:
    """Upon init, returns an object with a dictionary of layouts for property component and some of the house
    component. It takes a bird's eye view approach for each layout. z_offset represent the offset from the
    property's entrance_edge; its axis perpendicular to it.\nx_offset represents the offset in the axis parallel to
    the entrance_edge.\nThe layouts do not consider ABSOLUTE orientation, rather, the relative orientations of each
    component to each other. The component designer found in designer.py uses the layout for each component,
    along with the absolute orientation of the property to properly position and orientate each component. """
    name = None
    emoji = '📍'
    plot_length = None
    layout = {}

    # Init
    def __init__(self, plot_length: int):
        self.plot_length = plot_length
        print(f"{self.emoji} Layout initialized.\n")
        print(f"name: {self.name}\n")
        self._randomize_layout()

    # Internal Methods
    def _randomize_layout(self):
        pass

    # Print Method
    def _print(self, item_name, item_properties):
        print(f"{item_name}\n")
        for k, v in item_properties.items():
            print(f"{k}: {v}")
        print()


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
        h_z_len = house_layout['z_len']
        h_x_len = house_layout['x_len']

        if h_position == 'middle':
            bedroom_side = random.choice(['right', 'left'])

            if bedroom_side == 'right':
                house_layout['bedroom_side'] = 'right'
                z_offset = 1
                x_offset = 1
                orientation = 1
                bed_layouts.append({
                    'room': 'right',
                    'orientation': orientation,
                    'z_offset': z_offset,
                    'x_offset': x_offset
                })
                z_offset = h_z_len - 1 - 1
                bed_layouts.append({
                    'room': 'right',
                    'orientation': orientation,
                    'z_offset': z_offset,
                    'x_offset': x_offset
                })
            elif bedroom_side == 'left':
                house_layout['bedroom_side'] = 'left'
                z_offset = 1
                x_offset = h_x_len - 1 - 1
                orientation = 3
                bed_layouts.append({
                    'room': 'left',
                    'orientation': orientation,
                    'z_offset': z_offset,
                    'x_offset': x_offset
                })
                z_offset = h_z_len - 1 - 1
                bed_layouts.append({
                    'room': 'left',
                    'orientation': orientation,
                    'z_offset': z_offset,
                    'x_offset': x_offset
                })
        elif h_position == 'left':
            z_offset = 1
            x_offset = h_x_len - 1 - 1
            orientation = 3
            bed_layouts.append({
                'room': 'front',
                'orientation': orientation,
                'z_offset': z_offset,
                'x_offset': x_offset
            })
            z_offset = h_z_len - 1 - 1
            bed_layouts.append({
                'room': 'back',
                'orientation': orientation,
                'z_offset': z_offset,
                'x_offset': x_offset
            })
        elif h_position == 'right':
            z_offset = 1
            x_offset = 1
            orientation = 1
            bed_layouts.append({
                'room': 'front',
                'orientation': orientation,
                'z_offset': z_offset,
                'x_offset': x_offset
            })
            z_offset = h_z_len - 1 - 1
            bed_layouts.append({
                'room': 'back',
                'orientation': orientation,
                'z_offset': z_offset,
                'x_offset': x_offset
            })
        house_layout['beds'] = bed_layouts

    def _position_pool(self):
        z_offset = None  # offset into property from edge (+z for orientation 0)
        x_offset = None  # offset from entrance corner to corner (+x for orientation 0)
        z_len = None  # length in e  direction
        x_len = None  # length in c direction
        gate_z_offset = None
        gate_x_offset = None
        positions = ['left', 'back', 'right']  # From perpsective of walking onto property from entrance
        random_position = random.choice(positions)
        # random_position = 'back'                          # HARD CODED FOR TESTING
        if random_position == 'back':  ### BACK POOL ###
            z_offset = 10
            z_len = self.plot_length - z_offset - 1  # POOL DEPTH = 4
            x_offsets = [1, 2, 3, 4]  # GAP BETWEEN BOUNDARY AND POOL = 0/1/2/3
            x_offset = random.choice(x_offsets)
            x_len = self.plot_length - (x_offset * 2)  # POOL WIDTH = 13/11/9/7
            gate_z_offset = 10
            gate_x_offset = x_offset + x_len // 2
        else:  ### SIDE POOL ###
            z_offsets = [6, 7]  # GAP BETWEEN BOUNDARY AND POOL = 5/6
            z_offset = random.choice(z_offsets)
            z_len = self.plot_length - z_offset - 1  # POOL DEPTH = 8/7
            gate_z_offset = 11
            x_lens = [4, 5]  # POOL WIDTH = 4/5/6
            x_len = random.choice(x_lens)

            if random_position == 'right':  ### RIGHT POOL ###
                x_offset = 1
                gate_x_offset = x_offset + x_len - 1
            elif random_position == 'left':  ### LEFT POOL
                x_offset = self.plot_length - 1 - x_len
                gate_x_offset = x_offset

        self.layout['pool'] = {
            'position': random_position,
            'z_offset': z_offset,
            'x_offset': x_offset,
            'z_len': z_len,
            'x_len': x_len,
            'gate_z_offset': gate_z_offset,
            'gate_x_offset': gate_x_offset
        }

        self._print('pool', self.layout['pool'])

    def _position_house(self):
        # see _position_pool for description of below variables
        position = None
        z_offset = None
        x_offset = None
        z_len = None
        x_len = None
        pool_door_z_offset = None
        pool_door_x_offset = None
        pool_door_orientation = None
        front_door_z_offset = None
        front_door_x_offset = None
        front_door_orientation = 3
        front_step_z_offset = None
        front_step_x_offset = None
        pool_step_z_offset = None
        pool_step_x_offset = None

        pool_position = self.layout['pool']['position']

        if pool_position == 'back':  ### HOUSE MIDDLE POSITION ###
            position = 'middle'
            x_offsets = [2, 3]
            x_offset = random.choice(x_offsets)
            # x_offset = 3        # HARD CODED FOR TESTING
            x_len = self.plot_length - (x_offset * 2)  # HOUSE WIDTH = 11 or 9
            gap = 1  # GAP BETWEEN POOL AND HOUSE = 1
            z_len_pool = self.layout['pool']['z_len']
            z_offsets = [3, 4]  # GAP BETWEEN ENTRANCE AND HOUSE = 2 or 3
            z_offset = random.choice(z_offsets)
            z_len = self.plot_length - z_offset - z_len_pool - gap - 1  # HOUSE DEPTH = 6 or 5
            pool_door_z_offset = z_offset + z_len - 1
            pool_door_x_offset = x_offset + (x_len // 2)
            pool_door_orientation = 1
            pool_step_z_offset = pool_door_z_offset + 1
            pool_step_x_offset = pool_door_x_offset
            front_door_z_offset = z_offset
            front_door_x_offset = x_offset + (x_len // 2)
        else:  ### HOUSE SIDE POSITION ###
            x_len_pool = self.layout['pool']['x_len']
            z_offsets = [6, 7]  # GAP BETWEEN ENTRANCE AND HOUSE = 5 or 6
            z_offset = random.choice(z_offsets)
            # z_offset = 6    # HARD CODED FOR TESTING
            z_len = self.plot_length - z_offset - 1  # HOUSE DEPTH = 8 or 7
            gap = 1  # GAP BETWEEN HOUSE AND POOL = 1
            x_len = self.plot_length - x_len_pool - gap - 2  # HOUSE WIDTH = 8 or 7
            x_offset_pool = self.layout['pool']['x_offset']
            pool_door_z_offset = 11
            pool_step_z_offset = pool_door_z_offset
            front_door_z_offset = z_offset

            if pool_position == 'right':
                position = 'left'
                x_offset = x_offset_pool + x_len_pool + gap  # x_offset = 6/7 or 7/8 or 8/9
                pool_door_x_offset = x_offset
                pool_door_orientation = 2
                pool_step_x_offset = pool_door_x_offset - 1
                front_door_x_offset = x_offset + 2
            elif pool_position == 'left':
                position = 'right'
                x_offset = 1  # x_offset = 1, up to 5/6/7/8
                pool_door_x_offset = x_offset + x_len - 1
                pool_door_orientation = 0
                pool_step_x_offset = pool_door_x_offset + 1
                front_door_x_offset = x_offset + x_len - 1 - 2

        front_step_z_offset = z_offset - 1
        front_step_x_offset = front_door_x_offset
        self.layout['house'] = {
            'position': position,
            'z_offset': z_offset,
            'x_offset': x_offset,
            'z_len': z_len,
            'x_len': x_len,
            'pool_door_z_offset': pool_door_z_offset,
            'pool_door_x_offset': pool_door_x_offset,
            'pool_door_orientation': pool_door_orientation,
            'front_door_z_offset': front_door_z_offset,
            'front_door_x_offset': front_door_x_offset,
            'front_door_orientation': front_door_orientation,
            'front_step_z_offset': front_step_z_offset,
            'front_step_x_offset': front_step_x_offset,
            'pool_step_z_offset': pool_step_z_offset,
            'pool_step_x_offset': pool_step_x_offset,
            'internal_doors': [],
            'internal_walls': [],
            'windows': []
        }
        self._print('house', self.layout['house'])

    def _position_internal_doors(self):
        internal_door_layouts = []
        house_layout = self.layout['house']
        h_z_len = house_layout['z_len']
        h_x_len = house_layout['x_len']

        if house_layout['position'] == 'middle':
            z_offset = h_z_len // 2
            x_offset = h_x_len // 2 - 1
            internal_door_layouts.append({
                'name': 'right_internal_door',
                'z_offset': z_offset,
                'x_offset': x_offset,
                'orientation': 0
            })
            x_offset = house_layout['x_len'] // 2 + 1
            internal_door_layouts.append({
                'name': 'left_internal_door',
                'z_offset': z_offset,
                'x_offset': x_offset,
                'orientation': 2
            })
        else:
            z_offset = None
            x_offset = None

            if house_layout['position'] == 'left':
                x_offset = 3
                z_offset = 2
                orientation = 2
                internal_door_layouts.append({
                    'name': 'front_room',
                    'z_offset': z_offset,
                    'x_offset': x_offset,
                    'orientation': orientation
                })
                z_offset = h_z_len - 1 - 2
                internal_door_layouts.append({
                    'name': 'back_room',
                    'z_offset': z_offset,
                    'x_offset': x_offset,
                    'orientation': orientation
                })

            if house_layout['position'] == 'right':
                x_offset = h_x_len - 1 - 3
                z_offset = 2
                orientation = 0
                internal_door_layouts.append({
                    'name': 'front_room',
                    'z_offset': z_offset,
                    'x_offset': x_offset,
                    'orientation': orientation
                })
                z_offset = h_z_len - 1 - 2
                internal_door_layouts.append({
                    'name': 'back_room',
                    'z_offset': z_offset,
                    'x_offset': x_offset,
                    'orientation': orientation
                })
        self.layout['house']['internal_doors'] = internal_door_layouts

    def _position_windows(self):
        window_layouts = []
        house_layout = self.layout['house']
        h_z_len = house_layout['z_len']
        h_x_len = house_layout['x_len']

        if house_layout['position'] == 'middle':
            front_window_layouts = []
            z_offset = 0
            x_offset = h_x_len // 4
            front_window_layouts.append({
                'name': 'front_window',
                'z_offset': z_offset,
                'x_offset': x_offset,
            })

            x_offset = h_x_len - 1 - x_offset
            front_window_layouts.append({
                'name': 'front_window',
                'z_offset': z_offset,
                'x_offset': x_offset,
            })

            back_window_layouts = []
            z_offset = h_z_len - 1
            back_window_layouts.append({
                'name': 'front_window',
                'z_offset': z_offset,
                'x_offset': x_offset,
            })

            x_offset = h_x_len // 4
            back_window_layouts.append({
                'name': 'front_window',
                'z_offset': z_offset,
                'x_offset': x_offset,
            })

            window_layouts = front_window_layouts + back_window_layouts
        elif house_layout['position'] == 'right':
            front_window_layouts = []
            z_offset = 0
            x_offset = h_x_len // 4
            front_window_layouts.append({
                'name': 'front_window',
                'z_offset': z_offset,
                'x_offset': x_offset,
            })

            back_window_layouts = []
            z_offset = h_z_len - 1
            back_window_layouts.append({
                'name': 'front_window',
                'z_offset': z_offset,
                'x_offset': x_offset,
            })

            window_layouts = front_window_layouts + back_window_layouts
        elif house_layout['position'] == 'left':
            front_window_layouts = []
            z_offset = 0
            x_offset = h_x_len - 1 - (h_x_len // 4)
            front_window_layouts.append({
                'name': 'front_window',
                'z_offset': z_offset,
                'x_offset': x_offset,
            })

            back_window_layouts = []
            z_offset = h_z_len - 1
            back_window_layouts.append({
                'name': 'front_window',
                'z_offset': z_offset,
                'x_offset': x_offset,
            })

            window_layouts = front_window_layouts + back_window_layouts
        self.layout['house']['windows'] = window_layouts

    def _position_internal_walls(self):
        internal_wall_layouts = []
        house_layout = self.layout['house']

        if house_layout['position'] == 'middle':
            corridor_wall_layouts = []
            z_offset = house_layout['z_offset'] + 1
            x_offset = house_layout['front_door_x_offset'] + 1
            z_len = house_layout['z_len'] - 2
            x_len = 1
            corridor_wall_layouts.append({
                'name': 'corridor_wall',
                'z_offset': z_offset,
                'x_offset': x_offset,
                'z_len': z_len,
                'x_len': x_len
            })

            x_offset = house_layout['front_door_x_offset'] - 1
            corridor_wall_layouts.append({
                'name': 'corridor_wall',
                'z_offset': z_offset,
                'x_offset': x_offset,
                'z_len': z_len,
                'x_len': x_len
            })

            for layout in corridor_wall_layouts:
                internal_wall_layouts.append(layout)
        else:
            z_offset = house_layout['z_offset'] + 1
            x_offset = None
            z_len = house_layout['z_len'] - 2
            x_len = 1

            if house_layout['position'] == 'left':
                x_offset = house_layout['front_door_x_offset'] + 1
            elif house_layout['position'] == 'right':
                x_offset = house_layout['front_door_x_offset'] - 1

            internal_wall_layouts.append({
                'name': 'corridor_wall',
                'z_offset': z_offset,
                'x_offset': x_offset,
                'z_len': z_len,
                'x_len': x_len
            })

            if house_layout['x_len'] >= 7:
                room_dividing_wall_layout = {}
                z_offset = house_layout['z_offset'] + (house_layout['z_len'] // 2)
                x_offset = None
                z_len = 1
                x_len = house_layout['x_len'] - 5

                if house_layout['position'] == 'left':
                    x_offset = house_layout['front_door_x_offset'] + 2
                elif house_layout['position'] == 'right':
                    x_offset = house_layout['x_offset'] + 1

                room_dividing_wall_layout = {
                    'name': 'roof_dividing_wall',
                    'z_offset': z_offset,
                    'x_offset': x_offset,
                    'z_len': z_len,
                    'x_len': x_len
                }
                internal_wall_layouts.append(room_dividing_wall_layout)

        self.layout['house']['internal_walls'] = internal_wall_layouts

    def _position_outdoor_features(self):
        # TODO Read code again and make adjustments
        z_offset_house = self.layout['house']['z_offset']
        feature_house_gaps = [1, 2]
        feature_house_gap = random.choice(feature_house_gaps)
        entrance_feature_gaps = [1, 2]
        entrance_feature_gap = random.choice(entrance_feature_gaps)
        z_len = z_offset_house - feature_house_gap - entrance_feature_gap - 1
        z_offset = 1 + entrance_feature_gap
        boundary_gaps = [1, 2]
        boundary_gap = random.choice(boundary_gaps)
        path_gaps = [1, 2]
        path_gap = random.choice(path_gaps)
        left_feature = random.choice([True, False])
        right_feature = random.choice([True, False])
        self.layout['outdoor_features'] = []

        if left_feature:
            x_offset = 7 + path_gap + 1
            self.layout['outdoor_features'].append({
                'position': 'left',
                'z_offset': z_offset,
                'x_offset': x_offset,
                'z_len': z_len,
                'x_len': self.plot_length - x_offset - boundary_gap - 1 - 1
            })

        if right_feature:
            x_offset = 1 + boundary_gap
            self.layout['outdoor_features'].append({
                'position': 'right',
                'z_offset': z_offset,
                'x_offset': x_offset,
                'z_len': z_len,
                'x_len': 7 - path_gap - 1 - 1 - boundary_gap
            })

        for layout in self.layout['outdoor_features']:
            self._print('outdoor_feature', layout)

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
        x_offset = None

        if house_layout['position'] == 'left':
            x_offset = house_layout['x_offset'] - 1
        elif house_layout['position'] == 'right':
            x_offset = house_layout['x_offset'] + house_layout['x_len']

        z_offset = house_layout['z_offset']
        x_len = 1
        z_len = 14 - house_layout['z_offset']

        return {
            'name': name,
            'z_offset': z_offset,
            'x_offset': x_offset,
            'z_len': z_len,
            'x_len': x_len
        }

    def _get_side_path_layouts(self, house_layout):
        side_path_layouts = []
        name = 'side_path'
        x_offset = house_layout['x_offset'] - 1
        z_offset = house_layout['z_offset']
        x_len = 1
        z_len = house_layout['z_len']
        side_path_layouts.append({
            'name': name,
            'z_offset': z_offset,
            'x_offset': x_offset,
            'z_len': z_len,
            'x_len': x_len
        })

        x_offset = house_layout['x_offset'] + house_layout['x_len']
        side_path_layouts.append({
            'name': name,
            'z_offset': z_offset,
            'x_offset': x_offset,
            'z_len': z_len,
            'x_len': x_len
        })

        return side_path_layouts

    def _get_back_path_layout(self, pool_layout):
        name = 'back_path'
        x_offset = 1
        z_offset = pool_layout['z_offset'] - 1
        x_len = 13
        z_len = 1

        return {
            'name': name,
            'z_offset': z_offset,
            'x_offset': x_offset,
            'z_len': z_len,
            'x_len': x_len
        }

    def _get_c_axis_path_layout(self, house_layout):
        name = 'c_axis_path'
        x_offset = 1
        z_offset = house_layout['z_offset'] - 1
        x_len = 13
        z_len = 1

        return {
            'name': name,
            'z_offset': z_offset,
            'x_offset': x_offset,
            'z_len': z_len,
            'x_len': x_len
        }

    def _get_front_path_layout(self, house_layout):
        name = 'front_path'
        x_offset = 7
        z_offset = 1
        x_len = 1
        z_len = house_layout['z_offset'] - 1

        return {
            'name': name,
            'z_offset': z_offset,
            'x_offset': x_offset,
            'z_len': z_len,
            'x_len': x_len
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
