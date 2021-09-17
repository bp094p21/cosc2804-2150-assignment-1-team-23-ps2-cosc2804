from mcpi import vec3
import theme as t
import layout as l
import components

class Property:
    # __init__ inputs
    location_v3: vec3.Vec3 = None 
    orientation = None
    theme: t.Theme = None       
    entrance_edge: dict = None
    house_type: str = None      
    layout: l.Layout = None     
    components: dict = {        
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
    is_built = False

    # Public functions
    def __init__(self, location_v3: vec3.Vec3, orientation: int, theme, entrance_edge: dict, house_type: str, layout: l.Layout, components = {}) -> None:
        self.location_v3 = location_v3
        self.location_str = f"\nx: {location_v3.x}\ny: {location_v3.y}\nz: {location_v3.z}\n"
        self.orientation = orientation
        self.theme = theme
        self.entrance_edge = entrance_edge
        self.house_type = house_type
        self.layout = layout
        self.components = components
        return None
    def __repr__(self):
        return f"🖨  Printing object.__repr__:\n\n{type(self)}\n\nlocation_v3: {self.location_v3},\norientation: {self.orientation},\ntheme: {self.theme.name},\nhouse_type: {self.house_type},\nis_built: {self.is_built}"
    # Internal methods
    def _instantiate_components(self):
        # TODO: Use layout to randomly instantiate components to build
        pass
