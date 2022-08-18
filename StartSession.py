import pickle
from selenium import webdriver

class StartSession:
    def __init__(self, url, browser):
        self.url = url
        self.browser = browser

    def set_window_size(self, width, height):
        self.browser.set_window_size(width, height)

    def get_session(self):
        # Start a new browser window and jump to xpool login page
        self.set_window_size(1920, 1080)
        self.browser.get(self.url)

    def set_cookies(self):
        # Set the cookies
        cookies = pickle.load(open("./cookies/cookies.pkl", "rb"))
        for cookie in cookies:
            self.browser.add_cookie(cookie)

        # Refresh the browser window for the cookies to take effect
        self.browser.refresh()

    def execute_start_session(self):
        self.get_session()
        self.set_cookies()
