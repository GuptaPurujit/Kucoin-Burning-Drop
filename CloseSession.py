from BuildSession import BuildSession

class CloseSession:
    def __init__(self, browser, end):
        self.browser = browser
        self.end = end

    def quit_session(self):
        self.browser.quit()

    def close_session(self):
        self.browser.close()

    def end_session(self):
        if self.end:
            self.quit_session()
        else:
            self.close_session()
