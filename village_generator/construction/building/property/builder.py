from mcpi import minecraft
from .util import Logbook
from .property import Property
from .tradie import *


class Builder:
    name = None
    emoji = '👷‍♂️'
    properties = []
    tradies = {}

    def __init__(self):
        print(f"{self.emoji} Builder created.\n")
        if self.name:
            print(f"builder.name: {self.name}\n")
        self.TRADIES = {
            'bed': Decorator(),
            'boundary': JimsFencing(),
            'carpets': CarpetCall(),
            'chimney': Mason(),
            'decoration': Decorator(),
            'door': Carpenter(),
            'entrance': JimsFencing(),
            'fireplace': Mason(),
            'floor': FloorInstaller(),
            'flower_bed': Gardener(),
            'garden': Gardener(),
            'path': Landscaper(),
            'pool': PoolInstaller(),
            'stairs': Carpenter(),
            'room': Mason(),
            'roof': Roofer(),
            'steps': Carpenter(),
            'tree': Gardener(),
            'veggie_patch': Gardener(),
            'wall': Mason(),
            'wall_wrap': Mason(),
            'window': WindowMaker()
        }
        pass

    # Public Functions
    def assign_property(self, property: Property, mc: minecraft.Minecraft):
        self.properties.append(property)
        self.logbook = Logbook(self)
        self.logbook.logs.append(f'{self.emoji} Assigned property.\n')
        # self._print()
        self._build_property(property, mc)

    # Internal Methods
    def _build_property(self, property, mc):
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

    def _assign_tradie(self, component_type, component, mc):
        self.logbook.logs.append(f"{self.emoji} Assigning {component_type} to tradie...\n")
        # self._print()
        tradie = self.TRADIES[component_type]
        tradie.build_component(component, mc)

    def _print(self):
        print(self.logbook.logs[-1])

        # TODO: Use component to randomly build component
        pass


class Bob(Builder):
    name = 'Bob'
