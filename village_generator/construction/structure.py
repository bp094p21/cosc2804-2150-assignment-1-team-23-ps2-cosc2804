"""A collection of two data classes to allow interoperability with the property and misc package's system."""


# Represents an individual house.
class House:
    def __init__(self, mc_instance, orientation, theme):
        # A static/class variable for mc_instance would be much more suitable here, as there is only ever going to be one shared instance of the Minecraft class. However,
        # due to time shortage, this has been left out/
        self.mc_instance = mc_instance
        self.orientation = orientation
        self.theme = theme


# Represents an individual misc building.
class Misc:
    def __init__(self, mc_instance, biome):
        self.mc_instance = mc_instance
        self.biome = biome
