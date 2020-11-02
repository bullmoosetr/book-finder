
import requests
from app.utility.constants import BASE_URL
from settings import API_KEY

"""
    Use this To Search for Works from the Google API 
    Params: search - Search for volumes that contain this text string., 
    subject - Returns results where the text following this keyword is listed in the category list of the volume, 
    author - where the text following this keyword is found in the author
"""
class BaseRequest:

    def __init__(self, search, subject, author=None):
        self.url = BASE_URL
        self.search = search
        self.subject = subject
        self.author = author
    
    def search_by_volumes(self):
        params = {"q" : f"{self.search} subject:{self.subject} inauthor:{self.author}", "key": API_KEY}
        return requests.get(self.url, params=params).json()

    def search_by_volumes_no_author(self):
        params = {"q" : f"{self.search} subject:{self.subject}", "key": API_KEY}
        return requests.get(self.url, params=params).json()