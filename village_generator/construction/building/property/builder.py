from mcpi import minecraft
import util.logbook as l
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
            'carpets': t.carpet_call.CarpetCall(),
            'decoration': t.decorator.Decorator(),
            'boundary': t.jims_fencing.JimsFencing(),
            'floor': t.floor_installer.FloorInstaller(),
            'room': t.mason.Mason(),
            'roof': t.roofer.Roofer(),
            'steps': t.carpenter.Carpenter(),
            'wall': t.mason.Mason(),
            'wall_wrap': t.mason.Mason(),
            'stairs': t.carpenter.Carpenter(),
            'pool': t.pool_installer.PoolInstaller(),
            'entrance': t.jims_fencing.JimsFencing(),
            'garden': t.gardener.Gardener(),
            'veggie_patch': t.gardener.Gardener(),
            'fireplace': t.mason.Mason(),
            'chimney': t.mason.Mason()
        }
        pass
    # Public Functions
    def assign_property(self, property: p.Property, mc: minecraft.Minecraft) -> None:
        self.properties.append(property)
        self.logbook = l.Logbook(self)
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
