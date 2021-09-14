from mcpi import vec3
from mcpi import minecraft
import theme as t
import layout as l
from util import printer

class Property:
    # __init__ inputs
    location_vec3: vec3.Vec3 = None 
    orientation = None
    mc: minecraft.Minecraft = None
    # Derived properties
    entrance_edge: dict['start': vec3.Vec3, 'end': vec3.Vec3] = None
    theme: t.Theme = None       
    house_type: str = None      # Set by theme
    layout: l.Layout = None     # Set by house_type
    components: dict = {        # Set by layout
        'boundary': None,
        'entrance': None,
        'floors': [],
        'front': None,
        'house': None,
        'pool': None,
        'roof': None,
        'rooms': [],
        'sides': [],
        'stairs': [],
        'walls': []
    }
    # Initialize print utilities
    p = printer.Printer("Property not yet instantaited")
    p.location_str = "Location not set"

    # Public methods
    def __init__(self, location_vec3: vec3.Vec3, orientation: int, theme: str, mc: minecraft.Minecraft) -> None:
        self.location_vec3 = location_vec3
        self.p.location_str = f"\nx: {location_vec3.x}\ny: {location_vec3.y}\nz: {location_vec3.z}\n"
        self.orientation = orientation
        self._set_entrance_edge(orientation)
        self._set_theme(theme)
        self._set_house_type()
        self.mc = mc
        self.p.status = f"✅ Property object instantiated with location:\n{self.p.location_str}\nentrance edge: {self.entrance_edge}\ntheme: {self.theme.name}\nhouse_type: {self.house_type}"
        self.p.print_status()
        return None
    def build(self) -> None:
        self.p.status = f"🚧 Commencing property build at location:\n{self.p.location_str}"
        self.p.print_status()
        self._random_select_house_type()
        self._random_select_layout()
        self._instantiate_components()
        self._build_components()
        self.p.status = f"✅ Completed property build at location:\n{self.p.location_str}"
        self.p.print_status()
        return None
    # Internal methods
    def _set_entrance_edge(self, orientation):
        if orientation == 0:
            self.entrance_edge['start'] = self.location_vec3
            self.entrance_edge['end'] = vec3.Vec3(self.location_vec3.x + 14, self.location_vec3.y, self.location_vec3.z)
        elif orientation == 1:
            self.entrance_edge['start'] = vec3.Vec3(self.location_vec3.x + 14, self.location_vec3.y, self.location_vec3.z)
            self.entrance_edge['end'] = vec3.Vec3(self.location_vec3.x + 14, self.location_vec3.y, self.location_vec3.z + 14)
        elif orientation == 2:
            self.entrance_edge['start'] = vec3.Vec3(self.location_vec3.x + 14, self.location_vec3.y, self.location_vec3.z + 14)
            self.entrance_edge['end'] = vec3.Vec3(self.location_vec3.x, self.location_vec3.y, self.location_vec3.z + 14)
        elif orientation == 3:
            self.entrance_edge['start'] = vec3.Vec3(self.location_vec3.x, self.location_vec3.y, self.location_vec3.z + 14)
            self.entrance_edge['end'] = self.location_vec3
        self.p.status = f"✅ Entrance edge set."
        self.p.print_status()
        return None
    def _set_theme(self, theme):
        self.theme = t.get_theme(theme)
        self.p.status = f"✅ Theme set: {self.theme.name}"
        self.p.print_status()
        return None
    def _set_house_type(self) -> None:
        self.house_type = self.theme.house_type
        self.p.status = f"✅ House type set: {self.house_type}"
        self.p.print_status()
        return None
    def _set_layout(self) -> None:
        self.layout = l.get_layout(self.house_type)
    def _instantiate_components(self):
        # TODO: Use layout to randomly instantiate components to build
        pass
    def _build_components(self):
        # TODO: Use components to randomly build components
        pass
