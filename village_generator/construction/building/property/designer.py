from mcpi import vec3 as v
import random

from .property import Property
from .block import *
from .component import *
from .util.vector import orientate


class Designer:
    """Returns an object with external function give_specs that takes a Property object and appends suitable
    component designs to its component list. """
    name = None
    emoji = '🎨'
    properties = []

    def __init__(self):
        print(f"{self.emoji} Designer created.\n")
        if self.name:
            print(f"designer.name: {self.name}\n")

    def give_specs(self, property: Property):
        self.properties.append(property)
        self._design_components(property)

    def _design_components(self, property):
        self._design_property_components(property)
        self._design_house_components(property.house)

    def _design_property_components(self, property):
        self._design_boundary(property)
        self._design_entrance(property)
        self._design_pool(property)
        self._design_house(property)
        self._design_paths(property)
        self._design_outdoor_features(property)
        return None

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
        self._design_beds(house)
        self._design_roof(house)
        # self._design_rooms(house, levels, e_v3, z_offset, x_offset, z_len, x_len)

    def _design_outdoor_features(self, property):
        e_v3 = property.entrance_edge['start']
        orientation = property.orientation
        h_z_offset = property.layout.layout['house']['z_offset']

        for outdoor_feature_layout in property.layout.layout['outdoor_features']:
            z_offset = outdoor_feature_layout['z_offset']
            x_offset = outdoor_feature_layout['x_offset']
            z_len = outdoor_feature_layout['z_len']
            x_len = outdoor_feature_layout['x_len']
            o_v3 = orientate(e_v3, orientation, z_offset, x_offset)
            start_v3 = None

            if orientation == 0:
                start_v3 = v.Vec3(o_v3.x, o_v3.y, o_v3.z)
                x_len, z_len = x_len, z_len
            elif orientation == 1:
                start_v3 = v.Vec3(o_v3.x - (z_len - 1), o_v3.y, o_v3.z)
                x_len, z_len = z_len, x_len
            elif orientation == 2:
                start_v3 = v.Vec3(o_v3.x - (x_len - 1), o_v3.y, o_v3.z - (z_len - 1))
                x_len, z_len = x_len, z_len
            elif orientation == 3:
                start_v3 = v.Vec3(o_v3.x, o_v3.y, o_v3.z - (x_len - 1))
                x_len, z_len = z_len, x_len
            if x_len >= 2 and z_len >= 2:
                option = random.choice(['veggie_patch', 'flower_bed'])

                if option == 'veggie_patch':
                    property.components.append(VeggiePatch(start_v3))
                elif option == 'flower_bed':
                    property.components.append(FlowerBed(start_v3))

            else:
                if h_z_offset == 3:
                    continue

    def _design_beds(self, house):
        h_v3 = house.house_v3
        layout = house.layout
        orientation = house.orientation

        for bed_layout in layout['beds']:
            for elevation in house.floor_elevations:
                z_offset = bed_layout['z_offset']
                x_offset = bed_layout['x_offset']
                bed_orientation = bed_layout['orientation']
                bedhead_v3 = orientate(h_v3, orientation, z_offset, x_offset)
                x, y, z = bedhead_v3
                y += elevation
                bedtail_v3, bedhead_block, bedtail_block = self._get_bed_pair(bedhead_v3, orientation, bed_orientation)
                x2, y2, z2 = bedtail_v3
                y2 += elevation
                bedhead = Bed(v.Vec3(x, y, z), bedhead_block)
                bedtail = Bed(v.Vec3(x2, y2, z2), bedtail_block)
                house.components.append(bedhead)
                house.components.append(bedtail)

    def _get_bed_pair(self, bedhead_v3, orientation, bed_orientation):
        bedtail_v3 = None
        bedhead_block = None
        bedtail_block = None
        sum_orientation = (orientation + bed_orientation) % 4

        if sum_orientation == 0:
            bedtail_v3 = v.Vec3(bedhead_v3.x, bedhead_v3.y, bedhead_v3.z - 1)
            bedhead_block = BED.withData(8)
            bedtail_block = BED.withData(0)
        elif sum_orientation == 1:
            bedtail_v3 = v.Vec3(bedhead_v3.x + 1, bedhead_v3.y, bedhead_v3.z)
            bedhead_block = BED.withData(9)
            bedtail_block = BED.withData(1)
        elif sum_orientation == 2:
            bedtail_v3 = v.Vec3(bedhead_v3.x, bedhead_v3.y, bedhead_v3.z + 1)
            bedhead_block = BED.withData(10)
            bedtail_block = BED.withData(2)
        elif sum_orientation == 3:
            bedtail_v3 = v.Vec3(bedhead_v3.x - 1, bedhead_v3.y, bedhead_v3.z)
            bedhead_block = BED.withData(11)
            bedtail_block = BED.withData(3)
        return bedtail_v3, bedhead_block, bedtail_block

    def _design_door_steps(self, house):
        v3 = house.property_v3
        orientation = house.orientation
        layout = house.layout
        front_step_z_offset = layout['front_step_z_offset']
        front_step_x_offset = layout['front_step_x_offset']
        pool_step_z_offset = layout['pool_step_z_offset']
        pool_step_x_offset = layout['pool_step_x_offset']
        front_step_v3 = orientate(v3, orientation, front_step_z_offset, front_step_x_offset)
        pool_step_v3 = orientate(v3, orientation, pool_step_z_offset, pool_step_x_offset)
        front_step_block = random.choice(OPTIONS[house.theme]['steps']['basic'])
        pool_step_block = random.choice(OPTIONS[house.theme]['steps']['basic'])
        front_step = Steps(front_step_v3, front_step_block)
        pool_step = Steps(pool_step_v3, pool_step_block)
        house.components.append(front_step)
        house.components.append(pool_step)

    def _design_internal_doors(self, house):
        h_v3 = house.house_v3
        orientation = house.orientation
        theme = house.theme

        for internal_door_layout in house.layout['internal_doors']:
            internal_door_orientation = internal_door_layout['orientation']
            z_offset = internal_door_layout['z_offset']
            x_offset = internal_door_layout['x_offset']

            for floor_elevation in house.floor_elevations:
                elevated_v3 = v.Vec3(h_v3.x, h_v3.y + floor_elevation, h_v3.z)
                v3 = orientate(elevated_v3, orientation, z_offset, x_offset)
                door_orientation = self._get_absolute_door_orientation(orientation, internal_door_orientation)
                top_block = random.choice(OPTIONS[theme]['door']['basic']).withData(8)
                bot_block = top_block.withData(door_orientation)
                internal_door = Door(v3, top_block, bot_block, door_orientation)
                house.components.append(internal_door)

    def _design_windows(self, house):
        window_block = random.choice(OPTIONS[house.theme]['window']['basic'])
        orientation = house.orientation
        h_v3 = house.house_v3

        for window_layout in house.layout['windows']:
            for i, floor_elevation in enumerate(house.floor_elevations):
                z_offset = window_layout['z_offset']
                x_offset = window_layout['x_offset']
                (x, y, z) = orientate(h_v3, orientation, z_offset, x_offset)
                y += i * 4 + 2
                window = Window(v.Vec3(x, y, z), window_block)
                house.components.append(window)

    def _design_roof(self, house):
        style = random.choice([0, 1, 2, 3])
        stair_block = OPTIONS[house.theme]['roof']['stair'][style]
        slab_block = OPTIONS[house.theme]['roof']['slab'][style]
        cube_block = OPTIONS[house.theme]['roof']['cube'][style]
        layout = house.layout
        orientation = house.orientation
        h_v3 = house.house_v3
        y = h_v3.y + house.floor_elevations[-1] + 4
        z_len = layout['z_len']
        x_len = layout['x_len']
        start_v3 = None
        end_v3 = None

        if orientation == 0:
            start_v3 = v.Vec3(h_v3.x, y, h_v3.z)
            end_v3 = v.Vec3(h_v3.x + x_len - 1, y, h_v3.z + z_len - 1)
        elif orientation == 1:
            start_v3 = v.Vec3(h_v3.x - (z_len - 1), y, h_v3.z)
            end_v3 = v.Vec3(h_v3.x, y, h_v3.z + x_len - 1)
        elif orientation == 2:
            start_v3 = v.Vec3(h_v3.x - (x_len - 1), y, h_v3.z - (z_len - 1))
            end_v3 = v.Vec3(h_v3.x, y, h_v3.z)
        elif orientation == 3:
            start_v3 = v.Vec3(h_v3.x, y, h_v3.z - (x_len - 1))
            end_v3 = v.Vec3(h_v3.x + (z_len - 1), y, h_v3.z)

        roof = Roof(start_v3, end_v3, stair_block, slab_block, cube_block)
        house.components.append(roof)

    def _design_internal_walls(self, house):
        layout = house.layout
        internal_wall_layouts = layout['internal_walls']
        orientation = house.orientation
        e_v3 = house.property_v3
        g_v3 = v.Vec3(e_v3.x, e_v3.y, e_v3.z)

        for internal_wall_layout in internal_wall_layouts:
            for floor_elevation in house.floor_elevations:
                (x, y, z) = orientate(g_v3, orientation, internal_wall_layout['z_offset'],
                                      internal_wall_layout['x_offset'])
                y += floor_elevation
                (x2, y2, z2) = orientate(v.Vec3(x, y, z), orientation, internal_wall_layout['z_len'] - 1,
                                         internal_wall_layout['x_len'] - 1)
                y2 += 2
                block = random.choice(OPTIONS[house.theme]['wall']['basic'])
                internal_wall = Wall(v.Vec3(x, y, z), v.Vec3(x2, y2, z2), block)
                house.components.append(internal_wall)

    def _design_paths(self, property):
        e_v3 = property.entrance_edge['start']
        g_v3 = v.Vec3(e_v3.x, e_v3.y - 1, e_v3.z)
        orientation = property.orientation
        path_layouts = property.layout.layout['paths']

        for path_layout in path_layouts:
            (x, y, z) = orientate(g_v3, orientation, path_layout['z_offset'], path_layout['x_offset'])
            (x2, y2, z2) = orientate(v.Vec3(x, y, z), orientation, path_layout['z_len'] - 1, path_layout['x_len'] - 1)
            block = random.choice(OPTIONS[property.theme.name]['path']['basic'])
            path = Path(v.Vec3(x, y, z), v.Vec3(x2, y2, z2), block)
            property.components.append(path)

    def _design_doors(self, house):
        doors = []
        layout = house.layout
        orientation = house.orientation
        pool_door_z_offset = layout['pool_door_z_offset']
        pool_door_x_offset = layout['pool_door_x_offset']
        pool_door_orientation = layout['pool_door_orientation']
        front_door_z_offset = layout['front_door_z_offset']
        front_door_x_offset = layout['front_door_x_offset']
        front_door_orientation = layout['front_door_orientation']

        x, y, z = house.property_v3
        elevated_v3 = v.Vec3(x, y + house.floor_elevations[0], z)

        pool_door_v3 = orientate(elevated_v3, orientation, pool_door_z_offset, pool_door_x_offset)
        door_orientation = self._get_absolute_door_orientation(orientation, pool_door_orientation)
        top_block = random.choice(OPTIONS[house.theme]['door']['basic']).withData(8)
        bot_block = top_block.withData(door_orientation)
        doors.append(Door(pool_door_v3, top_block, bot_block, orientation))

        front_door_v3 = orientate(elevated_v3, orientation, front_door_z_offset, front_door_x_offset)
        door_orientation = self._get_absolute_door_orientation(orientation, front_door_orientation)
        top_block = random.choice(OPTIONS[house.theme]['door']['basic']).withData(8)
        bot_block = top_block.withData(door_orientation)
        doors.append(Door(front_door_v3, top_block, bot_block, orientation))

        for door in doors:
            house.components.append(door)

    def _get_absolute_door_orientation(self, house_orientation, door_orientation):
        absolute_orientation = (house_orientation + 2 + door_orientation) % 4
        return absolute_orientation

    def _design_external_walls(self, house):
        wall_wraps = []
        orientation = house.orientation
        z_offset = house.layout['z_len'] - 1
        x_offset = house.layout['x_len'] - 1
        wall_block = random.choice(OPTIONS[house.theme]['wall']['basic'])

        for i, floor_elevation in enumerate(house.floor_elevations):
            x, y, z = house.house_v3
            y += floor_elevation
            (x2, y2, z2) = orientate(house.house_v3, orientation, z_offset, x_offset)
            y2 += 2 + floor_elevation
            wall_wrap = WallWrap(v.Vec3(x, y, z), v.Vec3(x2, y2, z2), wall_block, i)
            wall_wraps.append(wall_wrap)

        for wall_wrap in wall_wraps:
            house.components.append(wall_wrap)

    def _design_walls(self, house):
        self._design_external_walls(house)

    def _get_random_total_levels(self, z_len, x_len):
        total_levels = None
        print(f"E LEN: {z_len}")
        print(f"x_len: {x_len}")

        if z_len >= 8 and (x_len == 11 or x_len == 8 or x_len == 7):
            # total_levels = random.choice([1, 2])
            total_levels = 2  # HARD CODED FOR TESTING
        else:
            total_levels = 1

        return total_levels

    def _design_stairs(self, house):
        orientation = house.orientation
        block_up, block_down = self._get_correct_stairs_pair(house.theme, orientation)
        stairs = []
        x_offset_stairs = None
        house_position = house.position

        if house_position == 'middle':
            x_offset_stairs = random.choice([4, 6])
        elif house_position == 'left':
            x_offset_stairs = 1
        elif house_position == 'right':
            x_offset_stairs = house.layout['x_len'] - 2

        floor_v3 = v.Vec3(house.house_v3.x, house.house_v3.y + house.floor_elevations[0], house.house_v3.z)
        v3 = orientate(floor_v3, orientation, 2, x_offset_stairs)
        x, y, z = v3

        for i in range(house.total_levels - 1):
            stairs.append(Stairs((x, y, z), orientation, block_up, block_down))
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

        stair_block = random.choice(OPTIONS[theme]['door']['basic'])
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

        stair_block = random.choice(OPTIONS[theme]['stairs']['basic'])
        block_up = stair_block.withData(up)
        block_down = stair_block.withData(down)

        return block_up, block_down

    def _design_house(self, property):
        house = House()
        house_layout = property.layout.layout['house']
        house.layout = house_layout
        house.theme = property.theme.name
        z_len = house_layout['z_len']
        x_len = house_layout['x_len']
        total_levels = self._get_random_total_levels(z_len, x_len)
        house.total_levels = total_levels
        z_offset = house_layout['z_offset']
        x_offset = house_layout['x_offset']
        e_v3 = property.entrance_edge['start']
        house.property_v3 = e_v3
        orientation = property.orientation
        house.orientation = orientation
        house.position = house_layout['position']
        h_v3 = orientate(e_v3, orientation, z_offset, x_offset)
        h_end_v3 = orientate(e_v3, orientation, z_offset + (z_len - 1), x_offset + (x_len - 1))
        house.house_v3 = h_v3
        house.end_v3 = h_end_v3
        property.house = house
        property.components.append(house)

    def _design_floors(self, house):
        total_levels = house.total_levels
        root_v3 = house.house_v3
        end_v3 = house.end_v3
        floors = []
        # elevation = random.choice([0, 1])
        elevation = 1

        for floor_level in range(total_levels):
            house.floor_elevations.append(elevation)
            floor_block = random.choice(OPTIONS[house.theme]['floor']['basic'])
            floors.append(Floor(root_v3, end_v3, floor_block, floor_level, elevation))
            elevation += 4

        for floor in floors:
            house.components.append(floor)
            print(floor)

    def _design_entrance(self, property):
        root_v3 = property.entrance_edge['start']
        orientation = property.orientation
        heights = [1, 2, 3]
        random_height = random.choice(heights)
        fence_block = random.choice(OPTIONS[property.theme.name]['boundary']['basic'])
        gate_block = random.choice(OPTIONS[property.theme.name]['gate']['basic'])
        entrance = Entrance(root_v3, orientation, random_height, fence_block, gate_block)
        print("Entrance design completed\n")
        print(entrance)
        property.components.append(entrance)

    def _design_boundary(self, property):
        root_v3 = property.entrance_edge['start']
        end_v3 = orientate(root_v3, property.orientation, 14, 14)
        fence_block = random.choice(OPTIONS[property.theme.name]['boundary']['basic'])
        boundary = Boundary(root_v3, end_v3, fence_block)
        print("Boundary design completed\n")
        print(boundary)
        property.components.append(boundary)

    def _design_pool(self, property):
        line_block = random.choice(OPTIONS[property.theme.name]['pool_line']['basic'])
        fill_block = random.choice(OPTIONS[property.theme.name]['pool_fill']['basic'])
        fence_block = random.choice(OPTIONS[property.theme.name]['fence']['basic'])
        line_v3 = {}
        fill_v3 = {}
        fence_v3 = {}
        line_depth = 1
        position = property.layout.layout['pool']['position']
        z_offset = property.layout.layout['pool']['z_offset']
        x_offset = property.layout.layout['pool']['x_offset']
        z_len = property.layout.layout['pool']['z_len']
        x_len = property.layout.layout['pool']['x_len']
        e_v3 = property.entrance_edge['start']
        orientation = property.orientation

        if position == 'back':
            if orientation == 0 or orientation == 2:
                gate_block = random.choice(OPTIONS[property.theme.name]['gate']['pool']).withData(0)
            else:
                gate_block = random.choice(OPTIONS[property.theme.name]['gate']['pool']).withData(1)
        else:
            if orientation == 0 or orientation == 2:
                gate_block = random.choice(OPTIONS[property.theme.name]['gate']['pool']).withData(1)
            else:
                gate_block = random.choice(OPTIONS[property.theme.name]['gate']['pool']).withData(0)

        line_raise = 0
        gate_z_offset = property.layout.layout['pool']['gate_z_offset']
        gate_x_offset = property.layout.layout['pool']['gate_x_offset']
        gate_v3 = orientate(e_v3, orientation, gate_z_offset, gate_x_offset)
        (x, y, z) = orientate(e_v3, orientation, z_offset, x_offset)
        line_v3['start'] = v.Vec3(x, y + (line_raise - 1), z)
        fence_v3['start'] = v.Vec3(x, y + line_raise, z)
        (x, y, z) = orientate(line_v3['start'], orientation, line_depth, line_depth)
        fill_v3['start'] = v.Vec3(x, y - line_raise, z)

        x, y, z = line_v3['start']
        (x, y, z) = orientate(e_v3, orientation, z_offset + z_len - 1, x_offset + x_len - 1)
        pool_depth = random.choice([2, 3, 4])
        line_v3['end'] = v.Vec3(x, y - (pool_depth + 1), z)
        fence_v3['end'] = v.Vec3(line_v3['end'].x, line_v3['end'].y + pool_depth + 1, line_v3['end'].z)
        (x, y, z) = orientate(line_v3['end'], orientation, line_depth * -1, line_depth * -1)
        fill_v3['end'] = v.Vec3(x, y + 1, z)

        # TODO: Use position to make fence and gate for pool
        # position = property.layout.layout['pool']['position']
        pool = Pool(line_v3, fill_v3, fence_v3, gate_v3, line_block, fill_block, fence_block, gate_block,
                    pool_depth, line_raise, line_depth)
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
