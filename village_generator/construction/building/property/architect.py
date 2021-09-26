from mcpi import minecraft
from mcpi import vec3 as v

from .builder import Builder, Bob
from .designer import Designer
from .layout import Layout, get_layout
from .property import Property
from .theme import Theme, get_theme

from .util import Logbook


class Architect:
    """Given a Vec3, the Architect will assume it as the corner of least z and x values and build a property of 15 x
    15 block dimensions in the positive z and x direction\nOrientation must also be given. 0 means the property will
    face West, 1 - North, 2 - East and 3 - South\nTheme should be given in string format (Currently ONLY accepts
    'medi').\nA Minecraft object should also be given.\nPlot Length is assumed to be 15 and currently does not
    support any other plot length. """

    name: str = None
    emoji: str = '👔'
    properties: list = []

    logbook: Logbook = None
    designer: Designer = None
    builder: Builder = None

    def __init__(self):
        print(f"{self.emoji} Architect created.\n")
        if self.name:
            print(f"architect.name: {self.name}\n")
        self.logbook = Logbook(self.name)

    # External Call
    def give_specs(self, location_v3: v.Vec3, house, plot_length=15):
        self.logbook.logs.append(
            f'{self.emoji} Specs received for property.\n\nLocation: {location_v3},\nOrientation: {house.orientation},\nTheme: {house.theme}\n')
        # self._print()
        property_orientation = None
        if house.orientation == 0:
            property_orientation = 3
        else:
            property_orientation = (house.orientation - 1) % 4
        self._draft_property(location_v3, property_orientation, house.theme, plot_length)
        self._get_designer()
        self._get_component_specs()
        self._get_builder()
        self._build_property(house.mc_instance)

    # region
    # Interal Methods
    def _draft_property(self, v3, orientation, theme_str, plot_length):
        self.logbook.logs.append(f'{self.emoji} Drafting property...\n')
        # self._print()
        entrance_edge = self._get_entrance_edge(v3, orientation, plot_length)
        theme = self._set_theme(theme_str)
        house_type = self._set_house_type(theme)
        layout = self._set_layout(house_type, plot_length)
        property = Property(v3, orientation, theme, entrance_edge, house_type, layout)
        self.properties.append(property)
        self.logbook.logs.append(f'✅ Property drafted.')

    def _get_entrance_edge(self, v3, orientation, plot_length):
        self.logbook.logs.append(f'{self.emoji} Getting entrance edge...\n')
        # self._print()
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
        # self._print()
        return {'start': start, 'end': end}

    def _set_theme(self, theme_str) -> Theme:
        self.logbook.logs.append(f'{self.emoji} Setting theme...\n')
        # self._print()
        theme = get_theme(theme_str)
        self.logbook.logs.append(f"✅ Property theme set: {theme.name}\n")
        # self._print()
        return theme

    def _set_house_type(self, theme: Theme) -> str:
        self.logbook.logs.append(f'{self.emoji} Setting house type...\n')
        # self._print()
        house_type = theme.house_type
        self.logbook.logs.append(f"✅ House type set: {house_type}\n")
        # self._print()
        return house_type

    def _set_layout(self, house_type, plot_length) -> Layout:
        self.logbook.logs.append(f'{self.emoji} Setting property layout...\n')
        # self._print()
        layout = get_layout(house_type, plot_length)
        self.logbook.logs.append(f"✅ Property layout set: {layout.name}\n")
        # self._print()
        return layout

    def _get_designer(self):
        self.logbook.logs.append(f'{self.emoji} Getting designer...\n')
        # self._print()
        self.designer = Designer()
        self.logbook.logs.append(f'✅ Designer on board\n')
        # self._print()

    def _get_component_specs(self) -> dict:
        self.logbook.logs.append(f'{self.emoji} Getting components from designer...\n')
        # self._print()
        self.designer.give_specs(self.properties[-1])
        self.logbook.logs.append(f"✅ Property components set\n")
        # self._print()

    def _get_builder(self):
        self.logbook.logs.append(f'{self.emoji} Getting builder...\n')
        # self._print()
        self.builder = Bob()
        self.logbook.logs.append(f'✅ Got builder\n')
        # self._print()

    def _build_property(self, mc):
        self.logbook.logs.append(f'{self.emoji} Assigning builder to property...\n')
        # self._print()
        self.builder.assign_property(self.properties[-1], mc)
        self.logbook.logs.append(f'✅ Builder assigned to property\n')
        # self._print()

    # Print Method
    def _print(self):
        print(self.logbook.logs[-1])

# #endregion
# class Jin(Architect):
#     name = 'Jin'

# TESTING
# if __name__ == '__main__':
#     import sys
#     mc = minecraft.Minecraft.create()
#     v3 = mc.player.getTilePos()
#     architect = Architect()
#     orientation = 2
#     theme = 'medi'
#     architect.give_specs(v3, House(mc, orientation, theme))
#     for property in architect.properties:
#         print(f"Property is_built: {property.is_built}")
