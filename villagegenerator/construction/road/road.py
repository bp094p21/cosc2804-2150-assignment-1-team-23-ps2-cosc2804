import mcpi.minecraft as minecraft
import mcpi.block as block
import math

# straight
def build_straight_ew():
    class PathEW(): #Path class for the East/West Path
        def __init__(self): #init function for self.mcpi connection as well as block id's 
            self.mc = minecraft.Minecraft.create()
            self.wood = 17

        def get_player_pos(self): #get_player_pos function to get the position of the player in game
            x, y, z = self.mc.player.getTilePos()
            return x, y, z

        def create_path(self, x, y, z): #createPath function to create the East/West path based on current player position
            center = 3 #This is to set the boundaries for the path to enable the path to be centred within a 15x15 area
            for i in range(15): #Loops 15 times over to cover a 15 block radius of below blocks (length of path)
                self.mc.setBlocks(x, y, z+center, x+i, y, z+center, block.LEAVES)
                self.mc.setBlocks(x, y-1, z+center, x+i, y-1, z+center, self.wood)
                self.mc.setBlocks(x, y-1, z+1+center, x+i, y-1, z+1+center, self.wood, 4)
                self.mc.setBlocks(x, y-1, z+2+center, x+i, y-1, z+6+center, block.BRICK_BLOCK)
                self.mc.setBlocks(x, y, z+8+center, x+i, y, z+8+center, block.LEAVES)
                self.mc.setBlocks(x, y-1, z+8+center, x+i, y-1, z+8+center, self.wood)
                self.mc.setBlocks(x, y-1, z+7+center, x+i, y-1, z+7+center, self.wood, 4)

            self.mc.setBlock(x+2, y-1, z+4+center, block.GLOWSTONE_BLOCK) #Will create evenly placed glowstone blocks down the center of the path
            self.mc.setBlock(x+7, y-1, z+4+center, block.GLOWSTONE_BLOCK)
            self.mc.setBlock(x+12, y-1, z+4+center, block.GLOWSTONE_BLOCK)

    craft = PathEW() #Initialise a variable to access the path class
    x, y, z = craft.get_player_pos() #Inistialise variables for the current player position
    craft.create_path(x, y, z) #Create the path using current player position

def build_straight_ns():
    class PathNS(): #Path class for the North/South Path
        def __init__(self): #init function for self.mcpi connection as well as block id's 
            self.mc = minecraft.Minecraft.create()
            self.wood = 17

        def get_player_pos(self): #get_player_pos function to get the position of the player in game
            x, y, z = self.mc.player.getTilePos()
            return x, y, z

        def create_path(self, x, y, z): #createPath function to create the North/South path based on current player position
            center = 3 #This is to set the boundaries for the path to enable the path to be centred within a 15x15 area
            for i in range(15): #Loops 15 times over to cover a 15 block radius of below blocks (length of path)
                self.mc.setBlocks(x+center, y, z, x+center, y, z+i, block.LEAVES)
                self.mc.setBlocks(x+center, y-1, z, x+center, y-1, z+i, self.wood)
                self.mc.setBlocks(x+1+center, y-1, z, x+1+center, y-1, z+i, self.wood, 4)
                self.mc.setBlocks(x+2+center, y-1, z, x+6+center, y-1, z+i, block.BRICK_BLOCK)
                self.mc.setBlocks(x+8+center, y, z, x+8+center, y, z+i, block.LEAVES)
                self.mc.setBlocks(x+8+center, y-1, z, x+8+center, y-1, z+i, self.wood)
                self.mc.setBlocks(x+7+center, y-1, z, x+7+center, y-1, z+i, self.wood, 4)

            self.mc.setBlock(x+4+center, y-1, z+2, block.GLOWSTONE_BLOCK) #Will create evenly placed glowstone blocks down the center of the path
            self.mc.setBlock(x+4+center, y-1, z+7, block.GLOWSTONE_BLOCK)
            self.mc.setBlock(x+4+center, y-1, z+12, block.GLOWSTONE_BLOCK)

    craft = PathNS() #Initialise a variable to access the path class
    x, y, z = craft.get_player_pos() #Inistialise variables for the current player position
    craft.create_path(x, y, z) #Create the path using current player position

