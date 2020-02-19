class Booster:
    def __init__(self, cardList, foilList):
        self.cardList = cardList
        self.foilList = foilList

        nonFoilCost = 0
        foilCost = 0

        for card in cardList:
            nonFoilCost += card.price

        for card in foilList:
            foilCost += card.foilCost

        self.packValue = foilCost + nonFoilCost

    def __str__(self):
        result = "Pack Value: {}\n".format(self.packValue)
        result += "====Cards====\n"
        
        for card in self.cardList:
            result += str(card) + "\n"

        if len(self.foilList):
            result += "\n====Foils===="
        
            for foil in self.foilList:
                result += str(foil) + "\n"

        return result