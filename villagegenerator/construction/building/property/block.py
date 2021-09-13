class Block:
    """Minecraft PI block description. Can be sent to Minecraft.setBlock/s"""
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
        return Block(self.id, data)

    def __iter__(self):
        """Allows a Block to be sent whenever id [and data] is needed"""
        return iter((self.id, self.data))
        
    def __repr__(self):
        return "Block(%d, %d)"%(self.id, self.data)

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
WOOD                = Block(17, True)
LEAVES              = Block(18, True)
GLASS               = Block(20)
FLOOR_PATTERN_GREY  = Block(23, False)
SANDSTONE           = Block(24)
NOTE_BLOCK          = Block(25)
BED                 = Block(26, True)
COBWEB              = Block(30)
GRASS_TALL          = Block(31, True)
WOOL                = Block(35, True)
FLOWER_YELLOW       = Block(37)
FLOWER_RED         = Block(38)
MUSHROOM_BROWN      = Block(39)
MUSHROOM_RED        = Block(40)
STONE_SLAB_DOUBLE   = Block(43, True)
STONE_SLAB          = Block(44, True)
BRICK_BLOCK         = Block(45)
BOOKSHELF           = Block(47)
MOSS                = Block(48)
OBSIDIAN            = Block(49)
TORCH               = Block(50, True)
TORTURE_CHAMBER     = Block(52, True)
STAIRS_WOOD         = Block(53, True, 'orientation')
CHEST               = Block(54)
BLOOD               = Block(55)
DIAMOND_ORE         = Block(56)
CRAFTING_TABLE      = Block(58)
SEEDS_WHEAT         = Block(59, True, 'growth_stage')
FARMLAND            = Block(60)     # Put 59 on top of this
FURNACE_INACTIVE    = Block(61)
FURNACE_ACTIVE      = Block(62)
DOOR_OAK            = Block(64, True, 'orientation')
LADDER              = Block(65)
STAIRS_COBBLESTONE  = Block(67, True, 'orientation')
DOOR_IRON           = Block(71, True, 'orientation')
TORCH_REDSTONE      = Block(75)     # TODO: Check if 75 or 76
SNOW                = Block(78, True, 'height')
ICE                 = Block(79)
SNOW_BLOCK          = Block(80)
CACTUS              = Block(81)
CLAY                = Block(82)
JUKEBOX             = Block(84)
FENCE               = Block(85, True, 'orientation')
PUMPKIN             = Block(86, True, 'orientation') 
SOUL_SAND           = Block(88)
GLOWSTONE           = Block(89)
NETHER_PORTAL       = Block(90)     # TODO: Check this
PUMPKIN_LIT         = Block(91, True, 'orientation')
CAKE                = Block(92, True, 'amount_eaten')
STAINED_GLASS       = Block(95, True, 'colors')
TRAPDOOR            = Block(96)
STONE_BRICK         = Block(98, True)       # TODO: Check variation type
IRON_BARS           = Block(101)
GLASS_PANE          = Block(102)
VINE                = Block(106)
FENCE_GATE          = Block(107, True, 'orientation')
STAIRS_BRICK        = Block(108, True, 'orientation')
STAIRS_STONE_BRICK  = Block(109, True, 'orientation')
LILYPAD             = Block(111)
NETHER_BRICK        = Block(112)
FENCE_NETHER_BRICK  = Block(113)        # TODO: Check this
STAIRS_NETHER_BRICK = Block(114, True, 'orientation')
ENCHANTING_TABLE    = Block(116)
BREWING_STAND       = Block(117, True)      # TODO: Check variation type
CAULDRON            = Block(118, True, 'water_level')
SLAB_WOODEN         = Block(125, True)  # TODO: Check variation type
WOODEN_SLAB         = Block(126)        # TODO: Check 125 or 126
STAIRS_SANDSTONE    = Block(128, True, 'orientation')
# TODO: Check in between 128 and 134
STAIRS_SPRUCE       = Block(134, True, 'orientation')
STAIRS_BIRCH        = Block(135, True, 'orientation')
STAIRS_JUNGLE       = Block(136, True, 'orientation')
CACTUS              = Block(140)
CARROT              = Block(141, True, 'growth_stage')
POTATO              = Block(142, True, 'growth_stage')
ANVIL               = Block(145, True, 'orientation')
TRAPPED_CHEST       = Block(146)
PRESSURE_PLATE_GOLD = Block(147)
PRESSURE_PLAYED_WHITE = Block (148)
DAYLIGHT_DETECTOR   = Block(151)       # Patterened flooring
HOPPER              = Block(154, True, 'orientation')   # Looks like pot
PILLAR_QUARTZ       = Block(155, True, 'patterns')
RAIL_ACTIVATOR      = Block(157)
STAIRS_QUARTZ       = Block(156, True, 'orientation')
TERRACOTTA          = Block(159, True, 'colors')
STAINED_GLASS_PANE  = Block(160, True, 'colors')
LEAVES2             = Block(161, True, 'type')
LOG                 = Block(162, True, 'type')
STAIRS_ACACIA       = Block(163, True, 'orientation')
STAIRS_DARK_OAK     = Block(164, True, 'orientation')
TRAPDOOR_IRON       = Block(167)
PRISMARINE          = Block(168, True, 'colors_patterns')
SEA_LANTERN         = Block(169)    # Decoration
HAY_BALE            = Block(170, True, 'orientation')
CARPET              = Block(171, True, 'colors')
TERRACOTTA2         = Block(172)
ICE_PACKED          = Block(174)
FLOWERS             = Block(175, True, 'types')
BANNER              = Block(176, True, 'orientation')
BANNER_LOW          = Block(177, True, 'orientation')
SANDSTONE_RED       = Block(179, True, 'minor')
STAIRS_RED_SANDSTONE= Block(180, True, 'orientation')
SLAB_RED_SANDSTONE  = Block(181)
FENCE_GATE_SPRUCE   = Block(183, True, 'orientation')
FENCE_GATE_BIRCH    = Block(184, True, 'orientation')
FENCE_GATE_JUNGLE   = Block(185, True, 'orientation')
FENCE_GATE_DARK_OAK = Block(186, True, 'orientation')
FENCE_GATE_ACACIA   = Block(187, True, 'orientation')
FENCE_SPRUCE        = Block(188)        # TODO: Check for variation
FENCE_BIRCH         = Block(189)
FENCE_JUNGLE        = Block(190)
FENCE_DARK_OAK      = Block(191)
FENCE_ACACIA        = Block(192)
DOOR_SPRUCE         = Block(193, True, 'orientation')
DOOR_BIRCH          = Block(194, True, 'orientation')
DOOR_JUNGLE         = Block(195, True, 'orientation')
DOOR_ACACIA         = Block(196, True, 'orientation')
DOOR_DARK_OAK       = Block(197, True, 'orientation')
END_ROAD            = Block(198, True, 'orientation')   # Light source
PURPUR_BLOCK        = Block(201)
PURPUR_PILLAR       = Block(202, True, 'minor')
PURPUR_STAIRS       = Block(203, True, 'orientation')
PURPUR_SLAB         = Block(204)
BRICKS_ENDSTONE     = Block(206)        # Highlighter yellow
SEEDS_BEETROOT      = Block(207, True, 'growth_stage')
PATH_GRASS          = Block(208)
BRICKS_NETHER       = Block(215)        # Red and black
# Blocks 219-234 are Shulker Boxes in different colors, each with orientation variation
SHULKER_BOX         = Block(219, True, 'orientation')
# Blocks 235-250 are Terracotta blocks in different colors, each with 4 variation to form a pattern
TERRACOTTA_WHITE_GLAZED = Block(235, True, 'pattern')
CONCRETE            = Block(251, True, 'colors')
CONCRETE_POWDER     = Block(252, True, 'colors')