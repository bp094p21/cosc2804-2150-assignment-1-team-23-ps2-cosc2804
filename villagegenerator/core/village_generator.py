from mcpi.minecraft import Minecraft

# Main class file. The VillageBuilder will be called from here to construction a village on player request (onCommand event).


if __name__ == '__main__':
    mc = Minecraft.create()
    mc.postToChat('Generating village...')

    x, y, z = mc.player.getTilePos()

    ply_coords = (x + 1, y + 1, z)

    ply_biome = mc.getBiome()

    mc.postToChat('Done!')
