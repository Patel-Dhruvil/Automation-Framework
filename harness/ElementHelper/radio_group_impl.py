from harness.ElementHelper.master_element_impl import ElementImpl


class RadioGroupImpl(ElementImpl):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # def IsSelected(self, locatorValue, locatorType):
    #     element = None
    #     try:
    #         element = self.get_element(locatorValue, locatorType)
    #         isSel = element.is_selected()
    #         print(isSel)
    #         self.log.info(
    #             "Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue + "is selected")
    #         return isSel
    #     except:
    #         self.log.info(
    #             "Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue + "is not selected")
    #         assert False

    def select_using_visible_text(self):
        pass

    def select_using_index_value(self):
        pass