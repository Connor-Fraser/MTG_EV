import random
import consts
from booster import Booster

'''
Sample Config Object
{
    'packSize': 15,
    'setSubGroups': {
        'set': lambda card: card.booster,
        'foil': lambda card: card.foilPrice and card.booster,
        'commons': lambda card: card.rarity == "common" and card.booster,
        'uncommons': lambda card: card.rarity == "uncommon", and card.booster,
        'rare': lambda card: card.rarity == "rare" and card.booster,
        'mythic': lambda card: card.rarity == "mythic" and card.booster
    },

    'generatePackFn': function

    'boosterEVFn': function
}
'''

def noop():
    return None

def baseGeneratePack(subGroups): 
    "For Base Config - Accuarte for Shards of Alara onwards not counting special sets like War of The Spark. See: https://mtg.gamepedia.com/Booster_pack"
    isMythicUpgrade = True if random.randint(consts.BASE_MYTHIC_RANGE_L, consts.BASE_MYTHIC_RANGE_H) == 1 else False
    isBonusFoil = True if random.randint(consts.BASE_BONUS_FOIL_RANGE_L, consts.BASE_BONUS_FOIL_RANGE_H) == 1 else False
    packList = []
    foilList = []

    if isMythicUpgrade:
        packList.append(random.choice(subGroups['mythic']))
    else:
        packList.append(random.choice(subGroups['rare']))

    if isBonusFoil:
        foilList.append(random.choice(subGroups['foil']))

    packList.extend(random.choices(subGroups['uncommon'], k = consts.BASE_UNCOMMON_COUNT))
    packList.extend(random.choices(subGroups['common'], k = consts.BASE_COMMON_COUNT))
    return Booster(packList, foilList)

def basePackEV(subGroups):
    "See baseGeneratePack"
    mythicEV = consts.BASE_MYTHIC_CHANCE*subGroups['mythic'].groupAveragePrice
    rareEV = consts.BASE_RARE_CHANCE*subGroups['rare'].groupAveragePrice
    uncommonEV = consts.BASE_UNCOMMON_COUNT*subGroups['uncommon'].groupAveragePrice
    commonEV = consts.BASE_COMMON_COUNT*subGroups['common'].groupAveragePrice
    foilEV = consts.BASE_BONUS_FOIL_CHANCE*subGroups['foil'].groupAverageFoilPrice
    return mythicEV + rareEV + uncommonEV + commonEV + foilEV

BASE_CONFIG = {
    'packSize': 15,
    'setSubGroups': {
        'foil': lambda card: card.foilPrice and card.booster,
        'common': lambda card: card.rarity == consts.RARITY_COMMON and card.booster,
        'uncommon': lambda card: card.rarity == consts.RARITY_UNCOMMON and card.booster,
        'rare': lambda card: card.rarity == consts.RARITY_RARE and card.booster,
        'mythic': lambda card: card.rarity == consts.RARITY_MYTHIC and card.booster
    },

    'generatePackFn': baseGeneratePack,
    'boosterEVFn': basePackEV
}

def warGeneratePack(subGroups):
    pass

def warPackEV(subGroups):
    pass

WAR_CONFIG = {
    'packSize': 15,
    'setSubGroups': {
        'foil': lambda card: card.foilPrice and card.booster,
        'common': lambda card: card.rarity == consts.RARITY_COMMON and card.booster,
        'uncommonNoPW': lambda card: card.rarity == consts.RARITY_UNCOMMON and card.booster and 'Planeswalker' not in card.type,
        'rareNoPW': lambda card: card.rarity == consts.RARITY_RARE and card.booster and 'Planeswalker' not in card.type,
        'mythicNoPW': lambda card: card.rarity == consts.RARITY_MYTHIC and card.booster and 'Planeswalker' not in card.type,
        'uncommonPW': lambda card: card.rarity == consts.RARITY_UNCOMMON and card.booster and 'Planeswalker' in card.type,
        'rarePW': lambda card: card.rarity == consts.RARITY_RARE and card.booster and 'Planeswalker' in card.type,
        'mythicPW': lambda card: card.rarity == consts.RARITY_MYTHIC and card.booster and 'Planeswalker' in card.type,
        'planeswalker': lambda card: card.rarity == card.booster and 'Planeswalker' in card.type,
    },

    'generatePackFn': warGeneratePack,
    'boosterEVFn': warPackEV
}

SET_MAPPING = {
    consts.WAR_SET_CODE: WAR_CONFIG
}