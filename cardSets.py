from cardInfo import getCardsFromSet
from setConfigs import SET_MAPPING, BASE_CONFIG

class SetSubGroup:
    def __init__(self, setCardList, name, filter):
        self.name = name
        self.subGroupCards = []
        self.groupAveragePrice = 0
        self.groupAverageFoilPrice = 0
        self.subGroupCount = 0
        self.subGroupFoilCount = 0

        for card in setCardList:
            if filter(card):
                self.subGroupCards.append(card)
                self.groupAveragePrice += card.price
                self.subGroupCount += 1

                if card.foilPrice:
                    self.groupAverageFoilPrice += card.foilPrice
                    self.subGroupFoilCount += 1

        if self.subGroupCount != 0:
            self.groupAveragePrice /= self.subGroupCount
        
        if self.subGroupFoilCount != 0:
            self.groupAverageFoilPrice /= self.subGroupFoilCount

    def __len__(self):
        return len(self.subGroupCards)

    def __getitem__(self, cardIndex):
        return self.subGroupCards[cardIndex]

class CardSet:
    def __init__(self, setInfo):
        self.set = setInfo
        self.setCardList = getCardsFromSet(self.set.code)
        
        setBoosterConfig = SET_MAPPING[self.set.code] if self.set.code in SET_MAPPING.keys() else BASE_CONFIG
        self.packSize = setBoosterConfig['packSize']
        self.boosterFactory = setBoosterConfig['generatePackFn']
        self.subGroups = {}

        for key, value in setBoosterConfig['setSubGroups'].items():
            self.subGroups[key] = SetSubGroup(self.setCardList, key, value)

        self.boosterEV = setBoosterConfig['boosterEVFn'](self.subGroups)

    def generateBooster(self):
        return self.boosterFactory(self.subGroups)