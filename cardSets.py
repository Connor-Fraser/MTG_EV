from cardInfo import getCardsFromSet

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

        self.groupAveragePrice /= self.subGroupCount
        self.groupAverageFoilPrice /= self.subGroupFoilCount

class CardSet:
    def __init__(self, setInfo, setBoosterConfig):
        self.set = setInfo
        self.setCardList = getCardsFromSet(self.set.code)
        self.packSize = setBoosterConfig['packSize']
        self.generatePack = setBoosterConfig['generatePackFn']
        self.boosterEv = setBoosterConfig['boosterEVFn']
        self.subGroups = {}

        for key, value in setBoosterConfig['setSubGroups'].items():
            self.subGroups[key] = SetSubGroup(self.setCardList, key, value)