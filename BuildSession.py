from selenium import webdriver
import Constants

class BuildSession:
    def __init__(self):
        self.browser = None

    def build_session(self):
        self.browser = webdriver.Chrome(executable_path=Constants.EXECUTABLE_PATH)

    def get_browser(self):
        self.build_session()
        return self.browser
