import mcpi.block as block
import math

CURVE = (17, [17, 4], 45, 45, 45, 45, 45, [17, 4], 17)


# straight
# Path class for the East/West Path
# A function that builds a path corresponding to function name based on matrix position
def build_straight_ew(mc, x, y, z):
    # Start is set to the boundaries for the path to enable the path to be centred within a 15x15 area.
    start = 3
    wood_id = 17
    # Working within 15x15 dimensions to generate road
    # Loops 15 times over to cover a 15 block radius of below blocks (length of path)

    mc.setBlocks(x, y, z + start, x + 15, y, z + start, block.LEAVES)
    mc.setBlocks(x, y - 1, z + start, x + 15, y - 1, z + start, wood_id)
    mc.setBlocks(x, y - 1, z + 1 + start, x + 15, y - 1, z + 1 + start, wood_id, 4)
    mc.setBlocks(x, y - 1, z + 2 + start, x + 15, y - 1, z + 6 + start, block.BRICK_BLOCK)
    mc.setBlocks(x, y - 1, z + 7 + start, x + 15, y - 1, z + 7 + start, wood_id, 4)
    mc.setBlocks(x, y - 1, z + 8 + start, x + 15, y - 1, z + 8 + start, wood_id)
    mc.setBlocks(x, y, z + 8 + start, x + 15, y, z + 8 + start, block.LEAVES)

    # Will create evenly placed glowstone blocks down the center of the path
    mc.setBlock(x + 2, y - 1, z + 4 + start, block.GLOWSTONE_BLOCK)
    mc.setBlock(x + 7, y - 1, z + 4 + start, block.GLOWSTONE_BLOCK)
    mc.setBlock(x + 12, y - 1, z + 4 + start, block.GLOWSTONE_BLOCK)


# Path class for the North/South Path
# createPath function to create the North/South path based on matrix position
def build_straight_ns(mc, x, y, z):
    center = 3
    wood_id = 17

    mc.setBlocks(x + center, y, z, x + center, y, z + 15, block.LEAVES)
    mc.setBlocks(x + center, y - 1, z, x + center, y - 1, z + 15, wood_id)
    mc.setBlocks(x + 1 + center, y - 1, z, x + 1 + center, y - 1, z + 15, wood_id, 4)
    mc.setBlocks(x + 2 + center, y - 1, z, x + 6 + center, y - 1, z + 15, block.BRICK_BLOCK)
    mc.setBlocks(x + 7 + center, y - 1, z, x + 7 + center, y - 1, z + 15, wood_id, 4)
    mc.setBlocks(x + 8 + center, y - 1, z, x + 8 + center, y - 1, z + 15, wood_id)
    mc.setBlocks(x + 8 + center, y, z, x + 8 + center, y, z + 15, block.LEAVES)

    mc.setBlock(x + 4 + center, y - 1, z + 2, block.GLOWSTONE_BLOCK)
    mc.setBlock(x + 4 + center, y - 1, z + 7, block.GLOWSTONE_BLOCK)
    mc.setBlock(x + 4 + center, y - 1, z + 12, block.GLOWSTONE_BLOCK)


# bent
# Path class for curve SE
def build_bent_connecting_se(mc, x, y, z):
    # Radius the curve is built upon
    radius = 11.5
    # List of blocks in path
    # Working within 15x15 dimensions to generate road
    # Angle of path created (SE direction)
    for angle in range(181, 270):
        for i in range(len(CURVE)):
            # Assigned x and z coordinates based on angle position
            new_x = x + (radius - i) * math.cos(angle * math.pi / 180)
            new_z = z + (radius - i) * math.sin(angle * math.pi / 180)
            # Place currently hovered block in list
            mc.setBlock(new_x + 15, y - 1, new_z + 15, CURVE[i])

            if i == 8:
                # Place leaf block at the end (inside)
                mc.setBlock(new_x + 15, y, new_z + 15, block.LEAVES)

        # Assign x and z coordinates based on angle position
        new_x = x + radius * math.cos(angle * math.pi / 180)
        new_z = z + radius * math.sin(angle * math.pi / 180)

        # Place leaf blocks along the outside of the build
        mc.setBlock(new_x + 15, y, new_z + 15, block.LEAVES)

    # Place glowstone blocks in path
    mc.setBlock(x + 12, y - 1, z + 7, block.GLOWSTONE_BLOCK)
    mc.setBlock(x + 7, y - 1, z + 12, block.GLOWSTONE_BLOCK)


