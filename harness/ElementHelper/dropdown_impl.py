from harness.ElementHelper.master_element_impl import ElementImpl


class DropDownImpl(ElementImpl):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def select_using_visible_text(self):
        pass

    def select_using_index_value(self):
        pass