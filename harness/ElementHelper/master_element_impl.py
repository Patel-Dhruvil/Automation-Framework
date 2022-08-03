"""
FILE: master_element_impl.py
List of Common Functions for handle the elements
Created Date:  01/08/2022
Created By: Dhruvil Patel & Apurva Sheth
Copy Rights: COPYRIGHT 2022 EINFOCHIPS LTD ALL RIGHTS RESERVED.
"""

from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
import harness.Utilities.CustomLogger as cl
from harness.Driver.DriversDefine import appium_element_locator_dict, Attribute_dic


class ElementImpl:

    """
    A class used to represent an Element Handler.

    ...

    Attributes
    ----------

    """

    log = cl.customLogger()

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locatorvalue, locatorType):

        """Return the element after finding it.

            Parameters
            ----------
            locatorvalue: str
                The locatorvalue is the value of the element locator
            locatorType: str
                The locatorType is the type of the element locator
            Raises
            ------
            ElementNotVisibleException:
                If Element is not visible, function will raises this exception.
            ElementNotSelectableException:
                If Element can not be select, function will raises this exception
            NoSuchElementException:
                If Element can not be found, function will raises this exception
            Returns
            -------
            Element: object
                It will return Element after finding it.
            """

        element = None
        if locatorType == None and locatorvalue == None:
            return element
        else:
            locatorType = locatorType.lower()

            wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                                 ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                                     NoSuchElementException])

            lst_locators = ["id", "xpath", "CLASS_NAME"]
            if locatorType in lst_locators:
                element = wait.until(lambda x: x.find_element(appium_element_locator_dict[locatorType], locatorvalue))
                return element

            else:
                element = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'text("%s")' % locatorvalue))
                return element

    def get_element(self, locatorValue, locatorType):#private  method
        element = None
        try:
            element = self.wait_for_element(locatorValue, locatorType)
            self.log.info("Element found with LocatorType: " + str(locatorType) + " with the locatorValue :" + str(locatorValue))
        except:
            self.log.info(
                "Element not found with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)
            assert False
        return element

    def click_on_element(self, locatorValue, locatorType):
        element = None
        try:
            element = self.get_element(locatorValue, locatorType)
            element.click()
            self.log.info(
                "Clicked on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)
        except:
            self.log.info(
                "Unable to click on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)
            assert False

    def double_click_on_element(self, locatorValue, locatorType):
        pass

    def get_tag_name(self, locatorValue, locatorType):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.get_element(locatorValue, locatorType)
            tagname = element.tag_name
            print(tagname)
            self.log.info(
                "TagName of Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)
            return tagname
        except:
            self.log.info(
                "Unable to take tagname of Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)
            assert False

    def is_element_visible(self, locatorValue, locatorType):
        element = None
        try:
            element = self.get_element(locatorValue, locatorType)
            isdis = element.is_displayed()
            print(isdis)
            self.log.info(
                "Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue + "is displayed")
            return isdis
        except:
            self.log.info(
                "Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue + "is not displayed")
            assert False

    def is_element_enable(self, locatorValue, locatorType):
        element = None
        try:
            element = self.get_element(locatorValue, locatorType)
            isenble = element.is_enabled()
            print(isenble)
            self.log.info(
                "Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue + "is enable")
            return isenble
        except:
            self.log.info(
                "Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue + "is not enable")
            assert False

    def find_element(self, locatorValue, locatorType):
        pass


    # def Move(self, locatorValueStart, locatorTypeStart, locatorValueEnd, locatorTypeEnd, startx, starty, endx, endy):
    #     try:
    #         elementStart = self.getElement(locatorValueStart, locatorTypeStart)
    #         elementEnd = self.getElement(locatorValueEnd, locatorTypeEnd)
    #
    #         actions = TouchAction(self.driver)
    #         actions.long_press(elementStart, startx, starty).move_to(elementEnd, endx, endy).release().perform()
    #         self.log.info(
    #             "moved Element with LocatorType: " + str(locatorTypeStart) + " and with the locatorValue :" + str(locatorValueStart))
    #     except:
    #         self.log.info(
    #             "Unable to move Element with LocatorType: " + str(locatorTypeStart) + " and with the locatorValue :" + str(locatorValueStart))
    #         assert False

    def get_attribute_value(self, locatorValue, locatorType):#need to make it dynamic
        element = None
        try:
            element = self.get_element(locatorValue, locatorType)
            attr = element.get_attribute('content-desc')
            print(attr)
            self.log.info(
                "Attribute of Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)
            return attr
        except:
            self.log.info(
                "Unable to take attribute of Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)
            assert False

    def get_element_text(self, locatorValue, locatorType):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.get_element(locatorValue, locatorType)
            fetched_text = element.text
            print(fetched_text)
            self.log.info(
                "Text  on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)
            return fetched_text
        except:
            self.log.info(
                "Unable to take text on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)
            assert False

    def get_element_specification(self):
        pass

    def get_size_of_element(self):
        pass

    def swipe_left(self):
        pass

    def swipe_right(self):
        pass

    def swipe_up(self):
        pass

    def swipe_down(self):
        pass

    def drag_and_drop_element(self):
        pass

    def double_tap_on_element(self):
        pass

    def tap_on_element(self):
        pass






