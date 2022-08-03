from harness.ElementHelper.master_element_impl import ElementImpl


class DatePickerImpl(ElementImpl):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def send_input_value(self):
        pass

    def clear_the_text_field(self):
        pass