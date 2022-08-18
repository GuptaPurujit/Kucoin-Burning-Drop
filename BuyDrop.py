from FetchCookies import FetchCookies
from LaunchDrop import LaunchDrop
from StartSession import StartSession
from CloseSession import CloseSession
from BuildSession import BuildSession
import Constants

class BuyDrop:
    def __init__(self):
        self.browser = BuildSession().get_browser()
        self.url = Constants.LOGIN_URL
        self.xdrop_url = Constants.XDROP_URL

    def execute_buy_drop(self):
        # Get Cookies after Manual Login
        if Constants.FETCH_COOKIES == "Y":
            fetch_cookies = FetchCookies(self.url, self.browser)
            fetch_cookies.execute_fetch_cookies()
            # CloseSession(self.browser, False).end_session()

        # Start Session using Cookies to bypass captcha
        if Constants.START_SESSION == "Y" and Constants.FETCH_COOKIES != "Y":
            start_session = StartSession(self.url, self.browser)
            start_session.execute_start_session()
            # # Close session after use
            # CloseSession(browser, False).end_session()

        # Jump to X-Drop page
        drop_name = "KCS-FOR-FCD-20D" # command line argument
        launch_drop = LaunchDrop(self.xdrop_url, self.browser, drop_name)
        launch_drop.get_session()
        launch_drop.navigate_to_drop()
        form_filled = launch_drop.fill_form('200', '002415') # command line arguments

        if form_filled:
            launch_drop.start_clicker()

if __name__ == "__main__":
    buy_drop = BuyDrop()
    buy_drop.execute_buy_drop()
