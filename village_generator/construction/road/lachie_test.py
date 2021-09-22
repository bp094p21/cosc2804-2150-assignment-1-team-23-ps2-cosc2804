from mcpi import block, minecraft
import numpy as np
import math
mc = minecraft.Minecraft.create()

def scanner(x, y, z):
    z_length = 15 #z_length by x_length dimensions (feel free to edit how you please to test different areas, this will later just call upon the village size)
    x_length = 15
    #mc.setBlocks(x, y - 1, z, x, y - 1, z+3, 0)
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
        if block == 0 and prev_block_height_array[x_block, z_block] != 0 and prev_block_height_array[x_block, z_block] != 18: #and prev_block_height_array[x_block, z_block] != 161 and prev_block_height_array[x_block, z_block] != 162 and prev_block_height_array[x_block, z_block] != 32 and prev_block_height_array[x_block, z_block] != 99 and prev_block_height_array[x_block, z_block] != 100 and prev_block_height_array[x_block, z_block] != 37 and prev_block_height_array[x_block, z_block] != 38 and prev_block_height_array[x_block, z_block] != 39 and prev_block_height_array[x_block, z_block] != 40 and prev_block_height_array[x_block, z_block] != 175: #checks from bottom up for a block until reaching highest block (not including air, water, or lava), priority being: z, x, y
            height_array[x_block,z_block] = y_block + 60 #set the current value in height_array to the y coordinate
        prev_block_height_array[x_block,z_block] = block #set the current value in prev_block to the current block
        z_block += 1 #ensures loop can continue
        count += 1
    return height_array

def path_ew(min_heights, x, y, z):
    center = 5
    prev_item = 0
    new_heights = []
    for item in min_heights:
        if item == 0:
            item = prev_item
        if prev_item == 0:
            mc.setBlocks(x, item, z + center, x, item + 50, z+4+center, 0)
            mc.setBlocks(x, item - 1, z + center, x, item - 1, z+4+center, 98)
            prev_item = item
            new_heights.append(item)
        elif prev_item <= item:
            if item - prev_item > 0:
                item = prev_item + 1
            mc.setBlocks(x, item, z + center, x, item + 50, z+4+center, 0)
            mc.setBlocks(x, item - 1, z + center, x, item - 1, z+4+center, 98)
            prev_item = item
            new_heights.append(item)
        else:
            temp = item
            item = prev_item - 1
            mc.setBlocks(x, temp, z + center, x, item + 50, z+4+center, 0)
            mc.setBlocks(x, temp, z + center, x, item, z+4+center, 98)
            prev_item = item
            new_heights.append(item)
        x = x + 1
    return new_heights

def path_ns(min_heights, x, y, z):
    center = 5
    prev_item = 0
    new_heights = []
    for item in min_heights:
        if item == 0:
            item = prev_item
            new_heights.append(item)
        if prev_item == 0:
            mc.setBlocks(x + center, item, z, x+4+center, item + 50, z, 0)
            mc.setBlocks(x + center, item - 1, z, x+4+center, item - 1, z, 98)
            prev_item = item
            new_heights.append(item)
        elif prev_item <= item:
            if item - prev_item > 0:
                item = prev_item + 1
            mc.setBlocks(x + center, item, z, x+4+center, item + 50, z, 0)
            mc.setBlocks(x + center, item - 1, z, x+4+center, item - 1, z, 98)
            prev_item = item
            new_heights.append(item)
        else:
            temp = item
            item = prev_item - 1
            mc.setBlocks(x + center, temp, z, x+4+center, item + 50, z, 0)
            mc.setBlocks(x + center, temp, z, x+4+center, item, z, 98)
            prev_item = item
            new_heights.append(item)
        z = z + 1
    return(new_heights)

#def path_se(mc, x, y, z): #test
    #mc.setBlocks(x, y, z, x+14, y + 30, z+14, 0)
    #radius = 9.5
    #for angle in range(181, 270):
        #for i in range(5):
            #new_x = x + (radius - i) * math.cos(angle * math.pi / 180)
            #new_z = z + (radius - i) * math.sin(angle * math.pi / 180)
            #mc.setBlock(new_x + 14, y - 1, new_z + 14, 98)
        #new_x = x + radius * math.cos(angle * math.pi / 180)
        #new_z = z + radius * math.sin(angle * math.pi / 180)

def call_for_ns(mc, x, y, z):
    center = 5
    heights = scanner(x, y, z)
    min_heights_ns = heights.min(axis=0)
    new_heights = path_ew(min_heights_ns, x, y, z)
    final_y_in_plot = new_heights[-1]
    #print(final_y_in_plot)
    mc.setBlocks(x + center, final_y_in_plot, z + 15, x + 4 + center, final_y_in_plot + 30, z + 16, 0)
    mc.setBlocks(x + center, final_y_in_plot - 1, z + 15, x + 4 + center, final_y_in_plot - 30, z + 16, 98)
    return final_y_in_plot

def call_for_ew(mc, x, y, z):
    center = 5
    heights = scanner(x, y, z)
    min_heights_ew = heights.min(axis=1)
    new_heights = path_ew(min_heights_ew, x, y, z)
    final_y_in_plot = new_heights[-1]
    #print(final_y_in_plot)
    mc.setBlocks(x + 15, final_y_in_plot, z + center, x + 16, final_y_in_plot + 30, z + 4 + center, 0)
    mc.setBlocks(x + 15, final_y_in_plot - 1, z + center, x + 16, final_y_in_plot - 30, z + 4 + center, 98)
    return final_y_in_plot



