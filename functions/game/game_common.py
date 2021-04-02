from setting import setting
from setting.setting import ImageNames
import pyautogui
from datetime import datetime

image_names = ImageNames()


def open_window():
    print('open_window start')
    logo_position = pyautogui.locateCenterOnScreen(setting.IMAGES_PATH + image_names.game_logo_file_name)
    pyautogui.moveTo(logo_position)
    pyautogui.click()
    time_start = datetime.now()
    while True:
        time_now = datetime.now()
        delta = time_now - time_start
        delta_seconds = delta.total_seconds()
        if delta_seconds > setting.WAIT_SECONDS_LIMIT:
            raise Exception('超過時間尚未打開遊戲視窗')
        else:
            window_title_position = pyautogui.locateCenterOnScreen(
                setting.IMAGES_PATH + image_names.window_title_file_name)
            if window_title_position is not None:
                break
    print('open_window end')


def close_message_windows():
    time_start = datetime.now()
    while True:
        time_now = datetime.now()
        delta = time_now - time_start
        delta_seconds = delta.total_seconds()
        if delta_seconds > 10:
            break
        message_window_close_position = pyautogui.locateCenterOnScreen(
            setting.IMAGES_PATH + image_names.message_close_file_name)
        if message_window_close_position is not None:
            pyautogui.moveTo(message_window_close_position)
            pyautogui.click()