def build_bent_connecting_sw(mc, x, y, z):
    radius = 11.5
    # Working within 15x15 dimensions to generate road
    for angle in range(271, 360):
        for i in range(len(CURVE)):
            new_x = x + (radius - i) * math.cos(angle * math.pi / 180)
            new_z = z + (radius - i) * math.sin(angle * math.pi / 180)
            mc.setBlock(new_x, y - 1, new_z + 15, CURVE[i])

            if i == 8:
                mc.setBlock(new_x, y, new_z + 15, block.LEAVES)

        new_x = x + radius * math.cos(angle * math.pi / 180)
        new_z = z + radius * math.sin(angle * math.pi / 180)
        mc.setBlock(new_x, y, new_z + 15, block.LEAVES)

    mc.setBlock(x + 2, y - 1, z + 7, block.GLOWSTONE_BLOCK)
    mc.setBlock(x + 7, y - 1, z + 12, block.GLOWSTONE_BLOCK)


def build_bent_connecting_ne(mc, x, y, z):
    radius = 11.5

    for angle in range(91, 180):
        for i in range(len(CURVE)):
            new_x = x + (radius - i) * math.cos(angle * math.pi / 180)
            new_z = z + (radius - i) * math.sin(angle * math.pi / 180)
            mc.setBlock(new_x + 15, y - 1, new_z, CURVE[i])

            if i == 8:
                mc.setBlock(new_x + 15, y, new_z, block.LEAVES)

        new_x = x + radius * math.cos(angle * math.pi / 180)
        new_z = z + radius * math.sin(angle * math.pi / 180)
        mc.setBlock(new_x + 15, y, new_z, block.LEAVES)

    mc.setBlock(x + 7, y - 1, z + 2, block.GLOWSTONE_BLOCK)
    mc.setBlock(x + 12, y - 1, z + 7, block.GLOWSTONE_BLOCK)


def build_bent_connecting_nw(mc, x, y, z):
    radius = 11.5

    for angle in range(90):
        for i in range(len(CURVE)):
            new_x = x + (radius - i) * math.cos(angle * math.pi / 180)
            new_z = z + (radius - i) * math.sin(angle * math.pi / 180)
            mc.setBlock(new_x, y - 1, new_z, CURVE[i])

            if i == 8:
                mc.setBlock(new_x, y, new_z, block.LEAVES)

        new_x = x + radius * math.cos(angle * math.pi / 180)
        new_z = z + radius * math.sin(angle * math.pi / 180)
        mc.setBlock(new_x, y, new_z, block.LEAVES)

    mc.setBlock(x + 7, y - 1, z + 2, block.GLOWSTONE_BLOCK)
    mc.setBlock(x + 2, y - 1, z + 7, block.GLOWSTONE_BLOCK)


