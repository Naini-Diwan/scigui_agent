import pyautogui
from appium import webdriver as appium_driver
from selenium import webdriver as selenium_driver

class GUIController:
    def __init__(self, mode="desktop"):
        self.mode = mode
        self.appium = None
        self.selenium = None

    def click(self, bbox):
        if self.mode == "desktop":
            x = (bbox[0] + bbox[2]) // 2
            y = (bbox[1] + bbox[3]) // 2
            pyautogui.moveTo(x, y)
            pyautogui.click()
        elif self.mode == "mobile":
            if not self.appium:
                self.appium = appium_driver.Remote('http://localhost:4723/wd/hub', desired_capabilities={})
            # Example: self.appium.tap([(x, y)])
        elif self.mode == "web":
            if not self.selenium:
                self.selenium = selenium_driver.Chrome()
            # Example: self.selenium.find_element_by_xpath(...).click()
