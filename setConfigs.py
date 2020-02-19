import random
from booster import Booster

#These values are accuarte for Shards of Alara onwards but some sets have special rules not
#currently accounted for https://mtg.gamepedia.com/Booster_pack
FOIL_CHANCE = 1/8               #Can be any card in the set
MYTHIC_UPGRADE_CHANCE = 1/8
PACK_COMMONS = 10
PACK_UNCOMMONS = 3
PACK_RARE = 1

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
    isMythicUpgrade = True if random.randint(1,8) == 1 else False
    isBonusFoil = True if random.randint(1,8) == 1 else False
    packList = []
    foilList = []

    if isMythicUpgrade:
        packList.append(random.choice(subGroups['mythic']))
    else:
        packList.append(random.choice(subGroups['rare']))

    if isBonusFoil:
        foilList.append(random.choice(subGroups['foil']))

    packList.extend(random.choices(subGroups['uncommons'], k=3))
    packList.extend(random.choices(subGroups['uncommons'], k=10))
    return Booster(packList, foilList)

def basePackEV():
    "See baseGeneratePack"


BASE_CONFIG = {
    'packSize': 15,
    'setSubGroups': {
        'foil': lambda card: card.foilPrice and card.booster,
        'commons': lambda card: card.rarity == "common" and card.booster,
        'uncommons': lambda card: card.rarity == "uncommon" and card.booster,
        'rare': lambda card: card.rarity == "rare" and card.booster,
        'mythic': lambda card: card.rarity == "mythic" and card.booster
    },

    'generatePackFn': baseGeneratePack,
    'boosterEVFn': noop
}