import requests
import time

class API:
    BASE_URL = "https://api.scryfall.com"
    SET_LIST_URL = '/sets'
    CARD_SEARCH_URL = '/cards/search'
    API_DELAY = 0.1 #API requests a 100ms delay between all requests

    def __makeAPICall(self, method='GET', fullURL=None, requestURL='/', params=None):
        response = None
        URL = fullURL or self.BASE_URL + requestURL
        
        if method == 'GET':
            response = requests.get(URL, params)

        if response.status_code == 200:
            return response.json()
        else:
            print('Something went wrong with API request')

    def __appendApiPagination(self, fullList, responsePayload):
        while responsePayload['has_more']:
            time.sleep(self.API_DELAY) 
            responsePayload = self.__makeAPICall(fullURL = responsePayload['next_page'])
            fullList += responsePayload['data']
        return fullList

    def getSetList(self):
        responsePayload = self.__makeAPICall(requestURL = self.SET_LIST_URL)
        setList = responsePayload['data']
        self.__appendApiPagination(setList, responsePayload)
        return setList

    def getCardList(self, setCode):
        params = {'q':'set:' + setCode, 'order':'rarity'}
        responsePayload = self.__makeAPICall(requestURL=self.CARD_SEARCH_URL, params=params)
        cardList = responsePayload['data']
        self.__appendApiPagination(cardList, responsePayload)
        return cardList

api = API()
