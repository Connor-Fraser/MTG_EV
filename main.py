from setInfo import getOfficialSets
from cardInfo import getCardsFromSet

officialSets = getOfficialSets()
for x in range(1,10):
    print(officialSets[x])

print('\n******************************\n')

warCardList = getCardsFromSet('war')
for x in range(1,15):
    print(warCardList[x])