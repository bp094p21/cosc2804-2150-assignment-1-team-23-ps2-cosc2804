from mcpi.minecraft import Minecraft
from core.village.village_builder import build_village
from core.village.village_size import VillageSize
import random

# The main class file where all the action happens (not really - just one line)!


if __name__ == '__main__':
    mc = Minecraft.create()

    x, y, z = mc.player.getTilePos()
    block = mc.getBlock(x, y-1, z)

    # Upon invocation will generate a village where the player is standing.
    rand_num = random.randint(0, 2) #0 is small, 1 is medium, 2 is large
    if rand_num == 0:
        mc.postToChat('This village being generated to you is of small size. Please wait..')
        build_village(VillageSize.SMALL, (x + 1, y, z + 1), mc.player.getBiome(), mc)
    elif rand_num == 1:
        mc.postToChat('This village being generated to you is of medium size. Please wait..')
        build_village(VillageSize.MEDIUM, (x + 1, y, z + 1), mc.player.getBiome(), mc)
    else:
        mc.postToChat('This village being generated to you is of large size. Please wait..')
        build_village(VillageSize.LARGE, (x + 1, y, z + 1), mc.player.getBiome(), mc)

