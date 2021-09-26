from mcpi.minecraft import Minecraft
from core.village.village_builder import build_village
from core.village.village_size import VillageSize
import random

# The main class file where all the action happens (not really - just a few lines)!


if __name__ == '__main__':
    mc = Minecraft.create()

    x, y, z = mc.player.getTilePos()
    block = mc.getBlock(x, y-1, z)

    # Upon invocation will generate a village where the player is standing.
    rand_num = random.randint(0, 2) #0 is small, 1 is medium, 2 is large
    if rand_num == 0:
        mc.postToChat('Sit tight whilst we generate a small sized village for you!')
        build_village(VillageSize.SMALL, (x + 1, y, z + 1), mc.player.getBiome(), mc)
    elif rand_num == 1:
        mc.postToChat('Sit tight whilst we generate a medium sized village for you!')
        build_village(VillageSize.MEDIUM, (x + 1, y, z + 1), mc.player.getBiome(), mc)
    else:
        mc.postToChat('Sit tight whilst we generate a large sized village for you!')
        build_village(VillageSize.LARGE, (x + 1, y, z + 1), mc.player.getBiome(), mc)

