from mcpi import vec3 as v
import random
import property as p
import block as b
import components as c


class Designer:
    name = None
    properties = []
    def __init__(self):
        pass
    def give_specs(self, property):
        self.properties.append(property)
        self._design_components(property)
        pass
    def _design_components(self, property):
        self._design_entrance(property)
        self._design_boundary(property)
        self._design_pool(property)
        pass
    def _design_house(self, property):
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
        property.components['entrance'] = entrance
    def _design_boundary(self, property):
        boundary = c.boundary.Boundary(property.components['entrance'].fence_block)
        print("Boundary design completed\n")
        print(boundary)
        property.components['boundary'] = boundary
    def _design_pool(self, property):
        v3 = None
        z_len = 0
        x_len = 0
        orientation = 0      # TODO: based on property orientation and pool position
        line_block = None
        fill_block = None
        pool_depth = None
        line_raise = None
        line_depth = 1
        e_offset = property.layout.layout['pool']['e_offset']
        c_offset = property.layout.layout['pool']['c_offset']
        e_len = property.layout.layout['pool']['e_len']
        c_len = property.layout.layout['pool']['c_len']
        e_v3 = property.entrance_edge['start']
        if property.orientation == 0:
            v3 = v.Vec3(e_v3.x + c_offset, e_v3.y, e_v3.z + e_offset)
            z_len = e_len
            x_len = c_len
        elif property.orientation == 1:
            v3 = v.Vec3(e_v3.x - e_offset, e_v3.y, e_v3.z + c_offset)
            z_len = c_len
            x_len = e_len
        elif property.orientation == 2:
            v3 = v.Vec3(e_v3.x - c_offset, e_v3.y, e_v3.z - e_offset)
            z_len = e_len
            x_len = c_len
        elif property.orientation == 3:
            v3 = v.Vec3(e_v3.x + e_offset, e_v3.y, e_v3.z - c_offset)
            z_len = c_len
            x_len = e_len
        line_block = random.choice(b.OPTIONS[property.theme.name]['pool_line']['basic'])
        fill_block = random.choice(b.OPTIONS[property.theme.name]['pool_fill']['basic'])
        pool_depth = random.choice([2, 3, 4])
        line_raise = random.choice([0,1,2])
        pool = c.pool.Pool(v3, z_len, x_len, orientation, line_block, fill_block, pool_depth, line_raise, line_depth)
        print("Pool design completed\n")
        print(pool)
        property.components['pool'] = pool
    def _set_gate_v3(self):
        v3 = self.fence_v3['start']
        h = self.height
        start_v3 = None
        end_v3 = None
        if self.orientation == 0:
            start_v3 = v.Vec3(v3.x + (self.length // 2), v3.y, v3.z)
            end_v3 = v.Vec3(start_v3.x, start_v3.y + self.height - 1, start_v3.z)
        elif self.orientation == 1:
            start_v3 = v.Vec3(v3.x, v3.y, v3.z + (self.length // 2))
            end_v3 = v.Vec3(start_v3.x, start_v3.y + self.height - 1, start_v3.z)
        elif self.orientation == 2:
            start_v3 = v.Vec3(v3.x - (self.length // 2), v3.y, v3.z)
            end_v3 = v.Vec3(start_v3.x, start_v3.y + self.height - 1, start_v3.z)
        elif self.orientation == 3:
            start_v3 = v.Vec3(v3.x, v3.y, v3.z - (self.length // 2))
            end_v3 = v.Vec3(start_v3.x, start_v3.y + self.height - 1, start_v3.z)
        self.gate_v3['start'] = start_v3
        self.gate_v3['end'] = end_v3

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