# intersection
# Path class for the intersection path
# A function that builds a path corresponding to function name based on matrix position
def build_crossintersection(mc, x, y, z):
    # This is to set the boundaries for the path to enable the path to be centred within a 15x15 area
    center = 3
    wood_id = 17
    # Working within 15x15 dimensions to generate road
    # Loops 15 times over to cover a 15 block radius of below blocks (length of path)
    for i in range(15):
        mc.setBlocks(x, y, z + center, x + i, y, z + center, block.LEAVES)
        mc.setBlocks(x, y - 1, z + center, x + i, y - 1, z + center, wood_id)
        mc.setBlocks(x, y - 1, z + 1 + center, x + i, y - 1, z + 1 + center, wood_id, 4)
        mc.setBlocks(x, y - 1, z + 2 + center, x + i, y - 1, z + 6 + center, block.BRICK_BLOCK)
        mc.setBlocks(x, y, z + 8 + center, x + i, y, z + 8 + center, block.LEAVES)
        mc.setBlocks(x, y - 1, z + 8 + center, x + i, y - 1, z + 8 + center, wood_id)
        mc.setBlocks(x, y - 1, z + 7 + center, x + i, y - 1, z + 7 + center, wood_id, 4)

    # Loops 15 times over to cover a 15 block radius of below blocks (length of path)
    for i in range(15):
        mc.setBlocks(x + center, y, z, x + center, y, z + i, block.LEAVES)
        mc.setBlocks(x + center, y - 1, z, x + center, y - 1, z + i, wood_id)
        mc.setBlocks(x + 1 + center, y - 1, z, x + 1 + center, y - 1, z + i, wood_id, 4)
        mc.setBlocks(x + 2 + center, y - 1, z, x + 6 + center, y - 1, z + i, block.BRICK_BLOCK)
        mc.setBlocks(x + 8 + center, y, z, x + 8 + center, y, z + i, block.LEAVES)
        mc.setBlocks(x + 8 + center, y - 1, z, x + 8 + center, y - 1, z + i, wood_id)
        mc.setBlocks(x + 7 + center, y - 1, z, x + 7 + center, y - 1, z + i, wood_id, 4)

    # Removes the leaves that are in the way from intersecting paths
    mc.setBlocks(x + center, y, z + 4, x + center, y, z + 10, block.AIR)
    mc.setBlocks(x + center + 8, y, z + 4, x + center + 8, y, z + 10, block.AIR)
    mc.setBlocks(x + 10, y, z + 4, x + center + 1, y, z + center, block.AIR)
    mc.setBlocks(x + 10, y, z + 4, x + center + 1, y, z + center + 8, block.AIR)

    # Replace the whole EW path with bricks
    mc.setBlocks(x, y - 1, z + center + 1, x + 14, y - 1, z + center + 7, block.BRICK_BLOCK)
    # Lay out block appropriately
    mc.setBlocks(x, y - 1, z + center + 1, x + 4, y - 1, z + center + 1, wood_id, 4)
    mc.setBlocks(x + 10, y - 1, z + center + 1, x + 14, y - 1, z + center + 1, wood_id, 4)
    mc.setBlocks(x, y - 1, z + center + 7, x + 4, y - 1, z + center + 7, wood_id, 4)
    mc.setBlocks(x + 10, y - 1, z + center + 7, x + 14, y - 1, z + center + 7, wood_id, 4)

    # Will create evenly placed glowstone blocks down the center of the path
    mc.setBlock(x + 4 + center, y - 1, z + 2, block.GLOWSTONE_BLOCK)
    mc.setBlock(x + 4 + center, y - 1, z + 12, block.GLOWSTONE_BLOCK)
    mc.setBlock(x + 2, y - 1, z + 4 + center, block.GLOWSTONE_BLOCK)
    mc.setBlock(x + 7, y - 1, z + 4 + center, block.GLOWSTONE_BLOCK)
    mc.setBlock(x + 12, y - 1, z + 4 + center, block.GLOWSTONE_BLOCK)


