from mcpi.minecraft import Minecraft
from core import build_village
from core import VillageSize

# Main class file. The VillageBuilder will be called from here to construction a village on player request (onCommand
# event).


if __name__ == '__main__':
    mc = Minecraft.create()
    mc.postToChat('Generating village...')

    x, y, z = mc.player.getTilePos()

    # upon invocation will generate a village where the player is standing.
    build_village(VillageSize.SMALL, (x + 1, y, z + 1), mc.getBiome(), mc)

    mc.postToChat('Done!')
