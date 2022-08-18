import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

class MoveCursor:
    def __init__(self, browser, coordinates):
        self.browser = browser
        self.x = coordinates[0]
        self.y = coordinates[1]
        self.w = coordinates[2]
        self.h = coordinates[3]
        self.actions = ActionChains(self.browser)

    def click_on_coordinates(self, ele):
        w = int(self.w)
        h = int(self.h)
        self.actions.move_to_element_with_offset(ele, w/2, h/2)
        self.actions.click()
        self.actions.perform()

    def enter_value_on_coordinates(self, key):
        self.actions.send_keys(key)
        self.actions.perform()
