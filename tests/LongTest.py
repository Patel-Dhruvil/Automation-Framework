import unittest
import pytest
from base.BasePage import BasePage
from pages.ContactUsFormPage import ContactForm
import utilities.CustomLogger as cl
import tests.LoginTest
from pages.tap_page import Long


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class ContactFormTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.l = Long(self.driver)
        self.bp = BasePage(self.driver)


    @pytest.mark.run(order=1)
    def test_opencontactForm(self):
        cl.allureLogs("App Launched")
        self.l.clickLongButton()


