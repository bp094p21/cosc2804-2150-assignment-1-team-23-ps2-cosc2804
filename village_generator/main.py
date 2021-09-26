from mcpi.minecraft import Minecraft
from core.village.village_builder import build_village
from core.village.village_size import VillageSize
import random

# The main class file where all the action happens (not really - just a few lines)!


if __name__ == '__main__':
    mc = Minecraft.create()

    x, y, z = mc.player.getTilePos()

    # Integer representation of each village:
    # 0 -- SMALL
    # 1 -- MEDIUM
    # 2 -- LARGE
    rand = random.randint(0, 2) 
    
    village_size = 'SMALL' if rand == 0 else ('MEDIUM' if rand == 1 else 'LARGE')
    mc.postToChat(f'A {village_size.lower()} village has been selected. Sit tight whilst we get to work!')

    # Upon invocation will generate a village where the player is standing.
    build_village(VillageSize[village_size.upper()], (x + 1, y, z + 1), mc.player.getBiome(), mc)