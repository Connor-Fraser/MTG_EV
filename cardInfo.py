from scryfallAPI import getCardList
from functools import lru_cache

class Card:
    def __init__(self, id, name, rarity, cardType, booster, price, foilPrice=None):
        self.id = id
        self.name = name
        self.rarity = rarity
        self.type = cardType
        self.booster = booster
        self.price = price
        self.foilPrice = foilPrice

    def __str__(self):
        return "{}  ({}): ${}   F${}".format(self.name, self.rarity, self.price, self.foilPrice)

    @staticmethod
    def apiMappingFn(rawCard):
        foilPrice = rawCard['prices']['usd_foil'] if rawCard['foil'] else None 
        return Card(rawCard['id'], rawCard['name'], rawCard['rarity'], rawCard['type_line'], rawCard['booster'], rawCard['prices']['usd'], foilPrice)

@lru_cache(maxsize=15)
def getCardsFromSet(setCode):
    cardListRaw = getCardList(setCode)
    setCardList = list(map(Card.apiMappingFn, cardListRaw))
    return setCardList
