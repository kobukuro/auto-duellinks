from setting import setting
from setting.setting import ImageNames
import pyautogui

if __name__ == '__main__':
    image_names = ImageNames()
    position = pyautogui.locateCenterOnScreen(setting.IMAGES_PATH+image_names.game_logo_file_name)
    pyautogui.moveTo(position)
    pyautogui.click()
    # while True:
    #     window_title_position = pyautogui.locateCenterOnScreen('images\\duellinks_logo.png')
    # while True:
    #     start = pyautogui.locateCenterOnScreen('images\\message_close.png')
    #     if start != None:
    #         pyautogui.moveTo(start)
    #         break