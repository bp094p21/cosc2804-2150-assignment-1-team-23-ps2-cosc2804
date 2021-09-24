class Block:
    """Minecraft PI block description w/ slight modifications and custom dictionaries. To be used in Minecraft.setBlock/s"""
    def __init__(self, id, has_variation=False, variation_type=None, data=0):
        self.id = id
        self.data = data
        self.has_variation = has_variation
        self.variation_type = variation_type
    def __eq__(self, rhs):
        return self.id == rhs.id and self.data == rhs.data
    def __hash__(self):
        return (self.id << 8) + self.data
    def withData(self, data):
        new_block = Block(self.id, data=data)
        return new_block
    def __iter__(self):
        """Allows a Block to be sent whenever id [and data] is needed"""
        return iter((self.id, self.data))
    def __repr__(self):
        return f"Block id: {self.id}, data: {self.data}, has_variation: {self.has_variation}, variation_type: {self.variation_type}"

# List of usable blocks for building property and house components
#region
AIR                 = Block(0)
STONE               = Block(1)
GRASS               = Block(2)
DIRT                = Block(3)
COBBLESTONE         = Block(4)
WOOD_PLANKS         = Block(5, True)
SAPLING             = Block(6, True)
WATER_FLOWING       = Block(8)
WATER               = WATER_FLOWING
WATER_STATIONARY    = Block(9)
LAVA_FLOWING        = Block(10)
LAVA                = LAVA_FLOWING
LAVA_STATIONARY     = Block(11)
SAND                = Block(12)
GRAVEL              = Block(13)
TIMBER_LOG          = Block(17, True, 'types')  # 0 Oak, 1 Spruce
LEAVES              = Block(18, True)   # 0 Oak, 1 Spruce, 2 Birch, 3 Jungle
GLASS_BLOCK         = Block(20)
FLOOR_PATTERN_GREY  = Block(23, False)
SANDSTONE           = Block(24)
NOTE_BLOCK          = Block(25)
BED                 = Block(26, True)
COBWEB              = Block(30)
GRASS_TALL          = Block(31, True)
WOOL                = Block(35, True)
FLOWER_YELLOW       = Block(37)
FLOWER_RED          = Block(38)
MUSHROOM_BROWN      = Block(39)
MUSHROOM_RED        = Block(40)
SLAB                = Block(43, True, 'types')
BRICK_BLOCK         = Block(45)
BOOKSHELF           = Block(47)
MOSSY_COBBLESTONE   = Block(48)
OBSIDIAN            = Block(49)
TORCH               = Block(50, True, 'orientation') # mc.setBlock(id, subtype) # Light source - Bright
TORTURE_CHAMBER     = Block(52, True)
STAIRS_WOOD         = Block(53, True, 'orientation')
CHEST               = Block(54, True, 'orientation')
BLOOD               = Block(55)     # Decoration
DIAMOND_ORE         = Block(56)
CRAFTING_TABLE      = Block(58)     # Decoration
SEEDS_WHEAT         = Block(59, True, 'growth_stage')
FARMLAND            = Block(60)     # Put 59 on top of this
FURNACE_INACTIVE    = Block(61)
FURNACE_ACTIVE      = Block(62)
DOOR_OAK            = Block(64, True, 'orientation')
LADDER              = Block(65)
STAIRS_COBBLESTONE  = Block(67, True, 'orientation')
DOOR_IRON           = Block(71, True, 'orientation')
TORCH_REDSTONE      = Block(75)     # Same as 76    # Light source - Dim
SNOW                = Block(78, True, 'height')
ICE                 = Block(79)
SNOW_BLOCK          = Block(80)
CACTUS              = Block(81)
CLAY                = Block(82)
JUKEBOX             = Block(84)
FENCE_OAK           = Block(85, True, 'orientation')
PUMPKIN             = Block(86, True, 'orientation') 
NETHERRACK          = Block(87)     # Fireplace under chimney
SOUL_SAND           = Block(88)
GLOWSTONE           = Block(89)
PUMPKIN_LIT         = Block(91, True, 'orientation')
CAKE                = Block(92, True, 'amount_eaten')       # Decoration
STAINED_GLASS_BLOCK = Block(95, True, 'colors')
TRAPDOOR            = Block(96)
STONE_BRICK         = Block(98, True, 'types')       # 
IRON_BARS           = Block(101)
GLASS_PANE          = Block(102)
VINE                = Block(106)    # Decoration
FENCE_GATE_OAK      = Block(107, True, 'orientation')
STAIRS_BRICK        = Block(108, True, 'orientation')
STAIRS_STONE_BRICK  = Block(109, True, 'orientation')
LILYPAD             = Block(111)        # Decoration
NETHER_BRICK_PURPLE = Block(112)    # Use 215 for red
FENCE_NETHER_BRICK  = Block(113, True, 'orientation') 
STAIRS_NETHER_BRICK = Block(114, True, 'orientation')
ENCHANTING_TABLE    = Block(116)    # Decoration
BREWING_STAND       = Block(117, True, 'pattern')      # Decoration
CAULDRON            = Block(118, True, 'water_level')   # Decoration
SLAB_WOODEN         = Block(125, True, 'types')  # Same as 126
STAIRS_SANDSTONE    = Block(128, True, 'orientation')
STAIRS_SPRUCE       = Block(134, True, 'orientation')
STAIRS_BIRCH        = Block(135, True, 'orientation')
STAIRS_JUNGLE       = Block(136, True, 'orientation')
CACTUS              = Block(140)
CARROT              = Block(141, True, 'growth_stage')  # Decoration
POTATO              = Block(142, True, 'growth_stage')  # Decoration
ANVIL               = Block(145, True, 'orientation')  # Decoration
TRAPPED_CHEST       = Block(146, True, 'orientation')  # Decoration
PRESSURE_PLATE_GOLD = Block(147)  # Decoration
PRESSURE_PLAYED_WHITE = Block (148)  # Decoration
DAYLIGHT_DETECTOR   = Block(151)       # Patterened flooring  # Decoration
PILLAR_QUARTZ       = Block(155, True, 'patterns')
RAIL_ACTIVATOR      = Block(157)
STAIRS_QUARTZ       = Block(156, True, 'orientation')
TERRACOTTA          = Block(159, True, 'colors')
STAINED_GLASS_PANE  = Block(160, True, 'colors')
LEAVES2             = Block(161, True, 'type')  # 0 Acacia, 1 Dark Oak
LOG                 = Block(162, True, 'type_orientation') # 0 Acacia, 1 Dark Oak
STAIRS_ACACIA       = Block(163, True, 'orientation')
STAIRS_DARK_OAK     = Block(164, True, 'orientation')
TRAPDOOR_IRON       = Block(167)
PRISMARINE          = Block(168, True, 'colors_patterns')
SEA_LANTERN         = Block(169)    # Light source      # Decoration
HAY_BALE            = Block(170, True, 'orientation')
CARPET              = Block(171, True, 'colors')
TERRACOTTA2         = Block(172)
ICE_PACKED          = Block(174)
FLOWERS             = Block(175, True, 'types')     # Decoration
BANNER              = Block(176, True, 'orientation')   # Decoration
BANNER_LOW          = Block(177, True, 'orientation')   # Decoration
SANDSTONE_RED       = Block(179, True, 'minor')
STAIRS_RED_SANDSTONE= Block(180, True, 'orientation')
SLAB_RED_SANDSTONE  = Block(181)
FENCE_GATE_SPRUCE   = Block(183, True, 'orientation')       # 0 = x direction, 1 = z direction
FENCE_GATE_BIRCH    = Block(184, True, 'orientation')
FENCE_GATE_JUNGLE   = Block(185, True, 'orientation')
FENCE_GATE_DARK_OAK = Block(186, True, 'orientation')
FENCE_GATE_ACACIA   = Block(187, True, 'orientation')
FENCE_SPRUCE        = Block(188, True, 'orientation')        
FENCE_BIRCH         = Block(189, True, 'orientation')
FENCE_JUNGLE        = Block(190, True, 'orientation')
FENCE_DARK_OAK      = Block(191, True, 'orientation')
FENCE_ACACIA        = Block(192, True, 'orientation')
DOOR_SPRUCE         = Block(193, True, 'orientation')
DOOR_BIRCH          = Block(194, True, 'orientation')
DOOR_JUNGLE         = Block(195, True, 'orientation')
DOOR_ACACIA         = Block(196, True, 'orientation')
DOOR_DARK_OAK       = Block(197, True, 'orientation')
END_ROD             = Block(198, True, 'orientation')   # Light source # Decoration
PURPUR_BLOCK        = Block(201)
PURPUR_PILLAR       = Block(202, True, 'minor')
PURPUR_STAIRS       = Block(203, True, 'orientation')
PURPUR_SLAB         = Block(204)
BRICKS_VANILLA      = Block(206)
SEEDS_BEETROOT      = Block(207, True, 'growth_stage')
PATH_GRASS          = Block(208)
BRICKS_NETHER_RED   = Block(215)    # Use 112 for Purple
# Blocks 235-250 are Terracotta blocks in different colors, each with 4 variation to form a pattern
TERRACOTTA1 = Block(235, True, 'pattern')
TERRACOTTA2 = Block(236, True, 'pattern')
TERRACOTTA3 = Block(238, True, 'pattern')
CONCRETE            = Block(251, True, 'colors')
CONCRETE_POWDER     = Block(252, True, 'colors')
#endregion

