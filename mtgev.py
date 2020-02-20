from setInfo import getOfficialSets
from cardSets import CardSet
import sys

if __name__ == "__main__":
    sets = getOfficialSets()

    if len(sys.argv) > 1 and len(sys.argv[1]) == 3:
        print("Getting Expected Value of Set: {}".format(sys.argv[1]))
        setInfo = next(x for x in sets if x.code == sys.argv[1])
        cardSet = CardSet(setInfo)
        
        print("Expected Value of a pack from {} is: {}".format(setInfo.name, cardSet.boosterEV))

    else:
        print("No valid set code provided, fetching set list...")
        print("Please rerurn again with one of the following 3 letter codes as an argument:\n")
        for cardSet in sets:
            print(cardSet)