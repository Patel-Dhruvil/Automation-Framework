from harness.ElementHelper.master_element_impl import ElementImpl


class TextBoxImpl(ElementImpl):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    def send_input_value(self, text, locatorValue, locatorType):
        element = None

        try:
            element = self.get_element(locatorValue, locatorType)
            element.send_keys(text)
            self.log.info(
                "Send text  on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)
        except:
            self.log.info(
                "Unable to send text on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)

            assert False

    def clear_the_text_field(self, locatorValue, locatorType):
        element = None
        try:
            element = self.get_element(locatorValue, locatorType)
            element.clear()
            self.log.info(
                "Element cleared with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)

        except:
            self.log.info(
                "Unable to send text on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)
            assert False

    def long_press_key(self, value):
        try:
            self.driver.long_press_keycode(value)
            self.log.info("LongPress_KeyCode")
        except:
            self.log.info("LongPress_KeyCode not found")
            assert False

    def hide_key_board(self):
        try:
            self.driver.hide_keyboard()
            self.log.info("HideKeyBoard")
        except:
            self.log.info("HideKeyBoard not found")
            assert False

    def is_keyboard_visible(self):
        try:
            self.driver.is_keyboard_shown()
            self.log.info("Keyboard found")
        except:
            self.log.info("Keyboard_Shown not found")
            assert False