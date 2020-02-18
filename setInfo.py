from scryfallAPI import getSetList
from functools import lru_cache

class Set:
    def __init__(self, code, name):
        self.code = code
        self.name = name

    def __str__(self):
        return self.code + ': ' + self.name

    @staticmethod
    def apiMappingFn(rawSet):
        return Set(rawSet['code'], rawSet['name'])

def getAllSetsRaw():
    return getSetList()

@lru_cache
def getAllSets():
    allSetsRaw = getAllSetsRaw()
    return list(map(Set.apiMappingFn, allSetsRaw))

@lru_cache
def getOfficialSets():
    allSets = getAllSetsRaw()
    officialSetsRaw = filter(lambda rawSet: len(rawSet['code']) == 3, allSets) #Official sets have a three letter code
    officialSets = list(map(Set.apiMappingFn, officialSetsRaw))
    return officialSets
