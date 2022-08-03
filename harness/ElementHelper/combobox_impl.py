from harness.ElementHelper.master_element_impl import ElementImpl


class ComboBoxImpl(ElementImpl):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def select_using_visible_text(self):
        pass

    def select_using_index_value(self):
        pass

    def send_input_value(self):
        pass

    def clear_the_text_field(self):
        pass

    def long_press_key(self, value):
        pass

    def hide_key_board(self):
        pass

    def is_keyboard_visible(self):
        pass