# A function that builds a path corresponding to function name based on current player position
def build_intersection_e_ns(mc, x, y, z):
    center = 3
    wood_id = 17
    # Working within 15x15 dimensions to generate road
    for i in range(15):
        mc.setBlocks(x, y, z + center, x + i, y, z + center, block.LEAVES)
        mc.setBlocks(x, y - 1, z + center, x + i, y - 1, z + center, wood_id)
        mc.setBlocks(x, y - 1, z + 1 + center, x + i, y - 1, z + 1 + center, wood_id, 4)
        mc.setBlocks(x, y - 1, z + 2 + center, x + i, y - 1, z + 6 + center, block.BRICK_BLOCK)
        mc.setBlocks(x, y, z + 8 + center, x + i, y, z + 8 + center, block.LEAVES)
        mc.setBlocks(x, y - 1, z + 8 + center, x + i, y - 1, z + 8 + center, wood_id)
        mc.setBlocks(x, y - 1, z + 7 + center, x + i, y - 1, z + 7 + center, wood_id, 4)

    for i in range(15):
        mc.setBlocks(x + center, y, z, x + center, y, z + i, block.LEAVES)
        mc.setBlocks(x + center, y - 1, z, x + center, y - 1, z + i, wood_id)
        mc.setBlocks(x + 1 + center, y - 1, z, x + 1 + center, y - 1, z + i, wood_id, 4)
        mc.setBlocks(x + 2 + center, y - 1, z, x + 6 + center, y - 1, z + i, block.BRICK_BLOCK)
        mc.setBlocks(x + 8 + center, y, z, x + 8 + center, y, z + i, block.LEAVES)
        mc.setBlocks(x + 8 + center, y - 1, z, x + 8 + center, y - 1, z + i, wood_id)
        mc.setBlocks(x + 7 + center, y - 1, z, x + 7 + center, y - 1, z + i, wood_id, 4)

    mc.setBlock(x + 4 + center, y - 1, z + 2, block.GLOWSTONE_BLOCK)
    mc.setBlock(x + 4 + center, y - 1, z + 12, block.GLOWSTONE_BLOCK)

    # Removes the leaves that are in the way from intersecting paths
    mc.setBlocks(x + center + 8, y, z + 4, x + center + 8, y, z + 10, block.AIR)
    mc.setBlocks(x + 10, y, z + 4, x + center + 1, y, z + center, block.AIR)
    mc.setBlocks(x + 10, y, z + 4, x + center + 1, y, z + center + 8, block.AIR)

    # Replace the whole EW path with bricks
    mc.setBlocks(x + 5, y - 1, z + center + 1, x + 14, y - 1, z + center + 7, block.BRICK_BLOCK)
    # Lay out wood appropriately
    mc.setBlocks(x + 10, y - 1, z + center + 1, x + 14, y - 1, z + center + 1, wood_id, 4)
    mc.setBlocks(x + 10, y - 1, z + center + 7, x + 14, y - 1, z + center + 7, wood_id, 4)

    # Will create evenly placed glowstone blocks down the center of the path
    mc.setBlock(x + 7, y - 1, z + 4 + center, block.GLOWSTONE_BLOCK)
    mc.setBlock(x + 12, y - 1, z + 4 + center, block.GLOWSTONE_BLOCK)

    # Remove a part of the intersection that is sticking out in order to make a T, and replace the hole with the block in the biome
    mc.setBlocks(x, y, z, x + 2, y, z + 14, block.AIR)
    block_id = mc.getBlock(x, y - 1, z + 15)
    mc.setBlocks(x, y - 1, z, x + 2, y - 1, z + 14, block_id)


# A function that builds a path corresponding to function name based on current player position
def build_intersection_s_ew(mc, x, y, z):
    center = 3
    wood_id = 17
    # Working within 15x15 dimensions to generate road
    for i in range(15):
        mc.setBlocks(x, y, z + center, x + i, y, z + center, block.LEAVES)
        mc.setBlocks(x, y - 1, z + center, x + i, y - 1, z + center, wood_id)
        mc.setBlocks(x, y - 1, z + 1 + center, x + i, y - 1, z + 1 + center, wood_id, 4)
        mc.setBlocks(x, y - 1, z + 2 + center, x + i, y - 1, z + 6 + center, block.BRICK_BLOCK)
        mc.setBlocks(x, y, z + 8 + center, x + i, y, z + 8 + center, block.LEAVES)
        mc.setBlocks(x, y - 1, z + 8 + center, x + i, y - 1, z + 8 + center, wood_id)
        mc.setBlocks(x, y - 1, z + 7 + center, x + i, y - 1, z + 7 + center, wood_id, 4)

    for i in range(15):
        mc.setBlocks(x + center, y, z, x + center, y, z + i, block.LEAVES)
        mc.setBlocks(x + center, y - 1, z, x + center, y - 1, z + i, wood_id)
        mc.setBlocks(x + 1 + center, y - 1, z, x + 1 + center, y - 1, z + i, wood_id, 4)
        mc.setBlocks(x + 2 + center, y - 1, z, x + 6 + center, y - 1, z + i, block.BRICK_BLOCK)
        mc.setBlocks(x + 8 + center, y, z, x + 8 + center, y, z + i, block.LEAVES)
        mc.setBlocks(x + 8 + center, y - 1, z, x + 8 + center, y - 1, z + i, wood_id)
        mc.setBlocks(x + 7 + center, y - 1, z, x + 7 + center, y - 1, z + i, wood_id, 4)

    # Will create evenly placed glowstone blocks down the center of the path
    mc.setBlock(x + 4 + center, y - 1, z + 12, block.GLOWSTONE_BLOCK)
    # Removes the leaves that are in the way from intersecting paths
    mc.setBlocks(x + center, y, z + 4, x + center, y, z + 10, block.AIR)
    mc.setBlocks(x + center + 8, y, z + 4, x + center + 8, y, z + 10, block.AIR)
    mc.setBlocks(x + 10, y, z + 4, x + center + 1, y, z + center + 8, block.AIR)

    # Replace the whole EW path with bricks
    mc.setBlocks(x, y - 1, z + center + 1, x + 14, y - 1, z + center + 7, block.BRICK_BLOCK)
    mc.setBlocks(x, y - 1, z + center + 1, x + 4, y - 1, z + center + 1, wood_id, 4)  # Lay out wood appropriately
    mc.setBlocks(x + 10, y - 1, z + center + 1, x + 14, y - 1, z + center + 1, wood_id, 4)
    mc.setBlocks(x, y - 1, z + center + 7, x + 4, y - 1, z + center + 7, wood_id, 4)
    mc.setBlocks(x + 10, y - 1, z + center + 7, x + 14, y - 1, z + center + 7, wood_id, 4)

    # Will create evenly placed glowstone blocks down the center of the path
    mc.setBlock(x + 2, y - 1, z + 4 + center, block.GLOWSTONE_BLOCK)
    mc.setBlock(x + 7, y - 1, z + 4 + center, block.GLOWSTONE_BLOCK)
    mc.setBlock(x + 12, y - 1, z + 4 + center, block.GLOWSTONE_BLOCK)

    # Remove a part of the intersection that is sticking out in order to make a T, and replace the hole with the block in the biome
    block_id = mc.getBlock(x, y - 1, z)
    mc.setBlocks(x, y - 1, z, x + 14, y, z + 2, block.AIR)
    mc.setBlocks(x, y - 1, z + 3, x + 14, y - 1, z + 3, wood_id)
    mc.setBlocks(x, y - 1, z + 4, x + 14, y - 1, z + 4, wood_id, 4)
    mc.setBlocks(x, y - 1, z, x + 15, y - 1, z + 2, block_id)


