# A collection of two data classes to allow interoperability with the property and misc package's system.

class House:
    mc_instance = None
    
    def __init__(self, mc_instance, orientation, theme):
        if mc_instance is None:
            House.mc_instance = mc_instance

        self.orientation = orientation
        self.theme = theme


class Misc:
    mc_instance = None

    def __init__(self, mc_instance, biome):
        if mc_instance is None:
            Misc.mc_instance = mc_instance

        self.biome = biome
