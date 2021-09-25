MEDI = ['BEACH',
        'COLD_BEACH',
        'DESERT',
        'DESERT_HILLS',
        'MESA',
        'MESA_CLEAR_ROCK',
        'SAVANNA',
        'SAVANNA_ROCK',
        'MESA_ROCK',
        'MUTATED_DESERT',
        'MUTATED_MESA',
        'MUTATED_MESA_CLEAR_ROCK',
        'MUTATED_MESA_ROCK',
        'MUTATED_SAVANNA',
        'MUTATED_SAVANNA_ROCK',
        'STONE_BEACH']

MODERN = ['EXTREME_HILLS',
          'MOUNTAINS',
          'MODIFIED_GRAVELLY_MOUNTAINS',
          'WOODED_MOUNTAINS',
          'BIRCH_FOREST',
          'BIRCH_FOREST_HILLS',
          'EXTREME_HILLS_WITH_TREES',
          'FOREST',
          'FOREST_HILLS',
          'MUTATED_BIRCH_FOREST',
          'MUTATED_BIRCH_FOREST_HILLS',
          'MUTATED_EXTREME_HILLS',
          'MUTATED_EXTREME_HILLS_WITH_TREES',
          'MUTATED_FOREST',
          'MUTATED_PLAINS',
          'PLAINS',
          'SMALLER_EXTREME_HILLS']


def get_player_theme(biome):
    if biome in MEDI:
        return 'medi'
    elif biome in MODERN:
        return 'modern'
    else:
        return 'magic'
