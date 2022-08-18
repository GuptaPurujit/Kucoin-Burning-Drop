import pickle
import time
from selenium import webdriver

class FetchCookies:
    def __init__(self, url, browser):
        self.url = url
        self.browser = browser

    def set_window_size(self, width, height):
        self.browser.set_window_size(width, height)

    def get_session(self):
        # Start a new browser window and jump to xpool login page
        self.set_window_size(1920, 1080)
        self.browser.get(self.url)

    def download_cookies(self):
        # Dump all the cookies after login to a pkl file
        pickle.dump(self.browser.get_cookies() , open("./cookies/cookies.pkl","wb"))

    def execute_fetch_cookies(self):
        self.get_session()

        """
        This sleep timer is required so that the user can manually add the login
        credentails and login once. This step has to be repeated every 7 days
        """
        time.sleep(60)

        self.download_cookies()
