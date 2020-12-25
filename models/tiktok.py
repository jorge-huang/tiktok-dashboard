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
        self.REFRESH_RATE = 60 / 4

    def __update_cache(self):
        if (time() - self.__last_update) < self.REFRESH_RATE:
            return

        url = f'https://www.tiktok.com/{self.account_handle}'
        txt = self.__browser.get_inner_text_by_class_name(url, 'count-infos')
        vals = txt.split('\n')
        self.__cache = []
        for i in range(0, len(vals), 2):
            temp = [vals[i + 1], vals[i]]
            self.__cache.append(temp)
        self.__last_update = time()

    def __update_followers(self):
        self.followers = self.__cache[1][1]

    def __update_likes(self):
        self.likes = self.__cache[2][1]

    def refresh_data(self):
        try:
            self.__update_cache()
            self.__update_followers()
            self.__update_likes()
        except Exception as e:
            print('FAILED TO REFRESH CACHE', e)
