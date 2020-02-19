#These values are accuarte for Shards of Alara onwards but some sets have special rules not
#currently accounted for https://mtg.gamepedia.com/Booster_pack

FOIL_CHANCE = 1/8 #Can be any card in the set
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

    'boosterEVFn': function #lambda: return None if not defined
}
'''

def noop():
    return None

BASE_CONFIG = {
    'packSize': 15,
    'setSubGroups': {
        'set': lambda card: card.booster,
        'foil': lambda card: card.foilPrice and card.booster,
        'commons': lambda card: card.rarity == "common" and card.booster,
        'uncommons': lambda card: card.rarity == "uncommon" and card.booster,
        'rare': lambda card: card.rarity == "rare" and card.booster,
        'mythic': lambda card: card.rarity == "mythic" and card.booster
    },

    'generatePackFn': noop,
    'boosterEVFn': noop
}