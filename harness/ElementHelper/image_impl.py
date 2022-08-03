from harness.ElementHelper.master_element_impl import ElementImpl


class ImageImpl(ElementImpl):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def long_press_on_element(self, locatorValue, locatorType):
        pass

    def click_and_hold_element(self):
        pass

    def tab_and_hold_element(self):
        pass

    def release_the_element(self):
        pass