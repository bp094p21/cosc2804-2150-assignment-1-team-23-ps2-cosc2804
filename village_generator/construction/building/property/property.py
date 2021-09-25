from mcpi import vec3
import theme as t
import layout as l


class Property:
    # __init__ inputs
    location_v3: vec3.Vec3 = None
    orientation: int = None
    theme: t.Theme = None
    entrance_edge: dict = None
    house_type: str = None
    layout: l.Layout = None
    # Default attributes
    components: list = []
    is_built: bool = False

    # Initializer
    def __init__(self, location_v3: vec3.Vec3, orientation: int, theme: t.Theme, entrance_edge: dict, house_type: str, layout: l.Layout):
        self.location_v3 = location_v3
        self.orientation = orientation
        self.theme = theme
        self.entrance_edge = entrance_edge
        self.house_type = house_type
        self.layout = layout

    def __repr__(self):
        return f"🖨  Printing {self.__class__.__name__} object details...\n\nlocation_v3: {self.location_v3}," \
               f"\norientation: {self.orientation},\ntheme: {self.theme.name},\nentrance_edge: {self.entrance_edge}," \
               f"\nhouse_type: {self.house_type},\nis_built: {self.is_built}.\n(layout and components not shown)\n "
