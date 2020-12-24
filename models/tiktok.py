from time import time
from .browser import Browser
import re

class TikTok:
    def __init__(self, account_handle):
        self.account_handle = account_handle
        self.followers = 0
        self.likes = 0
        self._last_update = float('-inf')
        self._cache = None
        self._browser = Browser()
        self.REFRESH_RATE = 60 / 4

    def __update_cache(self):
        if not self._cache or (time() - self._last_update) > self.REFRESH_RATE:
            url = f'https://www.tiktok.com/{self.account_handle}'
            txt = self._browser.get_inner_text_by_class_name(url, 'count-infos')
            vals = txt.split('\n')
            self._cache = []
            for i in range(0, len(vals), 2):
                temp = [vals[i + 1], vals[i]]
                self._cache.append(temp)
            self._last_update = time()

    def _update_followers(self):
        self.followers = self._cache[1][1]

    def _update_likes(self):
        self.likes = self._cache[2][1]

    def refresh_data(self):
        self.__update_cache()
        self._update_followers()
        self._update_likes()