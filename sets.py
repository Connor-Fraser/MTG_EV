from scryfallAPI import api

class Set:
    def __init__(self, code, name):
        self.code = code
        self.name = name

    def __str__(self):
        return self.code + ': ' + self.name

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

def __setMappingFn__(rawSet):
    return Set(rawSet['code'], rawSet['name'])

def __cardMappingFn__(rawCard):
    foilPrice = rawCard['prices']['usd_foil'] if rawCard['foil'] else None 
    return Card(rawCard['id'], rawCard['name'], rawCard['rarity'], rawCard['type_line'], rawCard['booster'], rawCard['prices']['usd'], foilPrice)

def getAllSetsRaw():
    return api.getSetList()

def getAllSets():
    allSetsRaw = getAllSetsRaw()
    return list(map(__setMappingFn__, allSetsRaw))

def getOfficialSets():
    allSets = getAllSetsRaw()
    officialSetsRaw = filter(lambda rawSet: len(rawSet['code']) == 3, allSets) #Official sets have a three letter code
    officialSets = list(map(__setMappingFn__, officialSetsRaw))
    return officialSets

def getCardsFromSet(setCode):
    cardListRaw = api.getCardList(setCode)
    setCardList = list(map(__cardMappingFn__, cardListRaw))
    return setCardList