# bent
def build_bent_connecting_se():
    class PathSE():
        def __init__(self):
            self.mc = minecraft.Minecraft.create()
        
        def get_player_pos(self):
            x, y, z = self.mc.player.getTilePos()
            return x, y, z
    
        def create_curve(self, x, y, z):
            radius = 11.5
            curve = [17, [17,4], 45, 45, 45, 45, 45, [17,4], 17]
            for angle in range(181, 270):
                for i in range(len(curve)):
                    new_x = x + (radius - i) * math.cos(angle*math.pi/180)
                    new_z = z + (radius - i) * math.sin(angle*math.pi/180)
                    self.mc.setBlock(new_x + 15, y-1, new_z + 15, curve[i])
                    if i == 8:
                        self.mc.setBlock(new_x + 15, y, new_z + 15, block.LEAVES)
                new_x = x + (radius) * math.cos(angle*math.pi/180)
                new_z = z + (radius) * math.sin(angle*math.pi/180)
                self.mc.setBlock(new_x + 15, y, new_z + 15, block.LEAVES)
            self.mc.setBlock(x + 12, y - 1, z + 7, block.GLOWSTONE_BLOCK)
            self.mc.setBlock(x + 7, y - 1, z + 12, block.GLOWSTONE_BLOCK)
    
    craft = PathSE() #Initialise a variable to access the path class
    x, y, z = craft.get_player_pos() #Inistialise variables for the current player position
    craft.create_curve(x, y, z) #Create the path using current player position

def build_bent_connecting_sw():
    class PathSW():
        def __init__(self):
            self.mc = minecraft.Minecraft.create()
        
        def get_player_pos(self):
            x, y, z = self.mc.player.getTilePos()
            return x, y, z
    
        def create_curve(self, x, y, z):
            radius = 11.5
            curve = [17, [17,4], 45, 45, 45, 45, 45, [17,4], 17]
            for angle in range(271, 360):
                for i in range(len(curve)):
                    new_x = x + (radius - i) * math.cos(angle*math.pi/180)
                    new_z = z + (radius - i) * math.sin(angle*math.pi/180)
                    self.mc.setBlock(new_x, y-1, new_z + 15, curve[i])
                    if i == 8:
                        self.mc.setBlock(new_x, y, new_z + 15, block.LEAVES)
                new_x = x + (radius) * math.cos(angle*math.pi/180)
                new_z = z + (radius) * math.sin(angle*math.pi/180)
                self.mc.setBlock(new_x, y, new_z + 15, block.LEAVES)
            self.mc.setBlock(x + 2, y - 1, z + 7, block.GLOWSTONE_BLOCK)
            self.mc.setBlock(x + 7, y - 1, z + 12, block.GLOWSTONE_BLOCK)
            
    craft = PathSW() #Initialise a variable to access the path class
    x, y, z = craft.get_player_pos() #Inistialise variables for the current player position
    craft.create_curve(x, y, z) #Create the path using current player position      

def build_bent_connecting_ne():
    class PathNE():
        def __init__(self):
            self.mc = minecraft.Minecraft.create()

        def get_player_pos(self):
            x, y, z = self.mc.player.getTilePos()
            return x, y, z

        def create_curve(self, x, y, z):
            radius = 11.5
            curve = [17, [17,4], 45, 45, 45, 45, 45, [17,4], 17]
            for angle in range(91, 180):
                for i in range(len(curve)):
                    new_x = x + (radius - i) * math.cos(angle*math.pi/180)
                    new_z = z + (radius - i) * math.sin(angle*math.pi/180)
                    self.mc.setBlock(new_x + 15, y-1, new_z, curve[i])
                    if i == 8:
                        self.mc.setBlock(new_x + 15, y, new_z, block.LEAVES)
                new_x = x + (radius) * math.cos(angle*math.pi/180)
                new_z = z + (radius) * math.sin(angle*math.pi/180)
                self.mc.setBlock(new_x + 15, y, new_z, block.LEAVES)
            self.mc.setBlock(x + 7, y - 1, z + 2, block.GLOWSTONE_BLOCK)
            self.mc.setBlock(x + 12, y - 1, z + 7, block.GLOWSTONE_BLOCK)

    craft = PathNE() #Initialise a variable to access the path class
    x, y, z = craft.get_player_pos() #Inistialise variables for the current player position
    craft.create_curve(x, y, z) #Create the path using current player position  

def build_bent_connecting_nw():
    class PathNW():
        def __init__(self):
            self.mc = minecraft.Minecraft.create()

        def get_player_pos(self):
            x, y, z = self.mc.player.getTilePos()
            return x, y, z

        def create_curve(self, x, y, z):
            radius = 11.5
            curve = [17, [17,4], 45, 45, 45, 45, 45, [17,4], 17]
            for angle in range(90):
                for i in range(len(curve)):
                    new_x = x + (radius - i) * math.cos(angle*math.pi/180)
                    new_z = z + (radius - i) * math.sin(angle*math.pi/180)
                    self.mc.setBlock(new_x , y-1, new_z, curve[i])
                    if i == 8:
                        self.mc.setBlock(new_x, y, new_z, block.LEAVES)
                new_x = x + (radius) * math.cos(angle*math.pi/180)
                new_z = z + (radius) * math.sin(angle*math.pi/180)
                self.mc.setBlock(new_x, y, new_z, block.LEAVES)
            self.mc.setBlock(x + 7, y - 1, z + 2, block.GLOWSTONE_BLOCK)
            self.mc.setBlock(x + 2, y - 1, z + 7, block.GLOWSTONE_BLOCK)

    craft = PathNW() #Initialise a variable to access the path class
    x, y, z = craft.get_player_pos() #Inistialise variables for the current player position
    craft.create_curve(x, y, z) #Create the path using current player position

