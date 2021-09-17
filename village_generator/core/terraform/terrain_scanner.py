from mcpi import minecraft
import numpy as np
import time


class TerrainScanner:
    def __init__(self):
        self.start_time = time.time()
        self.mc = minecraft.Minecraft.create()

    def scan_terrain_small(self):
        z_length = 60  # 15 * 4
        x_length = 90  # 15 * 6
        under_limit_num = 1080  # At most 20% unsuitable terrain allowed
        self.true_scan_terrain(z_length, x_length, under_limit_num)

    def scan_terrain_medium(self):
        z_length = 60  # 15 * 4
        x_length = 120  # 15 * 8
        under_limit_num = 1440  # At most 20% unsuitable terrain allowed
        self.true_scan_terrain(z_length, x_length, under_limit_num)

    def scan_terrain_large(self):
        z_length = 60  # 15 *4
        x_length = 150  # 15 * 10
        under_limit_num = 1800  # At most 20% unsuitable terrain allowed
        self.true_scan_terrain(z_length, x_length, under_limit_num)

    def true_scan_terrain(self, z_length, x_length, under_limit_num):
        x, y, z = self.mc.player.getPos()
        acceptable_height = y
        height_array = np.zeros(z_length * x_length, dtype=np.int64)
        prev_block_height_array = np.zeros(z_length * x_length, dtype=np.int64)
        height_array = np.reshape(height_array, (x_length, z_length))
        prev_block_height_array = np.reshape(prev_block_height_array, (x_length, z_length))
        # 0-256 is standard world height
        blocks = self.mc.getBlocks(x, 50, z, x + x_length - 1, acceptable_height + 15, z + z_length - 1)

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
                x_block, z_block] != 10 and prev_block_height_array[x_block, z_block] != 11 and prev_block_height_array[
                x_block, z_block] != 31 and prev_block_height_array[x_block, z_block] != 7 and prev_block_height_array[
                x_block, z_block] != 8:
                # set the current value in height_array to the y coordinate
                height_array[x_block, z_block] = y_block + 50

            # set the current value in prev_block to the current block
            prev_block_height_array[x_block, z_block] = block
            # ensures loop can continue
            z_block += 1
            count += 1

        under_limit = 0
        limit = acceptable_height - 5

        # go through every value to see if its under the limit or not, if it is add 1 to under_limit
        for row in height_array:
            for height in row:
                if height < limit:
                    under_limit += 1

        if under_limit <= under_limit_num:
            # print(height_array) #Remove comment if you want, just displays all blocks scanned so not needed
            print(f'It took {time.time() - self.start_time} seconds to scan {count} blocks.')
            print(f'The limit is y={int(limit)} and a maximum of {under_limit_num} blocks can be under it. '
                  f'There were {under_limit} blocks under the limit.')

            return True
        else:
            print("This terrain is not suitable for village generation. Please find another area and try again.")
            print(f'The limit is y={int(limit)} and a maximum of {under_limit_num} blocks can be under it. '
                  f'There were {under_limit} blocks under the limit.')

            self.mc.postToChat("This terrain is not suitable for village generation. "
                               "Please find another area and try again.")

            return False
