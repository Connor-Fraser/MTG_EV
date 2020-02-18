import requests
import time


BASE_URL = "https://api.scryfall.com"
SET_LIST_URL = '/sets'
CARD_SEARCH_URL = '/cards/search'
API_DELAY = 0.1 #API requests a 100ms delay between all requests

def __makeAPICall(method='GET', fullURL=None, requestURL='/', params=None):
    response = None
    URL = fullURL or BASE_URL + requestURL
    
    if method == 'GET':
        response = requests.get(URL, params)

    if response.status_code == 200:
        return response.json()
    else:
        print('Something went wrong with API request')

def __appendApiPagination(fullList, responsePayload):
    while responsePayload['has_more']:
        time.sleep(API_DELAY) 
        responsePayload = __makeAPICall(fullURL = responsePayload['next_page'])
        fullList += responsePayload['data']
    return fullList

def getSetList():
    responsePayload = __makeAPICall(requestURL = SET_LIST_URL)
    setList = responsePayload['data']
    __appendApiPagination(setList, responsePayload)
    return setList

def getCardList(setCode):
    params = {'q':'set:' + setCode, 'order':'rarity'}
    responsePayload = __makeAPICall(requestURL=CARD_SEARCH_URL, params=params)
    cardList = responsePayload['data']
    __appendApiPagination(cardList, responsePayload)
    return cardList
