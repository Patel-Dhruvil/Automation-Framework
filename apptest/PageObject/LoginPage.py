import pytest
import harness.Utilities.CustomLogger as cl
from harness.ElementHelper.master_element_impl import ElementImpl
from harness.ElementHelper.text_impl import TextBoxImpl


class LoginPageTest(TextBoxImpl):

    def __init__(self, driver):
        super().__init__(driver)

    # Locators values in Contact us form
    _loginbutton ="com.code2lead.kwad:id/Login" # id
    _enterEmail ="com.code2lead.kwad:id/Et4" # id
    _enterPassword ="Enter Password" # text
    _clickloginButton ="com.code2lead.kwad:id/Btn3" # id
    _wrongCredentials = "Wrong Credentials" # text
    _pageTitle ="Enter Admin" # text
    _enterText ="com.code2lead.kwad:id/Et4" # text
    _submitButton ="com.code2lead.kwad:id/Btn_admin_sub" # id

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.gt = LoginPageTest(self.driver)
        self.el = ElementImpl(self.driver)
        self.tb = TextBoxImpl(self.driver)

    def clickLoginBotton(self):
        self.click_on_element(self._loginbutton, "id")
        cl.allureLogs("Click on Login Button")

    def enterEmail(self):
        self.send_input_value("admin@gmail.com", self._enterEmail, "id")
        #self.sendText(self.getTestData("validTest")["email"], self._enterEmail,"id")
        cl.allureLogs("Entered email id")

    def enterPassword(self):
        self.send_input_value("admin123", self._enterPassword, "text")
        cl.allureLogs("Entered Password")

    def enterPassword2(self):
        self.send_input_value("dhruvil@1234", self._enterPassword, "text")
        cl.allureLogs("Entered Password")

    def clickOnLoginB(self):
        self.click_on_element(self._clickloginButton, "id")
        cl.allureLogs("Clicked on Login Button in Login Screen")

    def verifyAdminScreen(self):
        adminScreen = self.isDisplayed(self._pageTitle,"text")
        assert adminScreen == True
        cl.allureLogs("Opened Admin Screen")

    def enterText(self):
        self.send_input_value("Code2Lead", self._enterText, "id")
        cl.allureLogs("Entered Text")

    def clickOnSubmit(self):
        self.click_on_element(self._submitButton, "id")
        cl.allureLogs("Clicked on Submit Button")

    def Get_Text(self):
        self.get_element_text(self._enterEmail, "id")
        print(self.get_element_text(self._enterEmail, "id"))

    def Tag_Name(self):
        self.get_tag_name(self._clickloginButton, "id")
        print(self.get_tag_name(self._clickloginButton, "id"))

    def Is_Displayed(self):
        self.is_element_visible(self._loginbutton, "id")

    def Is_Enabled(self):
        self.is_element_enable(self._enterEmail, "id")
