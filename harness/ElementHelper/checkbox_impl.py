from harness.ElementHelper.master_element_impl import ElementImpl


class CheckboxImpl(ElementImpl):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def check_mark_the_check_box(self):

        # chkBx = driver.findElements(By.className(“android.widget.CheckBox”));
        # a = chkBx.get(0).getAttribute(“checked”);
        # It will return true or false as String.
        pass

    def uncheck_the_check_box(self):
        pass

    def select_using_visible_text(self):
        pass

    def select_using_index_value(self):
        pass