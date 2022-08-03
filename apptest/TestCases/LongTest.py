import time
import unittest
import pytest
from harness.ElementHelper.master_element_impl import ElementImpl
from apptest.PageObject.ContactUsFormPage import ContactForm
import harness.Utilities.CustomLogger as cl
#import tests.LoginTest
from apptest.PageObject.tap_page import Long
from apptest.PageObject.testDemo import testdemo



@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class ContactFormTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.l = Long(self.driver)
        self.bp = ElementImpl(self.driver)
        self.td = testdemo(self.driver)

    @pytest.mark.run(order=2)
    def test_opencontactForm(self):
        cl.allureLogs("App Launched")
        self.l.clickLongButton()

    @pytest.mark.run(order=1)
    def test_Demo(self):
        cl.allureLogs("App Launched")
        self.td.getContexts()

    @pytest.mark.run(order=2)
    def test_Demo1(self):
        cl.allureLogs("App Launched")
        self.td.getAllContexts()

    def test_swipe_left(self):
        self.td.Swipe_left_test()

    def test_swipe_Right(self):
        self.td.Swipe_right_test()

    def test_swipe_Top(self):
        self.td.Swipe_Top_test()

    def test_swipe_Bottom(self):
        self.td.Swipe_Bottom_test()

    def test_long_press(self):
        time.sleep(2)
        self.td.Long_press()

    def test_Two_finger(self):
        time.sleep(2)
        self.td.twoFinger()

    # @pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)])
    # def test_print(self, test_input, expected):
    #     print(test_input, expected)
    #
    # @pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)])
    # def test_eval(self,test_input, expected):
    #     assert eval(test_input) == expected


