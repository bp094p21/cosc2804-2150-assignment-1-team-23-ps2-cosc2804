from mcpi import minecraft
import util.logbook as l
import property as p
import tradies as t
import mcpi as m

class Builder:
    name = None
    properties = []
    tradies = {

    }
    def __init__(self):
        pass
    # Public Functions
    def assign_property(self, property: p.Property, mc: minecraft.Minecraft) -> None:
        self.properties.append(property)
        self.logbook = l.Logbook(self)
        self.logbook.logs.append(f'Assigned property:\n{property}')
    # Internal Methods
    def _build_property(self) -> None:
        self.p.status = f"🚧 Commencing property build at location:\n{self.p.location_str}"
        self.p.print_status()
        self._build_components()
        self.p.status = f"✅ Completed property build at location:\n{self.p.location_str}"
        self.p.print_status()
        return None
    def _build_components(self):
        # TODO: Use components to randomly build components
        pass

class Bob(Builder):
    name = 'Bob'

TRADIE = {
    'carpets': t.carpet_call.CarpetCall(),
    'decoration': t.decorator.Decorator(),
    'boundary': t.jims_fencing.JimsFencing(),
    'floor': t.floor_installer.FloorInstaller(),
    'room': t.mason.Mason(),
    'roof': t.roofer.Roofer(),
    'steps': t.carpenter.Carpenter(),
    'wall': {
        'stone': t.mason.Mason(),
        'brick': t.mason.Mason(),
        'timber': t.carpenter.Carpenter(),
        'concrete': t.mason.Mason()
    },
    'stairs': t.carpenter.Carpenter(),
    'pool': t.pool_installer.PoolInstaller(),
    'entrance': t.jims_fencing.JimsFencing(),
    'garden': t.gardener.Gardener(),
    'veggie_patch': t.gardener.Gardener(),
    'fireplace': t.mason.Mason(),
    'chimney': t.mason.Mason()
}