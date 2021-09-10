from mcpi.minecraft import Minecraft

# Main class file. The VillageBuilder will be called from here to build a village on player request (onCommand event).

mc = Minecraft.create()
mc.postToChat("Hello world")