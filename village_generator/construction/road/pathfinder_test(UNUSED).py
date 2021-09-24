from mcpi import block, minecraft
import numpy as np
import time
import copy

def scanner(x_length, z_length, x, y, z):
    mc.setBlocks(x, y, z, x, y+50, z, 0)
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
        if block == 0 and prev_block_height_array[x_block, z_block] != 0 and prev_block_height_array[x_block, z_block] != 31 and prev_block_height_array[x_block, z_block] != 18 and prev_block_height_array[x_block, z_block] != 161 and prev_block_height_array[x_block, z_block] != 162 and prev_block_height_array[x_block, z_block] != 32 and prev_block_height_array[x_block, z_block] != 99 and prev_block_height_array[x_block, z_block] != 100 and prev_block_height_array[x_block, z_block] != 37 and prev_block_height_array[x_block, z_block] != 38 and prev_block_height_array[x_block, z_block] != 39 and prev_block_height_array[x_block, z_block] != 40 and prev_block_height_array[x_block, z_block] != 175: #checks from bottom up for a block until reaching highest block (not including air, water, or lava), priority being: z, x, y
            height_array[x_block,z_block] = y_block + 60 #set the current value in height_array to the y coordinate
        prev_block_height_array[x_block,z_block] = block #set the current value in prev_block to the current block
        z_block += 1 #ensures loop can continue
        count += 1
    return height_array
    
from warnings import warn
import heapq

class Node:
    """
    A node class for A* Pathfinding
    """

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position
    
    def __repr__(self):
      return f"{self.position} - g: {self.g} h: {self.h} f: {self.f}"

    # defining less than for purposes of heap queue
    def __lt__(self, other):
      return self.f < other.f
    
    # defining greater than for purposes of heap queue
    def __gt__(self, other):
      return self.f > other.f

def return_path(current_node):
    path = []
    current = current_node
    while current is not None:
        path.append(current.position)
        current = current.parent
    return path[::-1]  # Return reversed path


def astar(maze, start, end, allow_diagonal_movement = False):
    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Heapify the open_list and Add the start node
    heapq.heapify(open_list) 
    heapq.heappush(open_list, start_node)

    # Adding a stop condition
    outer_iterations = 0
    max_iterations = (len(maze[0]) * len(maze) // 2)

    # what squares do we search
    adjacent_squares = ((0, -1), (0, 1), (-1, 0), (1, 0))
    #if allow_diagonal_movement:
        #adjacent_squares = ((0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1),)

    # Loop until you find the end
    while len(open_list) > 0:
        outer_iterations += 1

        if outer_iterations > max_iterations:
          # if we hit this point return the path such as it is
          # it will not contain the destination
          warn("giving up on pathfinding too many iterations")
          return return_path(current_node)       
        
        # Get the current node
        current_node = heapq.heappop(open_list)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            return return_path(current_node)

        # Generate children
        children = []
        
        for new_position in adjacent_squares: # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:
            # Child is on the closed list
            if len([closed_child for closed_child in closed_list if closed_child == child]) > 0:
                continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            if len([open_node for open_node in open_list if child.position == open_node.position and child.g > open_node.g]) > 0:
                continue

            # Add the child to the open list
            heapq.heappush(open_list, child)

    warn("Couldn't get a path to destination")
    return None


def main(maze):
    start = (0, 0)
    end = (9, 0)

    path = astar(maze, start, end)
    return path

if __name__ == '__main__':
    mc = minecraft.Minecraft.create()
    x, y, z = mc.player.getTilePos()
    #mc.setBlocks(x, y-1, z, x+29, y-1, z+29, 98)
    x_length = 10
    z_length = 10
    path_finder = scanner(x_length, z_length, x, y, z)
    heights = copy.deepcopy(path_finder)
    start_node = path_finder[0, 0]
    for i in range(x_length):
        for j in range(z_length):
            cur_node = path_finder[i, j]
            if cur_node > start_node + 5:
                path_finder[i, j] = 1
            else:
                path_finder[i, j] = 0

    x_coords = np.zeros(z_length * x_length, dtype=np.int64)
    x_coords = np.reshape(x_coords, (x_length, z_length))
    z_coords = np.zeros(z_length * x_length, dtype=np.int64)
    z_coords = np.reshape(z_coords, (x_length, z_length))  

    for i in range(x_length):
        for j in range(z_length):
            z_coords[i, j] = z + j
            x_coords[i, j] = x + i
              
    print(heights)
    print(path_finder)
    shortest_path = main(path_finder)
    for i in range(len(shortest_path)):
        for object in shortest_path:
            if heights[object[0]][object[1]] == 0:
                heights[object[0]][object[1]] = prev_height
            mc.setBlocks(x_coords[object[0]][object[1]], heights[object[0]][object[1]] - 1, z_coords[object[0]][object[1]], x_coords[object[0]][object[1]] + 2, heights[object[0]][object[1]] - 1, z_coords[object[0]][object[1]] + 2, 41)
            mc.setBlocks(x_coords[object[0]][object[1]], heights[object[0]][object[1]], z_coords[object[0]][object[1]], x_coords[object[0]][object[1]], heights[object[0]][object[1]] + 50, z_coords[object[0]][object[1]], 0)
            prev_height = heights[object[0]][object[1]]