import mcpi.minecraft as minecraft
import numpy as np
import time


def scan_terrain(mc, x, y, z):
    z_length = 15  
    x_length = 15  
    return _scan(mc, x, y, z, z_length, x_length)

def _scan(mc, x, y, z, z_length, x_length) -> bool:
    acceptable_height = y

    height_array = np.zeros(z_length * x_length, dtype=np.int32)
    prev_block_height_array = np.zeros(z_length * x_length, dtype=np.int32)

    height_array = np.reshape(height_array, (x_length, z_length))
    prev_block_height_array = np.reshape(prev_block_height_array, (x_length, z_length))

    # 0-256 is standard world height
    blocks = mc.getBlocks(x, 50, z, x + x_length - 1, acceptable_height + 15, z + z_length - 1)
    z_block = 0  # start off with
    x_block = 0
    y_block = 0
    count = 0

    # priority of checking is: z, x, y
    for block in blocks:

        # if the z coordinate of the block is more than the z length provided, the search on this row is done
        if z_block > z_length - 1:
            z_block = 0  # reset z coordinate back to start
            x_block += 1  # move to next row

        # if the x coordinate of the block is more than the x length provided,
        # the search on this row (and level) is done

        if x_block > x_length - 1:
            x_block = 0  # reset x coordinate back to start
            y_block += 1  # move up a level

        # checks from bottom up for a block until reaching highest block
        # (not including air, water, lava, grass, wood, or leaves), priority being: z, x, y
        if block == 0 and prev_block_height_array[x_block, z_block] != 0 and prev_block_height_array[
            x_block, z_block] != 8 and prev_block_height_array[x_block, z_block] != 9 and prev_block_height_array[
            x_block, z_block] != 10 and prev_block_height_array[x_block, z_block] != 11:
            # set the current value in height_array to the y coordinate
            height_array[x_block, z_block] = y_block + 50

        # set the current value in prev_block to the current block
        prev_block_height_array[x_block, z_block] = block
        # ensures loop can continue
        z_block += 1
        count += 1

    under_limit = 0
    over_limit = 0
    bench_under = acceptable_height - 2
    bench_over = acceptable_height + 2

    # go through every value to see if its under the limit or not, if it is add 1 to under_limit
    for row in height_array:
        for height in row:
            if height < bench_under:
                under_limit += 1
            elif height > bench_over:
                over_limit += 1

    if under_limit > 1:
        return False
    elif over_limit > 1:
        return False
    else:
        return True

mc = minecraft.Minecraft.create()
x, y, z = mc.player.getTilePos()
print(scan_terrain(mc, x, y, z))

