import requests

class API:
    baseURL = "https://api.scryfall.com"
    setListURL = '/sets'

    def __makeAPICall(self, method='GET', requestURL='/', params=None):
        response = None
        
        if method == 'GET':
            response = requests.get(self.baseURL + requestURL, params)

        if response.status_code == 200:
            return response.json()
        else:
            print('Something went wrong with API request')

    def getSetList(self):
        responsePayload = self.__makeAPICall(requestURL = self.setListURL)
        return responsePayload['data']

    def getCardList(self):
        pass

api = API()
