from selenium import webdriver
from selenium.webdriver.firefox.options import Options


class Browser:
    def __init__(self):
        options = Options()
        options.headless = True
        self.__browser = webdriver.Firefox(options=options)

    def __navigate_to(self, url):
        self.__browser.get(url)

    def get_followers_and_likes(self, handle):
        self.__navigate_to(f'https://www.tiktok.com/{handle}')
        get_stats_js_str = "JSON.parse(document.getElementById('__NEXT_DATA__').innerText).props.pageProps.userInfo.stats"
        followers = self.__browser.execute_script(f'return {get_stats_js_str}.followerCount')
        likes = self.__browser.execute_script(f'return {get_stats_js_str}.heartCount')

        return (followers, likes)