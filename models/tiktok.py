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
        self.TIME_OUT = 60 / 2

    def __update_cache(self):
        if not self._cache or (time() - self._last_update) > self.TIME_OUT:
            url = f'https://www.tiktok.com/{self.account_handle}'
            txt = self._browser.get_html_by_class_name(url, 'count-infos')
            fields = ['Following', 'Followers', 'Liles']
            vals = re.findall("\d+", txt)
            self._cache = tuple(zip(fields, vals))
            self._last_update = time()

    def _update_followers(self):
        self.followers = self._cache[1][1]

    def _update_likes(self):
        self.likes = self._cache[2][1]

    def refresh_data(self):
        self.__update_cache()
        self._update_followers()
        self._update_likes()