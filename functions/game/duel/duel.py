from setting.setting import DuelImagesNames
from functions.game import game_common
import time

image_names = DuelImagesNames()


def wait_until_my_main_phase():
    game_common.click_image(file_path=image_names.my_main_phase_file_path,
                            wait_seconds_limit=120)


def wait_until_my_draw_phase():
    game_common.click_image(file_path=image_names.my_draw_phase_file_path,
                            wait_seconds_limit=120)


def draw_card():  # 950, 900
    game_common.move_mouse(x=950, y=700)
    game_common.click()
    time.sleep(2)
    game_common.click()


def click_normal_summon():
    game_common.click_image(file_path=image_names.normal_summon_file_path)


def click_option():
    game_common.click_image(file_path=image_names.option_file_path)


def is_more_than_one_enemy():
    return game_common.is_exists_image(file_path=image_names.select_a_target_monster_file_path)


def is_can_battle():
    return game_common.is_exists_image(file_path=image_names.change_to_battle_phase_file_path)


def is_can_attack():
    return game_common.is_exists_image(file_path=image_names.attack_file_path)


def is_need_to_discard_card():
    return game_common.is_exists_image(file_path=image_names.discard_card_file_path)


def click_attack():
    game_common.click_image(file_path=image_names.attack_file_path)


def click_confirm_btn():
    game_common.click_image(file_path=image_names.confirm_file_path)


def click_go_to_battle_phase():
    game_common.click_image(file_path=image_names.change_to_battle_phase_file_path)


def click_go_to_end_phase():
    game_common.click_image(file_path=image_names.change_to_end_phase_file_path)


def is_ok_btn_show():
    return game_common.is_exists_image(file_path=image_names.ok_btn_file_path, wait_seconds_limit=20)


def is_event_ok_btn_show():
    return game_common.is_exists_image(file_path=image_names.event_ok_btn_file_path, wait_seconds_limit=10)


def click_ok_btn():
    game_common.click_image(file_path=image_names.ok_btn_file_path)


def click_event_ok_btn():
    game_common.click_image(file_path=image_names.event_ok_btn_file_path)


def click_next_btn(wait_seconds_limit=60):
    game_common.click_image(file_path=image_names.next_btn_file_path, wait_seconds_limit=wait_seconds_limit)
