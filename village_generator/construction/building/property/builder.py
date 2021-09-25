from mcpi import minecraft
from .util import Logbook
from .property import Property
import property as p
import tradies as t
import mcpi as m

class Builder:
    name = None
    emoji = '👷‍♂️'
    properties = []
    tradies = {

    }
    def __init__(self):
        print(f"{self.emoji} Builder created.\n")
        if self.name:
            print(f"builder.name: {self.name}\n")
        self.TRADIES = {
            'bed': t.decorator.Decorator(),
            'boundary': t.jims_fencing.JimsFencing(),
            'carpets': t.carpet_call.CarpetCall(),
            'chimney': t.mason.Mason(),
            'decoration': t.decorator.Decorator(),
            'door': t.carpenter.Carpenter(),
            'entrance': t.jims_fencing.JimsFencing(),
            'fireplace': t.mason.Mason(),
            'floor': t.floor_installer.FloorInstaller(),
            'flower_bed': t.gardener.Gardener(),
            'garden': t.gardener.Gardener(),
            'path': t.landscaper.Landscaper(),
            'pool': t.pool_installer.PoolInstaller(),
            'stairs': t.carpenter.Carpenter(),
            'room': t.mason.Mason(),
            'roof': t.roofer.Roofer(),
            'steps': t.carpenter.Carpenter(),
            'tree': t.gardener.Gardener(),
            'veggie_patch': t.gardener.Gardener(),
            'wall': t.mason.Mason(),
            'wall_wrap': t.mason.Mason(),
            'window': t.window_maker.WindowMaker()
        }
        pass
    # Public Functions
    def assign_property(self, property: Property, mc: minecraft.Minecraft) -> None:
        self.properties.append(property)
        self.logbook = Logbook(self)
        self.logbook.logs.append(f'{self.emoji} Assigned property.\n')
        # self._print()
        self._build_property(property, mc)
    # Internal Methods
    def _build_property(self, property, mc) -> None:
        self.logbook.logs.append(f"{self.emoji} Commencing property build...\n") 
        # self._print()
        all_components = property.components + property.house.components
        for component in all_components:
            if component.type == 'house':
                continue
            else:
                self._assign_tradie(component.type, component, mc)
        property.is_built = True
        self.logbook.logs.append(f"✅ Completed property build.\n")
        # self._print()
        return None
    def _assign_tradie(self, component_type, component, mc):
        self.logbook.logs.append(f"{self.emoji} Assigning {component_type} to tradie...\n")
        # self._print()
        tradie = self.TRADIES[component_type]
        tradie.build_component(component, mc)
    def _print(self):
        print(self.logbook.logs[-1])

        # TODO: Use components to randomly build components
        pass

class Bob(Builder):
    name = 'Bob'
