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
        self._print()
        self._build_property(property, mc)
    # Internal Methods
    def _build_property(self, property, mc) -> None:
        self.logbook.logs.append(f"🚧 Commencing property build...") 
        self._print()
        for component_type, component in property.components.items():
            self._assign_tradie(component, mc)
        self.logbook.logs.append(f"✅ Completed property build.")
        self._print()
        return None
    def _assign_tradie(self, component, mc):
        self.logbook.logs.append(f"Assigning {component.type} to tradie...")
        self._print()
        tradie = TRADIE[component.type]
        tradie.build_component(component, mc)
    def _print(self):
        print(self.logbook.logs[-1])

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