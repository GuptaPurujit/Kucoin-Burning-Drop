import time
import threading
import Constants
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
from MoveCursor import MoveCursor

start_stop_key = KeyCode(char=Constants.START_STOP_KEY)
exit_key = KeyCode(char=Constants.EXIT_KEY)

class AutoClicker(threading.Thread):
    def __init__(self, browser):
        super(AutoClicker, self).__init__()
        self.delay = Constants.DELAY
        self.button = Button.left
        self.running = False
        self.program_running = True
        self.mouse = Controller()
        self.browser = browser
        self.path = Constants.ENTER_BUTTON
        self.temp_ele = WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable((By.XPATH, self.path)))
        self.script = """
        console.clear();
        var data = arguments[0].getBoundingClientRect();
        var ret = new Array();
        ret.push(data.x);
        ret.push(data.y);
        ret.push(data.width);
        ret.push(data.height);
        return ret;
        """
        self.coordinates = self.browser.execute_script(self.script, self.temp_ele)
        self.ele = WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable((By.XPATH, self.path)))
        self.move_cursor = MoveCursor(self.browser, self.coordinates)

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                # self.mouse.click(self.button)
                self.move_cursor.click_on_coordinates(self.ele)
                time.sleep(self.delay)
            time.sleep(0.1)

class RunClicker:
    def __init__(self, browser):
        self.browser = browser
        self.click_thread = AutoClicker(self.browser)
        self.Listener = None

    def on_press(self, key):
        if key == start_stop_key:
            if self.click_thread.running:
                self.click_thread.stop_clicking()
            else:
                self.click_thread.start_clicking()
        elif key == exit_key:
            self.click_thread.exit()
            self.listener.stop()

    def run_clicker(self):
        self.click_thread.start()
        self.run_listener()

    def run_listener(self):
        self.listener = Listener(on_press=self.on_press)
        with self.listener as listener:
            listener.join()
