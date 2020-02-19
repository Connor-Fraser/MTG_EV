from setInfo import getOfficialSets
from cardInfo import getCardsFromSet
from cardSets import CardSet
from setConfigs import BASE_CONFIG

officialSets = getOfficialSets()
for x in range(1,10):
    print(officialSets[x])

print('\n******************************\n')

warCardList = getCardsFromSet('war')
for x in range(1,15):
    print(warCardList[x])

print('\n******************************\n')

TBDCardSet = CardSet(officialSets[1], BASE_CONFIG)
TBDBooster = TBDCardSet.generateBooster()
print(TBDBooster)
