WAR_SET_CODE = 'war'

RARITY_COMMON = 'common'
RARITY_UNCOMMON = 'uncommon'
RARITY_RARE = 'rare'
RARITY_MYTHIC = 'mythic'

BASE_MYTHIC_RANGE_L = 1
BASE_MYTHIC_RANGE_H = 8
#Current baseGeneratePackFn assumes chance is a 1 in x chance where x is an int (see setConfigs.py)
BASE_MYTHIC_CHANCE = BASE_MYTHIC_RANGE_L/BASE_MYTHIC_RANGE_H

BASE_RARE_CHANCE = 7/8

BASE_BONUS_FOIL_RANGE_L = 1
BASE_BONUS_FOIL_RANGE_H = 8
#Current baseGeneratePackFn assumes chance is a 1 in x chance where x is an int (see setConfigs.py)
BASE_BONUS_FOIL_CHANCE = BASE_BONUS_FOIL_RANGE_L/BASE_BONUS_FOIL_RANGE_H

BASE_COMMON_COUNT = 10
BASE_UNCOMMON_COUNT = 3