# A function that builds a path corresponding to function name based on current player position
def build_intersection_w_ns(mc, x, y, z):
    center = 3
    wood_id = 17

    for i in range(11):
        mc.setBlocks(x, y, z + center, x + i, y, z + center, block.LEAVES)
        mc.setBlocks(x, y - 1, z + center, x + i, y - 1, z + center, wood_id)
        mc.setBlocks(x, y - 1, z + 1 + center, x + i, y - 1, z + 1 + center, wood_id, 4)
        mc.setBlocks(x, y - 1, z + 2 + center, x + i, y - 1, z + 6 + center, block.BRICK_BLOCK)
        mc.setBlocks(x, y, z + 8 + center, x + i, y, z + 8 + center, block.LEAVES)
        mc.setBlocks(x, y - 1, z + 8 + center, x + i, y - 1, z + 8 + center, wood_id)
        mc.setBlocks(x, y - 1, z + 7 + center, x + i, y - 1, z + 7 + center, wood_id, 4)

    for i in range(15):
        mc.setBlocks(x + center, y, z, x + center, y, z + i, block.LEAVES)
        mc.setBlocks(x + center, y - 1, z, x + center, y - 1, z + i, wood_id)
        mc.setBlocks(x + 1 + center, y - 1, z, x + 1 + center, y - 1, z + i, wood_id, 4)
        mc.setBlocks(x + 2 + center, y - 1, z, x + 6 + center, y - 1, z + i, block.BRICK_BLOCK)
        mc.setBlocks(x + 8 + center, y, z, x + 8 + center, y, z + i, block.LEAVES)
        mc.setBlocks(x + 8 + center, y - 1, z, x + 8 + center, y - 1, z + i, wood_id)
        mc.setBlocks(x + 7 + center, y - 1, z, x + 7 + center, y - 1, z + i, wood_id, 4)

    # Will create evenly placed glowstone blocks down the center of the path
    mc.setBlock(x + 4 + center, y - 1, z + 2, block.GLOWSTONE_BLOCK)
    mc.setBlock(x + 4 + center, y - 1, z + 12, block.GLOWSTONE_BLOCK)

    # Removes the leaves that are in the way from intersecting paths
    mc.setBlocks(x + center, y, z + 4, x + center, y, z + 10, block.AIR)
    mc.setBlocks(x + 10, y, z + 4, x + center + 1, y, z + center, block.AIR)
    mc.setBlocks(x + 10, y, z + 4, x + center + 1, y, z + center + 8, block.AIR)

    # Replace the whole EW path with bricks
    mc.setBlocks(x, y - 1, z + center + 1, x + 9, y - 1, z + center + 7, block.BRICK_BLOCK)
    mc.setBlocks(x, y - 1, z + center + 1, x + 4, y - 1, z + center + 1, wood_id, 4)  # Lay out wood appropriately
    mc.setBlocks(x, y - 1, z + center + 7, x + 4, y - 1, z + center + 7, wood_id, 4)

    # Will create evenly placed glowstone blocks down the center of the path
    mc.setBlock(x + 2, y - 1, z + 4 + center, block.GLOWSTONE_BLOCK)
    mc.setBlock(x + 7, y - 1, z + 4 + center, block.GLOWSTONE_BLOCK)


