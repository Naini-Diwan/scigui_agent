import pyautogui

class GUIController:
    def click(self, bbox):
        x = (bbox[0] + bbox[2]) // 2
        y = (bbox[1] + bbox[3]) // 2
        pyautogui.moveTo(x, y)
        pyautogui.click()
