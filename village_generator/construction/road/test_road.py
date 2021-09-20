from mcpi.minecraft import Minecraft
import mcpi.block as block

def build_straight_ew_replace(mc, x, y, z):
    start = 3
    wood_id = 17

    # build the roads on the validated path.
    for i in range(15):
        mc.setBlock(x + i, mc.getHeight(x + i, start + z), start + z, wood_id)
        mc.setBlock(x + i, mc.getHeight(x + i, start + z) + 1, start + z, block.LEAVES)
        mc.setBlock(x + i,  mc.getHeight(x + i, start + z + 1), start + z + 1, wood_id, 4)
        
        mc.setBlock(x + i,  mc.getHeight(x + i, start + z + 2), start + z + 2, block.BRICK_BLOCK)
        mc.setBlock(x + i,  mc.getHeight(x + i, start + z + 3), start + z + 3, block.BRICK_BLOCK)
        mc.setBlock(x + i,  mc.getHeight(x + i, start + z + 4), start + z + 4, block.BRICK_BLOCK)
        mc.setBlock(x + i,  mc.getHeight(x + i, start + z + 5), start + z + 5, block.BRICK_BLOCK)
        mc.setBlock(x + i,  mc.getHeight(x + i, start + z + 6), start + z + 6, block.BRICK_BLOCK)

        mc.setBlock(x + i,  mc.getHeight(x + i, start + z + 7), start + z + 7, wood_id, 4)
        temp = mc.getHeight(x + i, start + z + 8)
        mc.setBlock(x + i, temp + 1, start + z + 8, block.LEAVES)
        mc.setBlock(x + i,  temp, start + z + 8, wood_id)

        # Will create evenly placed glowstone blocks down the center of the path
        mc.setBlock(x + 2, mc.getHeight(x + 2, z + 4 + start), z + 4 + start, block.GLOWSTONE_BLOCK)
        mc.setBlock(x + 7, mc.getHeight(x + 7, z + 4 + start), z + 4 + start, block.GLOWSTONE_BLOCK)
        mc.setBlock(x + 12, mc.getHeight(x + 12, z + 4 + start), z + 4 + start, block.GLOWSTONE_BLOCK)

# FIXME: replace with getLowestYInLine()
# TODO: need to update this method in the api so that it is more flexible. Currently it only supports the below variation.
def get_lowest_y_in_region_ew(mc, x1, y1, z1, z2):
    lowest = y1

    for k in range(int(z1), int(z2) + 1):
        curr_y = mc.getHeight(x1, k)
        if curr_y < lowest:
            lowest = curr_y

    return lowest

def get_lowest_y_in_region_ns(mc, x1, y1, z1, x2):
    lowest = y1

    for i in range(int(x1), int(x2) + 1):
        curr_y = mc.getHeight(i, z1)
        if curr_y < lowest:
            lowest = curr_y

    return lowest


# TODO: only activate the flattener in certain regions where hills are guaranted (biomes).
#  Will be more efficient because in plains biome, there wont be much to flatten.
# x1 and x2 for the only a different z will be the same.
def flatten_ew(mc, x1, y1, z1, z2):
    # have some sort of heuristic that checks if flattening is necessary, and if not, cancels.
    # change y1 + 15 to the highest y block in this region - when implemented on back-end.
    mc.setBlocks(x1, y1 + 15, z1, x1, get_lowest_y_in_region_ew(mc, x1, y1, z1, z2) + 1, z2, block.AIR)

def flatten_ns(mc, x1, y1, z1, x2):
    mc.setBlocks(x1, y1 + 15, z1, x2, get_lowest_y_in_region_ns(mc, x1, y1, z1, x2) + 1, z1, block.AIR)

