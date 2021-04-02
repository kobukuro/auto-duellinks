from setting import setting
from setting.setting import CommonImageNames
import pyautogui
from datetime import datetime

image_names = CommonImageNames()


def click_image(file_path):
    time_start = datetime.now()
    while True:
        time_now = datetime.now()
        delta = time_now - time_start
        delta_seconds = delta.total_seconds()
        if delta_seconds > 10:
            raise Exception(f'超過時間尚未找到{file_path}')
        else:
            position = pyautogui.locateCenterOnScreen(
                file_path)
            if position is not None:
                pyautogui.moveTo(position)
                pyautogui.click()
                break


def click_start_game():
    click_image(file_path=image_names.start_game_file_path)

def click_ok_btn():
    click_image(file_path=image_names.ok_btn_file_path)

def click_next_one_btn():
    click_image(file_path=image_names.next_one_btn_file_path)

def click_message_close_btn():
    click_image(file_path=image_names.message_close_file_path)

def click_card_flipper_close_btn():
    click_image(file_path=image_names.card_flipper_close_brn_file_path)

def open_window():
    logo_position = pyautogui.locateCenterOnScreen(image_names.game_logo_file_path)
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
            window_title_position = pyautogui.locateCenterOnScreen(image_names.window_title_file_path)
            if window_title_position is not None:
                break


def close_message_windows():
    time_start = datetime.now()
    while True:
        time_now = datetime.now()
        delta = time_now - time_start
        delta_seconds = delta.total_seconds()
        if delta_seconds > 2:
            break
        message_window_close_position = pyautogui.locateCenterOnScreen(image_names.message_close_file_path)
        if message_window_close_position is not None:
            pyautogui.moveTo(message_window_close_position)
            pyautogui.click()


def choose_character():
    click_image(file_path=image_names.outer_deck_image_file_path)
    click_image(file_path=image_names.inner_deck_circle_file_path)
