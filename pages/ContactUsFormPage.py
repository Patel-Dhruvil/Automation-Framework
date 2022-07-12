from base.BasePage import BasePage
import utilities.CustomLogger as cl

class ContactForm(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators values in Contact us form
    _contactFromButton = "com.code2lead.kwad:id/ContactUs"  # id
    _pagetitle = "Contact Us form"  # text
    _enterName = "Enter Name"  # text
    _enterEmail = "Enter Email"  # text
    _enterAddress = "Enter Address"  # text
    _enterMobileNumber = "4"  # index number
    _submitButton = "SUBMIT"  # text

    def clickContactFormButton(self):
        self.clickElement(self._contactFromButton, "id")
        cl.allureLogs("Click Contact Form")
    def key(self):
        self.a=int(input("enter code"))
        self.keyCode(self.a)
    def verifyContactPage(self):
        element = self.Attributes1(6,self._pagetitle, "text")
        cl.allureLogs("Click verify contact form")
        assert element == True
        print("maulik")

    def enterName(self):
        self.sendText("Ralpasoft",self._enterName,"text")
        cl.allureLogs("Click Enter Name")

    def enterEmail(self):
        self.sendText("maulikpatel@gmail.com",self._enterEmail,"text")
        cl.allureLogs("Click Enter Email ID")

    def enterAddress(self):
        self.sendText("India",self._enterAddress,"text")
        cl.allureLogs("Click Enter Address")

    def enterMNumber(self):
        self.sendText("9998144896",self._enterMobileNumber,"index")
        cl.allureLogs("Click enter Number")

    def clickSubmitButton(self):
        self.clickElement(self._submitButton,"text")
        cl.allureLogs("Click Submit Button")

    def Press_Key_Code(self):
        value = int(input("Enter the key value"))
        self.Press_keyCode(value)

    def Long_Press_Keycode(self):
        value = int(input("Enter the key value"))
        self.LongPress_KeyCode(value)



