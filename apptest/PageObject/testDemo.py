import time
import pytest
from harness.ElementHelper.master_element_impl import ElementImpl


class testdemo(ElementImpl):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _tabViewButton = "TAB ACTIVITY"  #text
    _ScrollViewButton = "ScrollView" #text
    _longpress = "LONG CLICK"  #text



    @pytest.fixture(autouse=True)
    def classObjects(self):
        bp = ElementImpl(self.driver)

    def getContexts(self):
        self.getcontexts()
        print("\n-------------------------------")
        print(self.getcontexts())
        print("-----------------------------------")

    def getAllContexts(self):
        self.getallcontexts()
        print("\n-------------------------------")
        print(self.getallcontexts())
        print("-----------------------------------")

    def Swipe_left_test(self):
        deviceSize = self.driver.get_window_size()
        screenWidth,screenHeight = None,None
        screenWidth = deviceSize['width']
        screenHeight = deviceSize['height']

        startx = screenWidth * 8 / 9
        endx = screenWidth / 9
        starty = screenHeight / 2
        endy = screenHeight / 2
        self.click_on_element(self._tabViewButton, "text")
        time.sleep(2)
        self.Move(None, None, startx, endx, starty, endy)

    def Swipe_right_test(self):
        deviceSize = self.driver.get_window_size()
        screenWidth = deviceSize['width']
        screenHeight = deviceSize['height']
        startx = screenWidth / 9
        endx = screenWidth * 8 / 9
        starty = screenHeight / 2
        endy = screenHeight / 2
        self.clickElement(self._tabViewButton, "text")
        time.sleep(2)
        self.Move(None, None, startx, endx, starty, endy)

    def Swipe_Top_test(self):
        deviceSize = self.driver.get_window_size()
        screenWidth = deviceSize['width']
        screenHeight = deviceSize['height']
        startx = screenWidth / 2
        endx = screenWidth / 2
        starty = screenHeight * 8 / 9
        endy = screenHeight / 9
        self.clickElement(self._ScrollViewButton, "text")
        time.sleep(2)
        self.Move(None, None, startx, endx, starty, endy)

    def Swipe_Bottom_test(self):
        deviceSize = self.driver.get_window_size()
        screenWidth = deviceSize['width']
        screenHeight = deviceSize['height']
        startx = screenWidth / 2
        endx = screenWidth / 2
        starty = screenHeight * 2 / 9
        endy = screenHeight * 8 / 9
        self.clickElement(self._ScrollViewButton, "text")
        time.sleep(2)
        self.Move(None, None, startx, endx, starty, endy)

    def Long_press(self):
        self.longpress(self._longpress,"text")

    def twoFinger(self):
        deviceSize = self.driver.get_window_size()
        screenWidth = deviceSize['width']
        screenHeight = deviceSize['height']
        startx = screenWidth / 2
        endx = screenWidth / 2
        starty = screenHeight * 2 / 9
        endy = screenHeight * 8 / 9
        self.twofingerswipe(startx, endx, starty, endy)


