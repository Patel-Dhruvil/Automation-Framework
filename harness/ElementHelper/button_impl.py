from appium.webdriver.common.touch_action import TouchAction
from harness.ElementHelper.master_element_impl import ElementImpl


class ButtonImpl(ElementImpl):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def long_press_on_element(self, locatorValue, locatorType):
        element = None
        try:
            element = self.get_element(locatorValue, locatorType)
            actions = TouchAction(self.driver)
            actions.long_press(element)
            actions.perform()
            self.log.info(
                "longPrass on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)
            return True
        except:
            self.log.info(
                "Unable to longPress on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)
            assert False

    def click_and_hold_element(self):
        pass

    def tab_and_hold_element(self):
        pass

    def release_the_element(self):
        pass