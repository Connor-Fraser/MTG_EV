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

INVALID_SETS = [
    "j20","ha1","gn2","ptg","c19","ss2","j19","gk2","uma","g18","gnt","gk1",
    "c18","ana","gs1","ss1","bbd","cm2","ddu","a25","j18","f18","v17","ima","ddt","g17","h17","htr","c17",
    "e01","cma","w17","dds","mm3","l17","f17","j17","pca","pz2","c16","v16","ema","w16","ddq","ogw","l16",
    "j16","f16","pz1","c15","exp","ddp","v15","cp3","ori","mm2","tpr","ddo","cp2","l15","j15","f15","gvl",
    "evg","dvd","jvc","c14","ddn","v14","cp1","vma","md1","ddm","l14","f14","j14","c13","ddl","v13","ddk",
    "l13","f13","j13","cm1","ddj","v12","pc2","ddi","l12","f12","j12","pd3","ddh","v11","cmd","td2","ddg",
    "me4","p11","f11","g11","pd2","td0","ddf","v10","dpa","dde","f10","g10","p10","h09","ddd","me3","hop",
    "v09","ddc","f09","p09","g09","dd2","me2","drb","f08","p08","g08","dd1","me1","p07","f07","g07","cst",
    "f06","p06","g06","f05","p05","g05","p04","f04","g04","p03","f03","g03","phj","prm","p02","f02","g02",
    "dkm","f01","g01","btd","s00","fnm","g00","brb","s99","g99","jgp","itp","mgb","rqs","ptc","cei","ced",
]