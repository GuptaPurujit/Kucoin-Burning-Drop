import time
import Constants
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from BuildSession import BuildSession
from StartSession import StartSession
from MoveCursor import MoveCursor
from AutoClicker import RunClicker


class LaunchDrop:
    def __init__(self, url, browser, drop_name):
        self.url = url
        self.browser = browser
        self.drop_name = drop_name
        self.amt_path = Constants.AMOUNT_PATH
        self.pass_path = Constants.PASSWORD_PATH

    def get_session(self):
        # Start a new browser window and jump to xpool login page
        self.browser.get(self.url)

    def navigate_to_drop(self):
        # select the desired burning drop
        time.sleep(5)
        path = "//*[contains(text(), {drop_name})]".format(drop_name=self.drop_name)
        WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable((By.XPATH, path))).click()

    def get_element_coordinates(self, path):
        ele = WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable((By.XPATH, path)))
        script = """
        console.clear();
        var data = arguments[0].getBoundingClientRect();
        var ret = new Array();
        ret.push(data.x);
        ret.push(data.y);
        ret.push(data.width);
        ret.push(data.height);
        return ret;
        """
        coordinates = self.browser.execute_script(script, ele)
        return coordinates

    def set_value(self, path, value):
        coordinates = self.get_element_coordinates(path)
        ele = WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable((By.XPATH, path)))
        move_cursor = MoveCursor(self.browser, coordinates)
        move_cursor.click_on_coordinates(ele)
        move_cursor.enter_value_on_coordinates(value)

    def fill_form(self, amount, trading_password):
        # time.sleep(2)
        # enter_btn = "/html/body/div[1]/div/div[2]/div/div[5]/div/div[3]/form/div[6]/div/div/span"
        # press_enter = WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable((By.XPATH, enter_btn)))
        time.sleep(2)
        self.browser.execute_script("window.scrollBy(0,800)", "")
        time.sleep(2)
        self.set_value(self.amt_path, int(amount))
        self.set_value(self.pass_path, str(trading_password))
        return True

    def start_clicker(self):
        path = Constants.ENTER_BUTTON
        ele = WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable((By.XPATH, path)))
        RunClicker(self.browser).run_clicker()
