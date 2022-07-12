import unittest
import pytest
from base.BasePage import BasePage
from pages.ContactUsFormPage import ContactForm
import utilities.CustomLogger as cl
import tests.LoginTest


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class ContactFormTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.cf = ContactForm(self.driver)
        self.bp = BasePage(self.driver)


    @pytest.mark.run(order=1)
    def test_opencontactForm(self):
        cl.allureLogs("App Launched")
        self.cf.clickContactFormButton()
        # self.cf.key()
        self.cf.verifyContactPage()

    @pytest.mark.run(order=2)
    def test_enterDataInForm(self):
        me()
        self.cf.enterEmail()
        self.cf.enterAddress()
        self.cf.enterMNumber()
        self.cf.clickSubmitButton()
        self.cf.keyCode(4)












