from mcpi import minecraft
from mcpi import vec3 as v

import builder as b
import designer as d
import layout as l
import property as p
import theme as t

import util.logbook as lb

class Architect():
    name = None
    emoji = '👔'
    properties = []
    designer = None
    builder = None
    def __init__(self):
        print(f"{self.emoji} Architect created.\n")
        if self.name:
            print(f"architect.name: {self.name}\n")
    # Public Functions
    def give_specs(self, location_v3: v.Vec3, orientation: int, theme_str: str, mc: minecraft.Minecraft, plot_length=15) -> None:
        self.logbook = lb.Logbook(self)
        self.logbook.logs.append(f'{self.emoji} Specs received for property.\n\nLocation: {location_v3},\nOrientation: {orientation},\nTheme: {theme_str}\n')
        self._print()
        self._draft_property(location_v3, orientation, theme_str, plot_length)
        self._get_designer()
        self._get_component_specs()
        self._get_builder()
        self._build_property(mc)
    # Interal Methods
    def _draft_property(self, v3, orientation, theme_str, plot_length):
        self.logbook.logs.append(f'{self.emoji} Drafting property...\n')
        self._print()
        entrance_edge = self._get_entrance_edge(v3, orientation, plot_length)
        theme = self._set_theme(theme_str)
        house_type = self._set_house_type(theme)
        layout = self._set_layout(house_type, entrance_edge, orientation, plot_length)
        property = p.Property(v3, orientation, theme, entrance_edge, house_type, layout)
        self.properties.append(property)
        self.logbook.logs.append(f'✅ Property drafted.')
    def _get_entrance_edge(self, v3, orientation, plot_length):
        self.logbook.logs.append(f'{self.emoji} Getting entrance edge...\n')
        self._print()
        start = None
        end = None
        if orientation == 0:
            start = v3
            end = v.Vec3(v3.x + plot_length - 1, v3.y, v3.z)
        elif orientation == 1:
            start = v.Vec3(v3.x + plot_length - 1, v3.y, v3.z)
            end = v.Vec3(v3.x + plot_length - 1, v3.y, v3.z + plot_length - 1)
        elif orientation == 2:
            start = v.Vec3(v3.x + plot_length - 1, v3.y, v3.z + plot_length - 1)
            end = v.Vec3(v3.x, v3.y, v3.z + plot_length - 1)
        elif orientation == 3:
            start = v.Vec3(v3.x, v3.y, v3.z + plot_length - 1)
            end = v3
        self.logbook.logs.append(f'✅ Entrance edge set.\n\nstart: {start},\nend: {end}\n')
        self._print()
        return {'start': start, 'end': end}
    def _set_theme(self, theme_str) -> t.Theme:
        self.logbook.logs.append(f'{self.emoji} Setting theme...\n')
        self._print()
        theme = t.get_theme(theme_str)
        self.logbook.logs.append(f"✅ Property theme set: {theme.name}\n")
        self._print()
        return theme
    def _set_house_type(self, theme: t.Theme) -> str:
        self.logbook.logs.append(f'{self.emoji} Setting house type...\n')
        self._print()
        house_type = theme.house_type
        self.logbook.logs.append(f"✅ House type set: {house_type}\n")
        self._print()
        return house_type
    def _set_layout(self, house_type, entrance_edge, orientation, plot_length) -> l.Layout:
        self.logbook.logs.append(f'{self.emoji} Setting property layout...\n')
        self._print()
        layout = l.get_layout(house_type, entrance_edge, orientation, plot_length)
        self.logbook.logs.append(f"✅ Property layout set: {layout.name}\n")
        self._print()
        return layout
    def _get_designer(self):
        self.logbook.logs.append(f'{self.emoji} Getting designer...\n')
        self._print()
        self.designer = d.Designer()
        self.logbook.logs.append(f'✅ Designer on board\n')
        self._print()
    def _get_component_specs(self) -> dict:
        self.logbook.logs.append(f'{self.emoji} Getting components from designer...\n')
        self._print()
        self.designer.give_specs(self.properties[-1])
        self.logbook.logs.append(f"✅ Property components set\n")
        self._print()
    def _get_builder(self):
        self.logbook.logs.append(f'{self.emoji} Getting builder...\n')
        self._print()
        self.builder = b.Bob()
        self.logbook.logs.append(f'✅ Got builder\n')
        self._print()
    def _build_property(self, mc):
        self.logbook.logs.append(f'{self.emoji} Assigning builder to property...\n')
        self._print()
        self.builder.assign_property(self.properties[-1], mc)
        self.logbook.logs.append(f'✅ Builder assigned to property\n')
        self._print()
    def _print(self):
        print(self.logbook.logs[-1])

class Jin(Architect):
    name = 'Jin'

# TESTING
if __name__ == '__main__':
    mc = minecraft.Minecraft.create()
    v3 = mc.player.getTilePos()
    architect = Jin()
    orientation = 0
    theme = 'medi'
    architect.give_specs(v3, orientation, theme, mc)
    print(architect.logbook)
    print(architect.properties)
    print(architect.builder.name)
    for property in architect.properties:
        print(f"Property is_built: {property.is_built}")
