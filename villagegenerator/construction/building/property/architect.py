from mcpi import vec3 as v
from mcpi import minecraft

import builder as b
import layout as l
import property as p
import theme as t

import util.logbook as logbook
from util import printer

class Architect():
    name = None
    properties = []
    builder = None
    def __init__(self):
        pass
    # Public Functions
    def give_specs(self, location_v3: v.Vec3, orientation: int, theme: str, mc: minecraft.Minecraft) -> None:
        self.logbook = logbook.Logbook(self)
        self.logbook.logs.append(f'✅ Specs received for property with:\nLocation: {location_v3},\nOrientation: {orientation},\nTheme: {theme}.')
        self._draft_property(location_v3, orientation, theme)
        self._get_builder()
        self._build_property(mc)
    # Interal Methods
    def _draft_property(self, v3, orientation, theme_str):
        entrance_edge = self._get_entrance_edge(v3, orientation)
        theme = self._set_theme(theme_str)
        house_type = self._set_house_type(theme)
        layout = self._set_layout(house_type)
        components = self._set_components(layout)
        property = p.Property(v3, orientation, theme, entrance_edge, house_type, layout, components)
        self.properties.append(property)
        self.logbook.logs.append(f'✅ Drafted property.')
    def _get_entrance_edge(self, v3, orientation):
        pass
    def _set_theme(self, theme_str) -> t.Theme:
        theme = t.get_theme(theme_str)
        self.logbook.logs.append(f"✅ Property theme set: {theme.name}")
        return theme
    def _set_house_type(self, theme: t.Theme) -> str:
        house_type = theme.house_type
        self.logbook.logs.append(f"✅ House type set: {house_type}")
        return house_type
    def _set_layout(self, house_type) -> l.Layout:
        layout = l.get_layout(house_type)
        self.logbook.logs.append(f"✅ Property layout set: {layout}")
        return layout
    def _set_components(self, layout) -> dict:
        # TODO: use layout to set components
        components = None
        self.logbook.logs.append(f"✅ Property components set: {components}")
    def _get_builder(self):
        self.builder = b.Bob()
        self.logbook.logs.append(f'✅ Got builder.')
    def _build_property(self, mc):
        self.builder.assign_property(self.properties[-1], mc)
        self.logbook.logs.append(f'✅ Builder assigned property')
        pass

class Jin(Architect):
    name = 'Jin'

# TESTING
if __name__ == '__main__':
    from mcpi import minecraft
    mc = minecraft.Minecraft.create()
    v3 = mc.player.getPos()
    architect = Jin()
    print(architect.name)
    orientation = 0
    theme = 'medi'
    architect.give_specs(v3, orientation, theme, mc)
    print(architect.logbook)
    print(architect.properties)
    print(architect.builder.name)

    pass