from mcpi import block, minecraft
import numpy as np
import time
start_time = time.time()

mc = minecraft.Minecraft.create()
z_length = 3 #z_length by x_length dimensions (feel free to edit how you please to test different areas, this will later just call upon the village size)
x_length = 15
x, y, z = mc.player.getPos()
acceptable_height = y
height_array = np.zeros(z_length * x_length, dtype=np.int64)
prev_block_height_array = np.zeros(z_length * x_length, dtype=np.int64)
height_array = np.reshape(height_array, (x_length,z_length))
prev_block_height_array = np.reshape(prev_block_height_array, (x_length,z_length))
blocks = mc.getBlocks(x, 50, z, x+x_length-1, acceptable_height + 30, z+z_length-1) #0-256 is standard world height

z_block = 0 #start off with
x_block = 0
y_block = 0
count = 0
for block in blocks: #priority of checking is: z, x, y
    if z_block > z_length - 1: #if the z coordinate of the block is more than the z length provided, the search on this row is done
        z_block = 0 #reset z coordinate back to start
        x_block += 1 #move to next row
    if x_block > x_length - 1: #if the x coordinate of the block is more than the x length provided, the search on this row (and level) is done
        x_block = 0 #reset x coordinate back to start
        y_block += 1 #move up a level
    if block == 0 and prev_block_height_array[x_block, z_block] != 0 and prev_block_height_array[x_block, z_block] != 8 and prev_block_height_array[x_block, z_block] != 9 and prev_block_height_array[x_block, z_block] != 10 and prev_block_height_array[x_block, z_block] != 11: #checks from bottom up for a block until reaching highest block (not including air, water, or lava), priority being: z, x, y
        height_array[x_block,z_block] = y_block + 50 #set the current value in height_array to the y coordinate
    prev_block_height_array[x_block,z_block] = block #set the current value in prev_block to the current block
    z_block += 1 #ensures loop can continue
    count += 1

min_heights = height_array.min(axis=1)
prev_item = 0
for item in min_heights:
    if prev_item == 0:
        mc.setBlocks(x, item, z, x, item + 15, z+2, 0)
        mc.setBlocks(x, item - 1, z, x, item - 1, z+2, 7)
        prev_item = item
    else:
        if item - prev_item > 0:
            item = prev_item + 1
        mc.setBlocks(x, item, z, x, item + 15, z+2, 0)
        mc.setBlocks(x, item - 1, z, x, item - 1, z+2, 7)
        prev_item = item
    x = x + 1