### LISTS BY BLOCK TYPE ###

FURNACE = {
    'inactive': FURNACE_INACTIVE,
    'active': FURNACE_ACTIVE
}
LOGS = {
    'vertical': {
        'oak': TIMBER_LOG.withData(0),
        'spruce': TIMBER_LOG.withData(1),
        'birch': TIMBER_LOG.withData(2),
        'jungle': TIMBER_LOG.withData(3),
        'acacia': LOG.withData(0),
        'dark_oak': LOG.withData(1)
    }
}
LEAFAGE = {
    'oak': LEAVES.withData(0),
    'spruce': LEAVES.withData(1),
    'birch': LEAVES.withData(2),
    'jungle': LEAVES.withData(3),
    'acacia': LEAVES2.withData(0),
    'dark_oak': LEAVES2.withData(1)
}
# Blocks for roof
CUBES = {
    'smooth_stone': [Block(43, 0), Block(43, 8)],
    'sandstone': Block(43, 1),
    'petrified_oak': Block(43, 2),
    'cobblestone': Block(43, 3),
    'brick': Block(43, 4),
    'stone_brick': Block(43, 5),
    'nether_brick': Block(43, 6),
    'quartz': Block(43, 7),
    'sandstone': SANDSTONE,
    'oak': WOOD_PLANKS.withData(0),
    'spruce': WOOD_PLANKS.withData(1),
    'birch': WOOD_PLANKS.withData(2),
    'jungle': WOOD_PLANKS.withData(3),
    'acacia': WOOD_PLANKS.withData(4),
    'dark_oak': WOOD_PLANKS.withData(5),
    'red_sandstone': SANDSTONE_RED,
    'purpur': PURPUR_BLOCK
}
SLABS = {
    'smooth_stone': [Block(43, 0), Block(43, 8)],
    'sandstone': Block(43, 1),
    'petrified_oak': Block(43, 2),
    'cobblestone': Block(43, 3),
    'brick': Block(43, 4),
    'stone_brick': Block(43, 5),
    'nether_brick': Block(43, 6),
    'quartz': Block(43, 7),
    'oak': SLAB_WOODEN.withData(0),
    'spruce': SLAB_WOODEN.withData(1),
    'birch': SLAB_WOODEN.withData(2),
    'jungle': SLAB_WOODEN.withData(3),
    'acacia': SLAB_WOODEN.withData(4),
    'dark_oak': SLAB_WOODEN.withData(5),
    'red_sandstone': SLAB_RED_SANDSTONE,
    'purpur': PURPUR_SLAB
}
SLABS_TOP = {
    'smooth_stone': Block(43, 8),
    'sandstone': Block(44, 9),
    'petrified_oak': Block(44, 10),
    'cobblestone': Block(44, 11),
    'brick': Block(44, 12),
    'stone_brick': Block(44, 13),
    'nether_brick': Block(44, 14),
    'quartz': Block(44, 15),
    'oak': SLAB_WOODEN.withData(8),
    'spruce': SLAB_WOODEN.withData(9),
    'birch': SLAB_WOODEN.withData(10),
    'jungle': SLAB_WOODEN.withData(11),
    'acacia': SLAB_WOODEN.withData(12),
    'dark_oak': SLAB_WOODEN.withData(13),
    'wooden': Block(44, 2),
    'red_sandstone': SLAB_RED_SANDSTONE.withData(8),
    'purpur': PURPUR_SLAB.withData(8),
}
STAIRS = [STAIRS_WOOD, STAIRS_COBBLESTONE, STAIRS_BRICK, STAIRS_STONE_BRICK, STAIRS_NETHER_BRICK, STAIRS_SANDSTONE, STAIRS_SPRUCE, STAIRS_BIRCH, STAIRS_JUNGLE, STAIRS_QUARTZ, STAIRS_ACACIA, STAIRS_DARK_OAK, STAIRS_RED_SANDSTONE, PURPUR_STAIRS]