def build_straight_ew_terraform(mc, x, y, z):
    start = 3
    wood_id = 17

    # first, flatten all the path, so that it is valid to place roads upon
    for i in range(15):
        flatten_ew(mc, x + i, mc.getHeight(x + i, start + z), start + z, start + z + 9)

    # build the roads on the validated path.

    for i in range(15):
        new_y = mc.getHeight(x + i, start + z)
        mc.setBlock(x + i, new_y, start + z, wood_id)
        mc.setBlock(x + i, new_y + 1, start + z, block.LEAVES)
        mc.setBlock(x + i, new_y, start + z + 1, wood_id, 4)
        mc.setBlocks(x + i, new_y, start + z + 2, x + i, new_y, start + z + 6, block.BRICK_BLOCK)
        mc.setBlock(x + i, new_y, start + z + 7, wood_id, 4)
        mc.setBlock(x + i, new_y + 1, start + z + 8, block.LEAVES)
        mc.setBlock(x + i, new_y, start + z + 8, wood_id)

        # Will create evenly placed glowstone blocks down the center of the path
        if i == 2:
            mc.setBlock(x + 2, new_y, z + 4 + start, block.GLOWSTONE_BLOCK)
        elif i == 7:
            mc.setBlock(x + 7, new_y, z + 4 + start, block.GLOWSTONE_BLOCK)
        elif i == 12:
            mc.setBlock(x + 12, new_y, z + 4 + start, block.GLOWSTONE_BLOCK)



# Path class for the North/South Path
# createPath function to create the North/South path based on matrix position
def build_straight_ns_terraform(mc, x, y, z):
    start = 3
    wood_id = 17

    # first, flatten all the path, so that it is valid to place roads upon
    for k in range(15):
        flatten_ns(mc, start + x, mc.getHeight(start + x, z + k), z + k, start + x + 9)

    # build the roads on the validated path.

    for k in range(15):
        new_y = mc.getHeight(x + start, z + k)
        mc.setBlock(start + x, new_y, z + k, wood_id)
        mc.setBlock(start + x, new_y + 1, z + k, block.LEAVES)
        mc.setBlock(start + x + 1, new_y, z + k, wood_id, 4)
        mc.setBlocks(start + x + 2, new_y, z + k, start + x + 6, new_y, z + k, block.BRICK_BLOCK)
        mc.setBlock(start + x + 7, new_y, z + k, wood_id, 4)
        mc.setBlock(start + x + 8, new_y + 1, z + k, block.LEAVES)
        mc.setBlock(start + x + 8, new_y, z + k, wood_id)

        # Will create evenly placed glowstone blocks down the center of the path
        if k == 2:
            mc.setBlock(x + 4 + start, new_y, z + 2, block.GLOWSTONE_BLOCK)
        elif k == 7:
            mc.setBlock(x + 4 + start, new_y, z + 7, block.GLOWSTONE_BLOCK)
        elif k == 12:
            mc.setBlock(x + 4 + start, new_y, z + 12, block.GLOWSTONE_BLOCK)



def build_straight_ew_terraform_skinny(mc, x, y, z):
    start = 3
    wood_id = 17

    # first, flatten all the path, so that it is valid to place roads upon
    for i in range(15):
        flatten_ew(mc, x + i, mc.getHeight(x + i, start + z), start + z + 3, start + z + 5)

    # build the roads on the validated path.

    for i in range(15):
        new_y = mc.getHeight(x + i, start + z)
        mc.setBlocks(x + i, new_y, start + z + 3, x + i, new_y, start + z + 5, block.BRICK_BLOCK)

        # Will create evenly placed glowstone blocks down the center of the path
        if i == 2:
            mc.setBlock(x + 2, new_y, z + 4 + start, block.GLOWSTONE_BLOCK)
        elif i == 7:
            mc.setBlock(x + 7, new_y, z + 4 + start, block.GLOWSTONE_BLOCK)
        elif i == 12:
            mc.setBlock(x + 12, new_y, z + 4 + start, block.GLOWSTONE_BLOCK)

if __name__ == '__main__':
    mc = Minecraft.create()
    x, y, z = mc.player.getPos()

    # NOTE: Adjust these coordinates to your liking. I  have made it so they all spawn near each other if you want a relative side-by-side comparsion.
    # otherwise, just comment the ones you dont wanna use out, or do whatever you'd like.

    # THE HARD WAY - TERRAFORMS TERRAIN TO ENSURE STRAIGHT ROAD PLACEMENT BEFORE PLACING.
    # THESE ARE THE TRADITIONAL 15 X 15 ROADS.
    build_straight_ew_terraform(mc, x, y, z)
    build_straight_ns_terraform(mc, x - 12, y, z)

    # THIS IS THE NEW IDAE: 3 X 15 ROADS ( WIDTH X LENGTH, where width = 3, and length = 15).
    build_straight_ew_terraform_skinny(mc, x + 12, y, z)

    build_straight_ew_replace(mc, x, y, z + 12)

    mc.postToChat('Done!')
