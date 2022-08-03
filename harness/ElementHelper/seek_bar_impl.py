from harness.ElementHelper.master_element_impl import ElementImpl


class SeekBarImpl(ElementImpl):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver