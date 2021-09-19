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
    def _design_house_components(self, house):
        self._design_floors(house)
        self._design_walls(house)
        if house.total_levels >= 2:
            self._design_stairs(house)
        # self._design_rooms(house, levels, e_v3, e_offset, c_offset, e_len, c_len)
        pass
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
            total_levels = random.choice([1, 2])
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
        elevation = random.choice([0, 1])
        for floor_level in range(total_levels):
            house.floor_elevations.append(elevation)
            floor_block = random.choice(b.OPTIONS[house.theme]['floor']['basic'])
            floors.append(c.floor.Floor(root_v3, end_v3, floor_block, floor_level, elevation))
            elevation += 4
        for floor in floors:
            house.components.append(floor)
            print(floor)
    def _design_roof(self, property):
        v3 = None
        e_v3 = property.entrance_edge['start']
        e_offset = property.layout.layout['house']['e_offset']
        c_offset = property.layout.layout['house']['c_offset']
        e_len = property.layout.layout['house']['e_len']
        c_len = property.layout.layout['house']['c_len']    

        roof_block = random.choice(b.OPTIONS[property.theme.name]['roof']['basic'])
        z_len = None
        x_len = None
        elevation = property.components['house'].floor_elevations[-1]
        if property.orientation == 0:
            v3 = v.Vec3(e_v3.x - 1 + c_offset, e_v3.y + elevation, e_v3.z + e_offset - 1)
            z_len = e_len + 2
            x_len = c_len + 2
        elif property.orientation == 1:
            v3 = v.Vec3(e_v3.x - e_offset + 1, e_v3.y + elevation, e_v3.z + c_offset - 1)
            z_len = c_len + 2
            x_len = e_len + 2
        elif property.orientation == 2:
            v3 = v.Vec3(e_v3.x - c_offset + 1, e_v3.y + elevation, e_v3.z - e_offset +1)
            z_len = e_len + 2
            x_len = c_len + 2
        elif property.orientation == 3:
            v3 = v.Vec3(e_v3.x + e_offset, e_v3.y, e_v3.z - c_offset)
            z_len = c_len + 2
            x_len = e_len + 2
        roof = c.roof.Roof(v3, roof_block, z_len, x_len)
        property.components['roof'] = roof
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
        line_v3 = {}
        fill_v3 = {}
        line_depth = 1
        e_offset = property.layout.layout['pool']['e_offset']
        c_offset = property.layout.layout['pool']['c_offset']
        e_len = property.layout.layout['pool']['e_len']
        c_len = property.layout.layout['pool']['c_len']
        e_v3 = property.entrance_edge['start']
        orientation = property.orientation
        line_raise = random.choice([0,1,2])
        (x, y, z) = self._orientate(e_v3, orientation, e_offset, c_offset)[0]
        line_v3['start'] = v.Vec3(x,y + (line_raise - 1),z)
        (x, y, z) = self._orientate(line_v3['start'], orientation, line_depth, line_depth)[0]
        fill_v3['start'] = v.Vec3(x, y - line_raise, z)
        x, y, z = line_v3['start']
        (x, y, z) = self._orientate(e_v3, orientation, e_offset + e_len - 1, c_offset + c_len - 1)[0]
        pool_depth = random.choice([2, 3, 4])
        line_v3['end'] = v.Vec3(x, y - (pool_depth + 1), z)
        (x, y, z) = self._orientate(line_v3['end'], orientation, line_depth * -1, line_depth * -1)[0]
        fill_v3['end'] = v.Vec3(x, y + 1, z)
        # TODO: Use position to make fence and gate for pool
        # position = property.layout.layout['pool']['position']
        pool = c.pool.Pool(line_v3, fill_v3, line_block, fill_block, pool_depth, line_raise, line_depth)
        print("Pool design completed\n")
        print(pool)
        property.components.append(pool)

class Diego(Designer):
    name = 'Diego'

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