# A function that builds a path corresponding to function name based on current player position
def build_intersection_n_ew(mc, x, y, z):
    center = 3
    wood_id = 17

    for i in range(15):
        mc.setBlocks(x, y, z + center, x + i, y, z + center, block.LEAVES)
        mc.setBlocks(x, y - 1, z + center, x + i, y - 1, z + center, wood_id)
        mc.setBlocks(x, y - 1, z + 1 + center, x + i, y - 1, z + 1 + center, wood_id, 4)
        mc.setBlocks(x, y - 1, z + 2 + center, x + i, y - 1, z + 6 + center, block.BRICK_BLOCK)
        mc.setBlocks(x, y, z + 8 + center, x + i, y, z + 8 + center, block.LEAVES)
        mc.setBlocks(x, y - 1, z + 8 + center, x + i, y - 1, z + 8 + center, wood_id)
        mc.setBlocks(x, y - 1, z + 7 + center, x + i, y - 1, z + 7 + center, wood_id, 4)

    for i in range(9):
        mc.setBlocks(x + center, y, z, x + center, y, z + i, block.LEAVES)
        mc.setBlocks(x + center, y - 1, z, x + center, y - 1, z + i, wood_id)
        mc.setBlocks(x + 1 + center, y - 1, z, x + 1 + center, y - 1, z + i, wood_id, 4)
        mc.setBlocks(x + 2 + center, y - 1, z, x + 6 + center, y - 1, z + i, block.BRICK_BLOCK)
        mc.setBlocks(x + 8 + center, y, z, x + 8 + center, y, z + i, block.LEAVES)
        mc.setBlocks(x + 8 + center, y - 1, z, x + 8 + center, y - 1, z + i, wood_id)
        mc.setBlocks(x + 7 + center, y - 1, z, x + 7 + center, y - 1, z + i, wood_id, 4)

    mc.setBlock(x + 4 + center, y - 1, z + 2, block.GLOWSTONE_BLOCK)

    # Removes the leaves that are in the way from intersecting paths
    mc.setBlocks(x + center, y, z + 4, x + center, y, z + 10, block.AIR)
    mc.setBlocks(x + center + 8, y, z + 4, x + center + 8, y, z + 10, block.AIR)
    mc.setBlocks(x + 10, y, z + 4, x + center + 1, y, z + center, block.AIR)

    # Replace the whole EW path with bricks
    mc.setBlocks(x, y - 1, z + center + 1, x + 14, y - 1, z + center + 7, block.BRICK_BLOCK)
    mc.setBlocks(x, y - 1, z + center + 1, x + 4, y - 1, z + center + 1, wood_id, 4)  # Lay out wood appropriately
    mc.setBlocks(x + 10, y - 1, z + center + 1, x + 14, y - 1, z + center + 1, wood_id, 4)
    mc.setBlocks(x, y - 1, z + center + 7, x + 4, y - 1, z + center + 7, wood_id, 4)
    mc.setBlocks(x + 10, y - 1, z + center + 7, x + 14, y - 1, z + center + 7, wood_id, 4)

    # Will create evenly placed glowstone blocks down the center of the path
    mc.setBlock(x + 2, y - 1, z + 4 + center, block.GLOWSTONE_BLOCK)
    mc.setBlock(x + 7, y - 1, z + 4 + center, block.GLOWSTONE_BLOCK)
    mc.setBlock(x + 12, y - 1, z + 4 + center, block.GLOWSTONE_BLOCK)

    mc.setBlocks(x, y - 1, z + 10, x + 14, y - 1, z + 10, wood_id,
                 4)  # Add wood to previous intersection path that has been cut off to make a T
