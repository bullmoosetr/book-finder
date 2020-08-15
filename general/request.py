import requests
from Utility.constants import BASE_URL

class BaseRequest:
    def __init__(self):
        self.url = BASE_URL
    
    def make_request(self):
        requests.get(self.url + self.request_url)

    def search_by_works(self, keyword):
        return requests.get(self.url + '/works?search={0}'.format(keyword))
