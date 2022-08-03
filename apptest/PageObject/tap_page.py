from harness.Base.BasePage import BasePage
import harness.Utilities.CustomLogger as cl

class Long(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators values in Contact us form
    _LongButton = "LONG CLICK"  # text


    def clickLongButton(self):
        self.touch(self._LongButton,None, None, None,"double_tap")
        cl.allureLogs("Click Contact Form")

