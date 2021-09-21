from mcpi import block, minecraft
import numpy as np
import math
mc = minecraft.Minecraft.create()

def scanner(x, y, z):
    z_length = 180 #z_length by x_length dimensions (feel free to edit how you please to test different areas, this will later just call upon the village size)
    x_length = 15
    mc.setBlocks(x, y, z, x, y, z+3, 0)
    acceptable_height = y
    height_array = np.zeros(z_length * x_length, dtype=np.int64)
    prev_block_height_array = np.zeros(z_length * x_length, dtype=np.int64)
    height_array = np.reshape(height_array, (x_length,z_length))
    prev_block_height_array = np.reshape(prev_block_height_array, (x_length,z_length))
    blocks = mc.getBlocks(x, 60, z, x+x_length-1, acceptable_height + 50, z+z_length-1) #0-256 is standard world height

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
        if block == 0 and prev_block_height_array[x_block, z_block] != 0 and prev_block_height_array[x_block, z_block] != 8 and prev_block_height_array[x_block, z_block] != 9 and prev_block_height_array[x_block, z_block] != 10 and prev_block_height_array[x_block, z_block] != 11 and prev_block_height_array[x_block, z_block] != 18 and prev_block_height_array[x_block, z_block] != 161 and prev_block_height_array[x_block, z_block] != 162 and prev_block_height_array[x_block, z_block] != 1985 and prev_block_height_array[x_block, z_block] != 99 and prev_block_height_array[x_block, z_block] != 100 and prev_block_height_array[x_block, z_block] != 398 and prev_block_height_array[x_block, z_block] != 38 and prev_block_height_array[x_block, z_block] != 39 and prev_block_height_array[x_block, z_block] != 40 and prev_block_height_array[x_block, z_block] != 1985: #checks from bottom up for a block until reaching highest block (not including air, water, or lava), priority being: z, x, y
            height_array[x_block,z_block] = y_block + 60 #set the current value in height_array to the y coordinate
        prev_block_height_array[x_block,z_block] = block #set the current value in prev_block to the current block
        z_block += 1 #ensures loop can continue
        count += 1
    min_heights = height_array.min(axis=1)
    return height_array

def path_ew(min_heights, x, y, z):
    center = 5
    prev_item = 0
    for item in min_heights:
        if item == 0:
            item = prev_item
        if prev_item == 0:
            mc.setBlocks(x, item, z + center, x, item + 50, z+4+center, 0)
            mc.setBlocks(x, item - 1, z + center, x, item - 1, z+4+center, 98)
            prev_item = item
        elif prev_item <= item:
            if item - prev_item > 0:
                item = prev_item + 1
            mc.setBlocks(x, item, z + center, x, item + 50, z+4+center, 0)
            mc.setBlocks(x, item - 1, z + center, x, item - 1, z+4+center, 98)
            prev_item = item
        else:
            temp = item
            item = prev_item - 1
            mc.setBlocks(x, temp, z + center, x, item + 50, z+4+center, 0)
            mc.setBlocks(x, temp, z + center, x, item, z+4+center, 98)
            prev_item = item
        x = x + 1

def path_ns(min_heights, x, y, z):
    center = 5
    prev_item = 0
    for item in min_heights:
        if item == 0:
            item = prev_item
        if prev_item == 0:
            mc.setBlocks(x + center, item, z, x+4+center, item + 50, z, 0)
            mc.setBlocks(x + center, item - 1, z, x+4+center, item - 1, z, 98)
            prev_item = item
        elif prev_item <= item:
            if item - prev_item > 0:
                item = prev_item + 1
            mc.setBlocks(x + center, item, z, x+4+center, item + 50, z, 0)
            mc.setBlocks(x + center, item - 1, z, x+4+center, item - 1, z, 98)
            prev_item = item
        else:
            temp = item
            item = prev_item - 1
            mc.setBlocks(x + center, temp, z, x+4+center, item + 50, z, 0)
            mc.setBlocks(x + center, temp, z, x+4+center, item, z, 98)
            prev_item = item
        z = z + 1

def path_se(mc, x, y, z):
    mc.setBlocks(x, y, z, x+14, y + 30, z+14, 0)
    radius = 9.5
    for angle in range(181, 270):
        for i in range(5):
            new_x = x + (radius - i) * math.cos(angle * math.pi / 180)
            new_z = z + (radius - i) * math.sin(angle * math.pi / 180)
            mc.setBlock(new_x + 14, y - 1, new_z + 14, 98)
        new_x = x + radius * math.cos(angle * math.pi / 180)
        new_z = z + radius * math.sin(angle * math.pi / 180)


x, y, z = mc.player.getPos()
heights = scanner(x, y, z)
#mc.setBlocks(x, y-1, z, x+14, y-1, z+14, 1)
min_heights_ew = heights.min(axis=1)
min_heights_ns = heights.min(axis=0)
#path_ew(min_heights_ew, x, y, z)
path_ns(min_heights_ns, x, y, z)
#path_se(mc, x, y, z)




