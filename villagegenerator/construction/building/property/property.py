from mcpi import vec3
from mcpi import minecraft
import theme

class Property:
    # __init__ inputs
    location_vec3: vec3.Vec3 = None 
    entrance_edge: int = None
    biome: int = None
    mc: minecraft.Minecraft = None
    # Derived properties
    theme: str = None       # Set by biome
    house_type: str = None      # Set by theme
    components: dict = {        # Set by house_type
        'entrance': None,
        'boundary': None,
        'floors': [],
        'front': None,
        'house': None,
        'pool': None,
        'roof': None
    }
    # Print message utilities
    property_location_str: str = "Location not set"
    build_status: str = "Property not yet instantiated"

    # Public methods
    def __init__(self, location_vec3: vec3.Vec3, entrance_edge: int, biome: int, mc: minecraft.Minecraft):
        self.location_vec3 = location_vec3
        self.property_location_str: str = f"\nx: {location_vec3.x}\ny: {location_vec3.y}\nz: {location_vec3.z}\n"
        self.entrance_edge = entrance_edge
        self.biome = biome
        self.mc = mc
        self.build_status = f"✅ Property object instantiated with location:\n{self.property_location_str}"
        self.print_status()
        pass
    def print_status(self):
        print(self.build_status)
    def build(self):
        self.build_status = f"🚧 Commencing property build at location:\n{self.property_location_str}"
        self.print_status()
        self._set_theme()
        self._random_select_house_type()
        self._instantiate_components()
        self._build_components()
        self.build_status = f"✅ Completed property build at location:\n{self.property_location_str}"
        self.print_status()
    # Internal methods
    def _set_theme(self):
        # TODO: Use biome to set theme
        if self.biome:
            self.theme = theme.ThemeA()
        elif self.biome:
            self.theme = theme.ThemeB()
        elif self.biome:
            self.theme = theme.ThemeC()
        self.build_status = f"✅ Theme set: {self.theme}\n"
        self.print_status()
    def _random_select_house_type(self):
        # TODO: Use theme to randomly select property type from a set of property types applicable to that theme
        self.build_status = f"✅ Property type randomly selected: {self.house_type}"
        pass
    def _instantiate_components(self):
        # TODO: Use house_type to randomly instantiate components to build
        pass
    def _build_components(self):
        # TODO: Use components to randomly build components
        pass
