from sets import getOfficialSets
from scryfallAPI import api


officialSets = getOfficialSets()
print(officialSets[0])

cards = api.getCardList('war')
print('hi')
