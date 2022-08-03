import unittest
import pytest
import harness.Utilities.CustomLogger as cl
from harness.ElementHelper.master_element_impl import ElementImpl
from apptest.PageObject.LoginPage import LoginPageTest
from harness.ElementHelper.text_impl import TextBoxImpl


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.el = ElementImpl(self.driver)
        self.gt = LoginPageTest(self.driver)
        self.tb = TextBoxImpl(self.driver)

    @pytest.mark.run(order=5)
    def test_enterDataInEditBox(self):
        self.gt.enterText()
        self.gt.clickOnSubmit()

    @pytest.mark.run(order=4)
    def test_openLoginScreen(self):
        #self.bp.keyCode(4)
        self.gt.clickLoginBotton()
        self.gt.enterEmail()
        self.gt.Get_Text()
        self.gt.Tag_Name()
        self.gt.enterPassword()
        self.gt.clickOnLoginB()

    @pytest.mark.run(order=3)
    def test_loginFailMethod(self):
        cl.allureLogs("App Opened")
        self.gt.clickLoginBotton()
        self.gt.enterEmail()
        self.gt.enterPassword2()
        self.gt.clickOnLoginB()






