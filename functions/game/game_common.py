from setting import setting
from setting.setting import ImageNames
import pyautogui
import datetime


def open_window():
    image_names = ImageNames()
    position = pyautogui.locateCenterOnScreen(setting.IMAGES_PATH + image_names.game_logo_file_name)
    pyautogui.moveTo(position)
    pyautogui.click()
