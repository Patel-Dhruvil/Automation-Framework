from appium.webdriver.common.appiumby import AppiumBy
#from ElementProperties.Properties import element

appium_element_locator_dict = {
    "id": AppiumBy.ID,
    "xpath": AppiumBy.XPATH,
    "class":AppiumBy.CLASS_NAME,
    "index" : AppiumBy.ANDROID_UIAUTOMATOR

}

Attribute_dic = {
    # 2:element.is_displayed(),
    # 1:element.is_enabled(),
    # 3:element.is_selected(),
    # 4:element.tag_name,
    # 5:element.get_attribute,
    # 6:element.text,
    7:'new UiScrollable(new UiSelector()).scrollIntoView(text("%s"))',
}
