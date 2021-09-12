import theme

class Property:
    # Init Inputs
    corner_vector = (None, None, None)
    entrance_edge = None
    biome = None
    mc = None
    # Set by biome
    theme = None
    # Set by theme
    house_type = None
    # Set by house_type
    components = {
        'entrance': None,
        'boundary': None,
        'floors': [],
        'front': None,
        'house': None,
        'pool': None,
        'roof': None
    }
    # Change throughout build
    build_status = "Property not yet instantiated"
    # Strings
    property_location_str = f"\nx: {corner_vector[2]}\ny: {corner_vector[0]}\nz: {corner_vector[1]}"
    # Public methods
    def __init__(self, corner_vector, entrance_edge, biome, mc):
        self.corner_vector = corner_vector
        self.entrance_edge = entrance_edge
        self.biome = biome
        self.mc = mc
        self.build_status = f"Property object instantiated with co-ordinates:\n{self.property_location_str}"
        self.print_status()
        pass
    def print_status(self):
        print(self.build_status)
    def build(self):
        self.build_status = f"Commencing property build at co-ordinates:{self.property_location_str}"
        self.print_status()
        self._set_theme()
        self._random_select_house_type()
        self._instantiate_components()
        self._build_components()
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
        self.build_status = f"Theme set: {self.theme}"
        self.print_status()
    def _random_select_house_type(self):
        # TODO: Use theme to randomly select property type from a set of property types applicable to that theme
        self.build_status = f"Property type randomly selected: {self.house_type}"
        pass
    def _instantiate_components(self):
        # TODO: Use house_type to randomly instantiate components to build
        pass
    def _build_components(self):
        # TODO: Use components to randomly build components
        pass
