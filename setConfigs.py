import random
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
    isMythicUpgrade = True if random.randint(1,8) == 1 else False   #1/8 chance of rare upgrade to mythic
    isBonusFoil = True if random.randint(1,8) == 1 else False       #1/8 chance of foil from the set
    packList = []
    foilList = []

    if isMythicUpgrade:
        packList.append(random.choice(subGroups['mythic']))
    else:
        packList.append(random.choice(subGroups['rare']))

    if isBonusFoil:
        foilList.append(random.choice(subGroups['foil']))

    packList.extend(random.choices(subGroups['uncommon'], k=3))
    packList.extend(random.choices(subGroups['common'], k=10))
    return Booster(packList, foilList)

def basePackEV(subGroups):
    "See baseGeneratePack"
    mythicEV = 1/8*subGroups['mythic'].groupAveragePrice
    rareEV = 7/8*subGroups['rare'].groupAveragePrice
    uncommonEV = 3*subGroups['uncommon'].groupAveragePrice
    commonEV = 10*subGroups['common'].groupAveragePrice
    foilEV = 1/8*subGroups['foil'].groupAverageFoilPrice
    return mythicEV + rareEV + uncommonEV + commonEV + foilEV

BASE_CONFIG = {
    'packSize': 15,
    'setSubGroups': {
        'foil': lambda card: card.foilPrice and card.booster,
        'common': lambda card: card.rarity == "common" and card.booster,
        'uncommon': lambda card: card.rarity == "uncommon" and card.booster,
        'rare': lambda card: card.rarity == "rare" and card.booster,
        'mythic': lambda card: card.rarity == "mythic" and card.booster
    },

    'generatePackFn': baseGeneratePack,
    'boosterEVFn': basePackEV
}