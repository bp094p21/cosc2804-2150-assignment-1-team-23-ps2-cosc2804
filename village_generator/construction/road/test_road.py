from mcpi.minecraft import Minecraft
import mcpi.block as block


# FIXME: replace with getLowestYInLine()
def get_lowest_y_in_region(mc, x1, y1, z1, z2):
    lowest = y1

    for k in range(int(z1), int(z2) + 1):
        curr_y = mc.getHeight(x1, k)
        if curr_y < lowest:
            lowest = curr_y

    return lowest


# TODO: only activate the flattener in certain regions where hills are guaranted (biomes).
#  Will be more efficient because in plains biome, there wont be much to flatten.
# x1 and x2 for the only a different z will be the same.
def flatten(mc, x1, y1, z1, z2):
    # have some sort of heuristic that checks if flattening is necessary, and if not, cancels.
    # change y1 + 15 to the highest y block in this region - when implemented on back-end.
    mc.setBlocks(x1, y1 + 15, z1, x1, get_lowest_y_in_region(mc, x1, y1, z1, z2) + 1, z2, block.AIR)


def build_straight_ew(mc, x, y, z):
    start = 3
    wood_id = 17

    # first, flatten all the path, so that it is valid to place roads upon
    for i in range(15):
        flatten(mc, x + i, mc.getHeight(x + i, z), z + 3, z + 12)

    # build the roads on the validated path.

    for i in range(15):
        new_y = mc.getHeight(x + i, start + z)
        mc.setBlock(x + i, new_y, start + z, wood_id)
        mc.setBlock(x + i, new_y + 1, start + z, block.LEAVES)
        mc.setBlock(x + i, new_y, start + z + 1, wood_id, 4)
        mc.setBlocks(x + i, new_y, start + z + 2, x + i, new_y, start + z + 7, block.BRICK_BLOCK)
        mc.setBlock(x + i, new_y, start + z + 8, wood_id, 4)
        mc.setBlock(x + i, new_y + 1, start + z + 9, block.LEAVES)
        mc.setBlock(x + i, new_y, start + z + 9, wood_id)

        # Will create evenly placed glowstone blocks down the center of the path
        if i == 2:
            mc.setBlock(x + 2, new_y, z + 4 + start, block.GLOWSTONE_BLOCK)
        elif i == 7:
            mc.setBlock(x + 7, new_y, z + 4 + start, block.GLOWSTONE_BLOCK)
        elif i == 12:
            mc.setBlock(x + 12, new_y, z + 4 + start, block.GLOWSTONE_BLOCK)


if __name__ == '__main__':
    mc = Minecraft.create()

    build_straight_ew(mc, *mc.player.getPos())

    mc.postToChat('Done!')