# intersection
def build_crossintersection():
    class Intersection(): #Path class for the intersection path
        def __init__(self): #init function for self.mcpi connection as well as block id's 
            self.mc = minecraft.Minecraft.create()
            self.wood = 17

        def get_player_pos(self): #get_player_pos function to get the position of the player in game
            x, y, z = self.mc.player.getTilePos()
            return x, y, z

        def create_intersection(self, x, y, z): #createPath function to create the East/West path based on current player position
            center = 3 #This is to set the boundaries for the path to enable the path to be centred within a 15x15 area
            for i in range(15): #Loops 15 times over to cover a 15 block radius of below blocks (length of path)
                self.mc.setBlocks(x, y, z+center, x+i, y, z+center, block.LEAVES)
                self.mc.setBlocks(x, y-1, z+center, x+i, y-1, z+center, self.wood)
                self.mc.setBlocks(x, y-1, z+1+center, x+i, y-1, z+1+center, self.wood, 4)
                self.mc.setBlocks(x, y-1, z+2+center, x+i, y-1, z+6+center, block.BRICK_BLOCK)
                self.mc.setBlocks(x, y, z+8+center, x+i, y, z+8+center, block.LEAVES)
                self.mc.setBlocks(x, y-1, z+8+center, x+i, y-1, z+8+center, self.wood)
                self.mc.setBlocks(x, y-1, z+7+center, x+i, y-1, z+7+center, self.wood, 4)

            for i in range(15): #Loops 15 times over to cover a 15 block radius of below blocks (length of path)
                self.mc.setBlocks(x+center, y, z, x+center, y, z+i, block.LEAVES)
                self.mc.setBlocks(x+center, y-1, z, x+center, y-1, z+i, self.wood)
                self.mc.setBlocks(x+1+center, y-1, z, x+1+center, y-1, z+i, self.wood, 4)
                self.mc.setBlocks(x+2+center, y-1, z, x+6+center, y-1, z+i, block.BRICK_BLOCK)
                self.mc.setBlocks(x+8+center, y, z, x+8+center, y, z+i, block.LEAVES)
                self.mc.setBlocks(x+8+center, y-1, z, x+8+center, y-1, z+i, self.wood)
                self.mc.setBlocks(x+7+center, y-1, z, x+7+center, y-1, z+i, self.wood, 4)

            self.mc.setBlocks(x+center, y, z+4, x+center, y, z+10, block.AIR) #Removes the leaves that are in the way from intersecting paths
            self.mc.setBlocks(x+center+8, y, z+4, x+center+8, y, z+10, block.AIR)
            self.mc.setBlocks(x+10, y, z+4, x+center+1, y, z+center, block.AIR)
            self.mc.setBlocks(x+10, y, z+4, x+center+1, y, z+center+8, block.AIR)

            self.mc.setBlocks(x, y-1, z+center+1, x+14, y-1, z+center+7, block.BRICK_BLOCK) #Replace the whole EW path with bricks
            self.mc.setBlocks(x, y-1, z+center+1, x+4, y-1, z+center+1, self.wood, 4) #Lay out wood appropriately
            self.mc.setBlocks(x+10, y-1, z+center+1, x+14, y-1, z+center+1, self.wood, 4)
            self.mc.setBlocks(x, y-1, z+center+7, x+4, y-1, z+center+7, self.wood, 4)
            self.mc.setBlocks(x+10, y-1, z+center+7, x+14, y-1, z+center+7, self.wood, 4)

            self.mc.setBlock(x+4+center, y-1, z+2, block.GLOWSTONE_BLOCK) #Will create evenly placed glowstone blocks down the center of the path
            self.mc.setBlock(x+4+center, y-1, z+12, block.GLOWSTONE_BLOCK)
            self.mc.setBlock(x+2, y-1, z+4+center, block.GLOWSTONE_BLOCK)
            self.mc.setBlock(x+7, y-1, z+4+center, block.GLOWSTONE_BLOCK)
            self.mc.setBlock(x+12, y-1, z+4+center, block.GLOWSTONE_BLOCK)
        
    craft = Intersection() #Initialise a variable to access the path class
    x, y, z = craft.get_player_pos() #Inistialise variables for the current player position
    craft.create_intersection(x, y, z) #Create the path using current player position
