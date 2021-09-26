from mcpi.minecraft import Minecraft
from core.village.village_builder import build_village
from core.village.village_size import VillageSize

# The main class file where all the action happens (not really - just one line)!


if __name__ == '__main__':
    mc = Minecraft.create()

    x, y, z = mc.player.getTilePos()
    block = mc.getBlock(x, y-1, z)

    # Upon invocation will generate a village where the player is standing.
    build_village(VillageSize.LARGE, (x + 1, y, z + 1), mc.player.getBiome(), mc)
    # Create a border
    village_len_large = (15 * 7) + 1
    village_wid_large = (15 * 6) + 1
    comfortable_ground = 40 #Base level for border in order to always be efficient
    mc.setBlocks(x, comfortable_ground, z, x + village_wid_large, y, z, block) 
    mc.setBlocks(x, comfortable_ground, z, x, y, z + village_len_large, block)
    mc.setBlocks(x, comfortable_ground, z + village_len_large, x + village_wid_large, y, z + village_len_large, block)
    mc.setBlocks(x + village_wid_large, comfortable_ground, z, x + village_wid_large, y, z + village_len_large, block)

