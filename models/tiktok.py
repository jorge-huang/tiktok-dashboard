from time import time
from .browser import Browser

class TikTok:
    def __init__(self, account_handle):
        self.account_handle = account_handle
        self.followers = 0
        self.likes = 0
        self.__last_update = time()
        self.__cache = []
        self.__browser = Browser()
        self.__REFRESH_RATE = 60 / 1

    def __update_cache(self):
        if len(self.__cache) == 0 or (time() - self.__last_update) > self.__REFRESH_RATE:
            self.__cache = self.__browser.get_followers_and_likes(self.account_handle)
            self.__last_update = time()

    def __update_followers(self):
        self.followers = self.__cache[0]

    def __update_likes(self):
        self.likes = self.__cache[1]

    def refresh_data(self):
        try:
            self.__update_cache()
            self.__update_followers()
            self.__update_likes()
        except Exception as e:
            print('FAILED TO REFRESH CACHE', e)
