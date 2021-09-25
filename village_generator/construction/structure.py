# A data class to allow interoperability with the property package's system.

class House:
    mc_instance = None
    
    def __init__(self, mc_instance, orientation, theme):
        if mc_instance is None:
            mc_instance = mc_instance

        self.orientation = orientation
        self.theme = theme


class Misc:
    mc_instance = None

    def __init__(self, mc_instance, biome):
        if mc_instance is None:
            mc_instance = mc_instance

        self.biome = biome