BEDS = {
    'list': [],
    'color': {
        'blue': None,
    }
}

# Blocks by theme
OPTIONS = {
    'medi': {
        'boundary': {
            'basic': [TERRACOTTA, SANDSTONE, SANDSTONE_RED],
            'designer': [TERRACOTTA1, TERRACOTTA2, TERRACOTTA3]
        },
        'carpet': {
            'basic': [CARPET]
        },
        'door': {
            'basic': [DOOR_ACACIA, DOOR_BIRCH]
        },
        'fence': {
            'basic': [FENCE_ACACIA, FENCE_BIRCH],
            'designer': [FENCE_BIRCH]
        },
        'gate': {
            'basic': [AIR],
            'designer': [FENCE_GATE_ACACIA, FENCE_GATE_BIRCH],
            'pool': [FENCE_GATE_ACACIA, FENCE_GATE_BIRCH]
        },
        'floor': {
            'basic': [TERRACOTTA, SANDSTONE, SANDSTONE_RED],
            'designer': [TERRACOTTA1, TERRACOTTA2, TERRACOTTA3]
        },
        'ground': {
            'basic': [SAND, GRAVEL]
        },
        'path': {
            'basic': [TERRACOTTA, SANDSTONE, SANDSTONE_RED],
        },
        'pool_fill': {
            'basic': [WATER]
        },
        'pool_line': {
            'basic': [TERRACOTTA],
            'designer': [TERRACOTTA1, TERRACOTTA2, TERRACOTTA3]
        },
        'roof': {
            'stair': [STAIRS_WOOD, STAIRS_RED_SANDSTONE, STAIRS_ACACIA, STAIRS_SPRUCE],
            'slab': [SLABS['oak'], SLABS['red_sandstone'], SLABS['acacia'], SLABS['spruce']],
            'cube': [CUBES['oak'], CUBES['red_sandstone'], CUBES['acacia'], CUBES['spruce']]
        },
        'stairs': {
            'basic': [STAIRS_SANDSTONE, STAIRS_WOOD],
            'designer': [STAIRS_RED_SANDSTONE, STAIRS_QUARTZ]
        },
        'steps': {
            'basic': [SLABS['sandstone'], SLABS['brick'], SLABS['spruce'], SLABS['acacia'], SLABS['red_sandstone']],
            'designer': [SLABS['red_sandstone'], SLABS['quartz']]
        },
        'tree': {
            'trunk': [LOGS['vertical']['acacia'], LOGS['vertical']['oak'], LOGS['vertical']['spruce']],
            'leaves': [LEAFAGE['acacia'], LEAFAGE['oak'], LEAFAGE['spruce']]
        },
        'wall': {
            'basic': [TERRACOTTA, SANDSTONE],
            'designer': [TERRACOTTA1, TERRACOTTA2, TERRACOTTA3]
        },
        'window': {
            'basic': [GLASS_BLOCK],
            'designer': [STAINED_GLASS_BLOCK.withData(x) for x in range(10)]
        },
    }
}

# TESTING

if __name__ == '__main__':
    from mcpi import minecraft
    mc = minecraft.Minecraft.create()
    x,y,z = mc.player.getPos()
    block = CONCRETE.withData(1)
    mc.setBlock(x,y,z,block)