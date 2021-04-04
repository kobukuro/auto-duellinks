from setting import setting
from setting.setting import CommonImageNames
import pyautogui
from datetime import datetime

image_names = CommonImageNames()


def is_exists_image(file_path, wait_seconds_limit=5):
    result = False
    time_start = datetime.now()
    while True:
        time_now = datetime.now()
        delta = time_now - time_start
        delta_seconds = delta.total_seconds()
        if delta_seconds > wait_seconds_limit:
            break
        else:
            position = pyautogui.locateCenterOnScreen(
                file_path)
            if position is not None:
                result = True
                break
    return result


def click():
    pyautogui.click()


def move_mouse(x, y):
    pyautogui.moveTo(x, y)


def click_image(file_path, wait_seconds_limit=60):
    time_start = datetime.now()
    while True:
        time_now = datetime.now()
        delta = time_now - time_start
        delta_seconds = delta.total_seconds()
        if delta_seconds > wait_seconds_limit:
            raise Exception(f'超過時間尚未找到{file_path}')
        else:  # pyautogui.locateOnScreen('Dark.png', confidence=0.9)
            position = pyautogui.locateCenterOnScreen(
                file_path)
            if position is not None:
                pyautogui.moveTo(position)
                pyautogui.click()
                break


def wait_until_duel_orb_show():
    is_exists_image(file_path=image_names.duel_orb_file_path, wait_seconds_limit=30)


def click_gate(initial=False):
    if initial:
        click_image(file_path=image_names.initial_gate_file_path)
    else:
        click_image(file_path=image_names.gate_file_path)


def click_duel_btn():
    click_image(file_path=image_names.duel_btn_file_path)


def skip_dialog():
    time_start = datetime.now()
    while True:
        time_now = datetime.now()
        delta = time_now - time_start
        delta_seconds = delta.total_seconds()
        if delta_seconds > 10:
            break
        else:
            position = pyautogui.locateCenterOnScreen(
                image_names.dialog_arrow_file_path)
            if position is not None:
                pyautogui.click()
                break


def click_inner_duel_btn():
    click_image(file_path=image_names.inner_duel_btn_file_path)


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


def close_duel_quest_windows(wait_seconds_limit=15):
    time_start = datetime.now()
    while True:
        time_now = datetime.now()
        delta = time_now - time_start
        delta_seconds = delta.total_seconds()
        if delta_seconds > wait_seconds_limit:
            break
        message_window_close_position = pyautogui.locateCenterOnScreen(image_names.ok_btn_file_path)
        # print(f'close_duel_quest_windows {message_window_close_position}')
        if message_window_close_position is not None:
            pyautogui.moveTo(message_window_close_position)
            pyautogui.click()


def close_message_windows(wait_seconds_limit=15):
    time_start = datetime.now()
    while True:
        time_now = datetime.now()
        delta = time_now - time_start
        delta_seconds = delta.total_seconds()
        if delta_seconds > wait_seconds_limit:
            break
        message_window_close_position = pyautogui.locateCenterOnScreen(image_names.message_close_file_path)
        # print(f'close_message_windows {message_window_close_position}')
        if message_window_close_position is not None:
            pyautogui.moveTo(message_window_close_position)
            pyautogui.click()


def choose_character():
    click_image(file_path=image_names.outer_deck_image_file_path)
    click_image(file_path=image_names.inner_deck_circle_file_path)
