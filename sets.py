from scryfallAPI import api
from models import cardSet

def __setMappingFn__(rawSet):
    return cardSet.Set(rawSet['code'], rawSet['name'])

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