from mcpi import vec3 as v
import random
import property as p
import block as b
import components as c


class Designer:
    name = None
    emoji = '🎨'
    properties = []
    def __init__(self):
        print(f"{self.emoji} Designer created.\n")
        if self.name:
            print(f"designer.name: {self.name}\n")
    def give_specs(self, property):
        self.properties.append(property)
        self._design_components(property)
        pass
    def _design_components(self, property):
        self._design_property_components(property)
        self._design_house_components(property.house)
        pass
    def _design_property_components(self, property):
        self._design_entrance(property)
        self._design_boundary(property)
        self._design_pool(property)
        self._design_house(property)
        self._design_paths(property)
        self._design_outdoor_features(property)
    def _design_outdoor_features(self, property):
        e_v3 = property.entrance_edge['start']
        orientation = property.orientation
        h_e_offset = property.layout.layout['house']['e_offset']
        for outdoor_feature_layout in property.layout.layout['outdoor_features']:
            e_offset = outdoor_feature_layout['e_offset']
            c_offset = outdoor_feature_layout['c_offset']
            e_len = outdoor_feature_layout['e_len']
            c_len = outdoor_feature_layout['c_len']
            o_v3 = self._orientate(e_v3, orientation, e_offset, c_offset)[0]
            start_v3 = None
            x_len = None
            z_len = None
            if orientation == 0:
                start_v3 = v.Vec3(o_v3.x, o_v3.y, o_v3.z)
                x_len, z_len = c_len, e_len
            elif orientation == 1:
                start_v3 = v.Vec3(o_v3.x - (e_len - 1), o_v3.y, o_v3.z)
                x_len, z_len = e_len, c_len
            elif orientation == 2:
                start_v3 = v.Vec3(o_v3.x - (c_len - 1), o_v3.y, o_v3.z - (e_len - 1))
                x_len, z_len = c_len, e_len
            elif orientation == 3:
                start_v3 = v.Vec3(o_v3.x, o_v3.y, o_v3.z - (c_len - 1))
                x_len, z_len = e_len, c_len
            if x_len >= 2 and z_len >= 2:
                option = random.choice(['veggie_patch', 'flower_bed'])
                if option == 'veggie_patch':
                    property.components.append(c.veggie_patch.VeggiePatch(start_v3, x_len, z_len))
                elif option == 'flower_bed':
                    property.components.append(c.flower_bed.FlowerBed(start_v3, x_len, z_len))
            else:
                if h_e_offset == 3:
                    continue
                trunk_block = random.choice(b.OPTIONS[property.theme.name]['tree']['trunk'])
                leaves_block = random.choice(b.OPTIONS[property.theme.name]['tree']['leaves'])
                property.components.append(c.tree.Tree(o_v3, trunk_block, leaves_block))
        pass
    def _design_house_components(self, house):
        self._design_floors(house)
        self._design_walls(house)
        if house.total_levels >= 2:
            self._design_stairs(house)
        self._design_doors(house)
        self._design_door_steps(house)
        self._design_internal_walls(house)
        self._design_internal_doors(house)
        self._design_windows(house)
        self._design_roof(house)
        # self._design_rooms(house, levels, e_v3, e_offset, c_offset, e_len, c_len)
        pass
    def _design_door_steps(self, house):
        v3 = house.property_v3
        orientation = house.orientation
        layout = house.layout
        front_step_e_offset = layout['front_step_e_offset']
        front_step_c_offset = layout['front_step_c_offset']
        pool_step_e_offset = layout['pool_step_e_offset']
        pool_step_c_offset = layout['pool_step_c_offset']
        front_step_v3 = self._orientate(v3, orientation, front_step_e_offset, front_step_c_offset)[0]
        pool_step_v3 = self._orientate(v3, orientation, pool_step_e_offset, pool_step_c_offset)[0]
        front_step_block = random.choice(b.OPTIONS[house.theme]['steps']['basic'])
        pool_step_block = random.choice(b.OPTIONS[house.theme]['steps']['basic'])
        front_step = c.steps.Steps(front_step_v3, front_step_block)
        pool_step = c.steps.Steps(pool_step_v3, pool_step_block)
        house.components.append(front_step)
        house.components.append(pool_step)

    def _design_internal_doors(self, house):
        h_v3 = house.house_v3
        orientation = house.orientation
        theme = house.theme
        for internal_door_layout in house.layout['internal_doors']:
            internal_door_orientation = internal_door_layout['orientation']
            e_offset = internal_door_layout['e_offset']
            c_offset = internal_door_layout['c_offset']
            for floor_elevation in house.floor_elevations:
                elevated_v3 = v.Vec3(h_v3.x, h_v3.y + floor_elevation, h_v3.z)
                v3 = self._orientate(elevated_v3, orientation, e_offset, c_offset)[0]
                door_orientation = self._get_absolute_door_orientation(orientation, internal_door_orientation)
                top_block = random.choice(b.OPTIONS[theme]['door']['basic']).withData(8)
                bot_block = top_block.withData(door_orientation)
                internal_door = c.door.Door(v3, top_block, bot_block, door_orientation)
                house.components.append(internal_door)
                pass
        pass
    def _design_windows(self, house):
        window_block = random.choice(b.OPTIONS[house.theme]['window']['basic'])
        orientation = house.orientation
        h_v3 = house.house_v3
        for window_layout in house.layout['windows']:
            for i, floor_elevation in enumerate(house.floor_elevations):
                e_offset = window_layout['e_offset']
                c_offset = window_layout['c_offset']
                (x, y, z) = self._orientate(h_v3, orientation, e_offset, c_offset)[0]
                y += i * 4 + 2
                window = c.window.Window(v.Vec3(x, y, z), window_block)
                house.components.append(window)
    def _design_roof(self, house):
        style = random.choice([0, 1, 2, 3])
        stair_block = b.OPTIONS[house.theme]['roof']['stair'][style]
        slab_block = b.OPTIONS[house.theme]['roof']['slab'][style]
        cube_block = b.OPTIONS[house.theme]['roof']['cube'][style]
        layout = house.layout
        orientation = house.orientation
        h_v3 = house.house_v3
        y = h_v3.y + house.floor_elevations[-1] + 4
        e_len = layout['e_len']
        c_len = layout['c_len']
        start_v3 = None
        end_v3 = None
        if orientation == 0:
            start_v3 = v.Vec3(h_v3.x, y, h_v3.z)
            end_v3 = v.Vec3(h_v3.x + c_len - 1, y, h_v3.z + e_len - 1 )
        elif orientation == 1:
            start_v3 = v.Vec3(h_v3.x - (e_len - 1), y, h_v3.z)
            end_v3 = v.Vec3(h_v3.x, y, h_v3.z + c_len - 1 )
        elif orientation == 2:
            start_v3 = v.Vec3(h_v3.x - (c_len - 1), y, h_v3.z - (e_len - 1))
            end_v3 = v.Vec3(h_v3.x, y, h_v3.z)
        elif orientation == 3:
            start_v3 = v.Vec3(h_v3.x, y, h_v3.z - (c_len - 1))
            end_v3 = v.Vec3(h_v3.x + (e_len - 1), y, h_v3.z)
        roof = c.roof.Roof(start_v3, end_v3, stair_block, slab_block, cube_block)
        house.components.append(roof)
    def _design_internal_walls(self, house):
        layout = house.layout
        internal_wall_layouts = layout['internal_walls']
        orientation = house.orientation
        e_v3 = house.property_v3
        hx, hy, hz = house.house_v3
        g_v3 = v.Vec3(e_v3.x, e_v3.y, e_v3.z)
        for internal_wall_layout in internal_wall_layouts:
            for floor_elevation in house.floor_elevations:
                (x,y,z) = self._orientate(g_v3, orientation, internal_wall_layout['e_offset'], internal_wall_layout['c_offset'], internal_wall_layout['e_len'], internal_wall_layout['c_len'])[0]
                y += floor_elevation
                (x2,y2,z2) = self._orientate(v.Vec3(x,y,z), orientation, internal_wall_layout['e_len'] - 1, internal_wall_layout['c_len'] - 1)[0]
                y2 += 2
                block = random.choice(b.OPTIONS[house.theme]['wall']['basic'])
                internal_wall = c.wall.Wall(v.Vec3(x,y,z), v.Vec3(x2, y2, z2), block)
                house.components.append(internal_wall)

        pass
    def _design_paths(self, property):
        e_v3 = property.entrance_edge['start']
        g_v3 = v.Vec3(e_v3.x, e_v3.y - 1, e_v3.z)
        orientation = property.orientation
        path_layouts = property.layout.layout['paths']
        for path_layout in path_layouts:
            (x,y,z) = self._orientate(g_v3, orientation, path_layout['e_offset'], path_layout['c_offset'], path_layout['e_len'], path_layout['c_len'])[0]
            (x2,y2,z2) = self._orientate(v.Vec3(x,y,z), orientation, path_layout['e_len'] - 1, path_layout['c_len'] - 1)[0]
            block = random.choice(b.OPTIONS[property.theme.name]['path']['basic'])
            path = c.path.Path(v.Vec3(x,y,z), v.Vec3(x2, y2, z2), block)
            property.components.append(path)
        pass
    def _design_doors(self, house):
        doors = []
        layout = house.layout
        orientation = house.orientation
        pool_door_e_offset = layout['pool_door_e_offset']
        pool_door_c_offset = layout['pool_door_c_offset']
        pool_door_orientation = layout['pool_door_orientation']
        front_door_e_offset = layout['front_door_e_offset']
        front_door_c_offset = layout['front_door_c_offset']
        front_door_orientation = layout['front_door_orientation']
        x, y, z = house.property_v3
        elevated_v3 = v.Vec3(x, y + house.floor_elevations[0], z)
        pool_door_v3 = self._orientate(elevated_v3, orientation, pool_door_e_offset, pool_door_c_offset)[0]
        door_orientation = self._get_absolute_door_orientation(orientation, pool_door_orientation)
        top_block = random.choice(b.OPTIONS[house.theme]['door']['basic']).withData(8)
        bot_block = top_block.withData(door_orientation)
        doors.append(c.door.Door(pool_door_v3, top_block, bot_block, orientation))
        front_door_v3 = self._orientate(elevated_v3, orientation, front_door_e_offset, front_door_c_offset)[0]
        door_orientation = self._get_absolute_door_orientation(orientation, front_door_orientation)
        top_block = random.choice(b.OPTIONS[house.theme]['door']['basic']).withData(8)
        bot_block = top_block.withData(door_orientation)
        doors.append(c.door.Door(front_door_v3, top_block, bot_block, orientation))
        for door in doors:
            house.components.append(door)
        pass
    def _get_absolute_door_orientation(self, house_orientation, door_orientation):
        absolute_orientation = (house_orientation + 2+ door_orientation) % 4
        return absolute_orientation
    def _design_external_walls(self, house):
        wall_wraps = []
        orientation = house.orientation
        e_offset = house.layout['e_len'] - 1
        c_offset = house.layout['c_len'] - 1
        wall_block = random.choice(b.OPTIONS[house.theme]['wall']['basic'])
        for i, floor_elevation in enumerate(house.floor_elevations):
            x, y, z = house.house_v3
            y += floor_elevation
            (x2, y2, z2) = self._orientate(house.house_v3, orientation, e_offset, c_offset)[0]
            y2 += 2 + floor_elevation
            wall_wrap = c.wall.WallWrap(v.Vec3(x, y, z), v.Vec3(x2, y2, z2), wall_block, i)
            wall_wraps.append(wall_wrap)
        for wall_wrap in wall_wraps:
            house.components.append(wall_wrap)
    def _design_walls(self, house):
        self._design_external_walls(house)
        pass
    def _get_random_total_levels(self, e_len, c_len):
        total_levels = None
        print(f"E LEN: {e_len}")
        print(f"C_LEN: {c_len}")
        if (e_len >= 8 and (c_len == 11 or c_len == 8 or c_len == 7)):
            # total_levels = random.choice([1, 2])
            total_levels = 2        # HARD CODED FOR TESTING
        else: 
            total_levels = 1
        return total_levels
    def _design_stairs(self, house):
        orientation = house.orientation
        block_up, block_down = self._get_correct_stairs_pair(house.theme, orientation)
        stairs = []
        e_len = 4
        c_len = 1
        c_offset_stairs = None
        house_position = house.position
        if house_position == 'middle':
            c_offset_stairs = random.choice([4, 6])
        elif house_position == 'left':
            c_offset_stairs = 1
        elif house_position == 'right':
            c_offset_stairs = house.layout['c_len'] - 2
        floor_v3 = v.Vec3(house.house_v3.x, house.house_v3.y + house.floor_elevations[0], house.house_v3.z)
        v3 = self._orientate(floor_v3, orientation, 2, c_offset_stairs, e_len, c_len)[0]
        x, y, z = v3
        for i in range(house.total_levels - 1):
            stairs.append(c.stairs.Stairs((x, y, z), orientation, block_up, block_down))
            y += 4
        for stair_component in stairs:
            house.components.append(stair_component)
    def _get_correct_door_pair(self, theme, orientation):
        if orientation == 0:
            top = 8
            bottom = 1
        elif orientation == 1:
            top = 8
            bottom = 2
        elif orientation == 2:
            top = 8
            bottom = 3
        elif orientation == 3:
            top = 8
            bottom = 0
        stair_block = random.choice(b.OPTIONS[theme]['door']['basic'])
        door_top = stair_block.withData(top)
        door_bottom = stair_block.withData(bottom)
        return door_top, door_bottom
    def _get_correct_stairs_pair(self, theme, orientation):
        if orientation == 0:
            up = 2
            down = 7
        elif orientation == 1:
            up = 1
            down = 4
        elif orientation == 2:
            up = 3
            down = 6
        elif orientation == 3:
            up = 0
            down = 5
        stair_block = random.choice(b.OPTIONS[theme]['stairs']['basic'])
        block_up = stair_block.withData(up)
        block_down = stair_block.withData(down)
        return block_up, block_down
    def _design_house(self, property):
        house = c.house.House()
        house_layout = property.layout.layout['house']
        house.layout = house_layout
        house.theme = property.theme.name
        e_len = house_layout['e_len']
        c_len = house_layout['c_len']    
        total_levels = self._get_random_total_levels(e_len, c_len)
        house.total_levels = total_levels
        e_offset = house_layout['e_offset']
        c_offset = house_layout['c_offset']
        e_v3 = property.entrance_edge['start']
        house.property_v3 = e_v3
        orientation = property.orientation
        house.orientation = orientation
        house.position = house_layout['position']
        h_v3 = self._orientate(e_v3, orientation, e_offset, c_offset)[0]
        h_end_v3 = self._orientate(e_v3, orientation, e_offset + (e_len - 1), c_offset + (c_len - 1))[0]
        house.house_v3 = h_v3
        house.end_v3 = h_end_v3
        property.house = house
        property.components.append(house)
    def _orientate(self, v3, orientation=0, e_offset=0, c_offset=0, e_len=1, c_len=1):
        orientated_v3 = None
        x_len = None
        z_len = None
        if orientation == 0:
            orientated_v3 = v.Vec3(v3.x + c_offset, v3.y, v3.z + e_offset)
            z_len = e_len
            x_len = c_len
        elif orientation == 1:
            orientated_v3 = v.Vec3(v3.x - e_offset, v3.y, v3.z + c_offset)
            z_len = c_len
            x_len = e_len
        elif orientation == 2:
            orientated_v3 = v.Vec3(v3.x - c_offset, v3.y, v3.z - e_offset)
            z_len = e_len
            x_len = c_len
        elif orientation == 3:
            orientated_v3 = v.Vec3(v3.x + e_offset, v3.y, v3.z - c_offset)
            z_len = c_len
            x_len = e_len
        return orientated_v3, z_len, x_len
    def _design_floors(self, house):
        total_levels = house.total_levels
        root_v3 = house.house_v3
        end_v3 = house.end_v3
        floors = []
        # elevation = random.choice([0, 1])
        elevation = 1
        for floor_level in range(total_levels):
            house.floor_elevations.append(elevation)
            floor_block = random.choice(b.OPTIONS[house.theme]['floor']['basic'])
            floors.append(c.floor.Floor(root_v3, end_v3, floor_block, floor_level, elevation))
            elevation += 4
        for floor in floors:
            house.components.append(floor)
            print(floor)
    def _design_level(self, level):
        total_rooms = random.choice(1,2)
        pass
    def _design_entrance(self, property):
        root_v3 = property.entrance_edge['start']
        orientation = property.orientation
        heights = [1, 2, 3]
        random_height = random.choice(heights)
        fence_block = random.choice(b.OPTIONS[property.theme.name]['boundary']['basic'])
        gate_block = random.choice(b.OPTIONS[property.theme.name]['gate']['basic'])
        entrance = c.entrance.Entrance(root_v3, orientation, random_height, fence_block, gate_block)
        print("Entrance design completed\n")
        print(entrance)
        property.components.append(entrance)
    def _design_boundary(self, property):
        fence_block = random.choice(b.OPTIONS[property.theme.name]['boundary']['basic'])
        boundary = c.boundary.Boundary(fence_block)
        print("Boundary design completed\n")
        print(boundary)
        property.components.append(boundary)
    def _design_pool(self, property):
        line_block = random.choice(b.OPTIONS[property.theme.name]['pool_line']['basic'])
        fill_block = random.choice(b.OPTIONS[property.theme.name]['pool_fill']['basic'])
        fence_block = random.choice(b.OPTIONS[property.theme.name]['fence']['basic'])
        line_v3 = {}
        fill_v3 = {}
        fence_v3 = {}
        gate_v3 = None
        line_depth = 1
        position = property.layout.layout['pool']['position']
        e_offset = property.layout.layout['pool']['e_offset']
        c_offset = property.layout.layout['pool']['c_offset']
        e_len = property.layout.layout['pool']['e_len']
        c_len = property.layout.layout['pool']['c_len']
        e_v3 = property.entrance_edge['start']
        orientation = property.orientation
        gate_block = None
        if position == 'back':
            if orientation == 0 or orientation == 2:
                gate_block = random.choice(b.OPTIONS[property.theme.name]['gate']['pool']).withData(0)
            else:
                gate_block = random.choice(b.OPTIONS[property.theme.name]['gate']['pool']).withData(1)
        else:
            if orientation == 0 or orientation == 2:
                gate_block = random.choice(b.OPTIONS[property.theme.name]['gate']['pool']).withData(1)
            else:
                gate_block = random.choice(b.OPTIONS[property.theme.name]['gate']['pool']).withData(0)
        line_raise = 0
        gate_e_offset = property.layout.layout['pool']['gate_e_offset']
        gate_c_offset = property.layout.layout['pool']['gate_c_offset']
        gate_v3 = self._orientate(e_v3, orientation, gate_e_offset, gate_c_offset)[0]
        (x, y, z) = self._orientate(e_v3, orientation, e_offset, c_offset)[0]
        line_v3['start'] = v.Vec3(x,y + (line_raise - 1),z)
        fence_v3['start'] = v.Vec3(x, y + line_raise, z)
        (x, y, z) = self._orientate(line_v3['start'], orientation, line_depth, line_depth)[0]
        fill_v3['start'] = v.Vec3(x, y - line_raise, z)
        x, y, z = line_v3['start']
        (x, y, z) = self._orientate(e_v3, orientation, e_offset + e_len - 1, c_offset + c_len - 1)[0]
        pool_depth = random.choice([2, 3, 4])
        line_v3['end'] = v.Vec3(x, y - (pool_depth + 1), z)
        fence_v3['end'] = v.Vec3(line_v3['end'].x, line_v3['end'].y + pool_depth + 1, line_v3['end'].z)
        (x, y, z) = self._orientate(line_v3['end'], orientation, line_depth * -1, line_depth * -1)[0]
        fill_v3['end'] = v.Vec3(x, y + 1, z)
        # TODO: Use position to make fence and gate for pool
        # position = property.layout.layout['pool']['position']
        pool = c.pool.Pool(line_v3, fill_v3, fence_v3, gate_v3, line_block, fill_block, fence_block, gate_block, pool_depth, line_raise, line_depth)
        print("Pool design completed\n")
        print(pool)
        property.components.append(pool)

class Diego(Designer):
    name = 'Diego'

# TESTING

if __name__ == '__main__':
    from mcpi import minecraft
    import architect as a
    mc = minecraft.Minecraft.create()

    v3 = mc.player.getPos()
    architect = a.Jin()
    print(f"✅ Architect created.\n\narchitect.name: {architect.name}\n")
    orientation = 2
    theme = 'medi'
    architect.give_specs(v3, orientation, theme, mc)
    for property in architect.properties:
        print(f"Property is_built: {property.is_built}")