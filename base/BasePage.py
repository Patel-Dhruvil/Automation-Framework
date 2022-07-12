import allure
import appium
from allure_commons.types import AttachmentType
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
import utilities.CustomLogger as cl
import time

from base.DriversDefine import appium_element_locator_dict, Attribute_dic


class BasePage:
    log = cl.customLogger()

    def __init__(self, driver):
        self.driver = driver

    def waitForElement(self, locatorvalue, locatorType):
        locatorType = locatorType.lower()
        element = None

        wait = WebDriverWait(self.driver, 25, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                                 NoSuchElementException])

        list1 = ["id", "xpath", "CLASS_NAME"]
        if locatorType in list1:
            element = wait.until(lambda x: x.find_element(appium_element_locator_dict[locatorType], locatorvalue))
            print(appium_element_locator_dict[locatorType])
            return element
        else:
            element = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'text("%s")' % locatorvalue))
            return element

    def ForElement(self, locatorvalue, locatorType):
        locatorType = locatorType.lower()
        element = None

        wait = WebDriverWait(self.driver, 25, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                                 NoSuchElementException])

        ele = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                  Attribute_dic[7] % locatorvalue))
        # ele = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
        #                                           'new UiScrollable(new UiSelector()).scrollIntoView(text("LOGIN"))'))
        return ele

    def getElement(self, locatorValue, locatorType):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
            self.log.info("Element found with LocatorType: " + locatorType + " with the locatorValue :" + locatorValue)
        except:
            self.log.info(
                "Element not found with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)
            self.takeScreenshot(locatorType)
            assert False
        return element

    def clickElement(self, locatorValue, locatorType):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.getElement(locatorValue, locatorType)
            element.click()
            self.log.info(
                "Clicked on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)
        except:
            self.log.info(
                "Unable to click on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)
            self.takeScreenshot(locatorType)
            assert False

    def touch(self, locatorValue, x, z, count, text):
        element = None
        actions = TouchAction(self.driver)
        actions1 = ActionChains(self.driver)

        try:
            element = self.ForElement(locatorValue, locatorType="text")
            Touch_Actions = {
                "long": actions.long_press(element, x, z, count),
                "tap": actions.tap(element, x, z, count),
                "double_tap": actions1.double_click(element)

            }

            Touch_Actions[text]
            print(Touch_Actions[text])
            actions.perform()
            print("done ")
        except:
            assert False

    def sendText(self, text, locatorValue, locatorType):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.getElement(locatorValue, locatorType)
            element.send_keys(text)
            self.log.info(
                "Send text  on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)
        except:
            self.log.info(
                "Unable to send text on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)
            self.takeScreenshot(locatorType)
            return False

    def Attributes1(self, text, locatorValue, locatorType):
        element = None
        operation = Attribute_dic[text]
        try:
            locatorType = locatorType.lower()
            element = self.getElement(locatorValue, locatorType)
            operation
            print("maulik")
            # element.is_displayed()
            self.log.info(
                " Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue + "is displayed ")
            return True
        except:
            self.log.info(
                " Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue + " is not displayed")
            self.takeScreenshot(locatorType)
            return False

#code for implementing key codes on the pages(keyboard)

    def Press_keyCode(self, value):
        self.driver.press_keycode(value)

    def LongPress_KeyCode(self, value):
        self.driver.long_press_keycode(value)




    def screenShot(self, screenshotName):
        fileName = screenshotName + "_" + (time.strftime("%d_%m_%y_%H_%M_%S")) + ".png"
        screenshotDirectory = "../screenshots/"
        screenshotPath = screenshotDirectory + fileName
        try:
            self.driver.save_screenshot(screenshotPath)
            self.log.info("Screenshot save to Path : " + screenshotPath)

        except:
            self.log.info("Unable to save Screenshot to the Path : " + screenshotPath)

    def takeScreenshot(self, text):
        allure.attach(self.driver.get_screenshot_as_png(), name=text, attachment_type=AttachmentType.PNG)




        # if locatorType == "id":
        #     element = wait.until(lambda x: x.find_element(AppiumBy.ID, locatorvalue))
        #     return element
        # elif locatorType == "class":
        #     element = wait.until(lambda x: x.find_element(AppiumBy.CLASS_NAME, locatorvalue))
        #     return element
        # elif locatorType == "des":
        #     element = wait.until(
        #         lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
        #                                  'UiSelector().description("%s")' % (locatorvalue)))
        #     return element
        # elif locatorType == "index":
        #     element = wait.until(
        #         lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "UiSelector().index(%d)" % int(locatorvalue)))
        #     return element
        # elif locatorType == "text":
        #     element = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'text("%s")' % locatorvalue))
        #     return element
        # elif locatorType == "xpath":
        #     element = wait.until(lambda x: x.find_element(AppiumBy.XPATH, '%s' % (locatorvalue)))
        #     return element
        # else:
        #     self.log.info("Locator value " + locatorvalue + "not found")

# ---------------------------------------- New implementation by Dhruvil ----------------------

    def getcontexts(self):
        try:
            context = self.driver.current_context
            self.log.info(" This is All the Contexts: " + context)
            return context
        except:
            #self.log.info("Unable to get the Contexts")
            self.log.warning("Unable to get the Contexts")
            assert False

    def getallcontexts(self):
        try:
            contexts = self.driver.contexts
            self.log.info(" This is All the Contexts: " + contexts)
            return contexts
        except:
            self.log.warning("Unable to get the All Contexts")
            assert False
