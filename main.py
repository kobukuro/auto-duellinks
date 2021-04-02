from setting import setting
from functions.game import game_common
from functions.game.card_flipper import card_flipper
import os

if __name__ == '__main__':
    # os.startfile(setting.GAME_SHORTCUT_PATH)
    # game_common.click_start_game()
    game_common.open_window()
    # region everyday reward
    # game_common.click_ok_btn()
    # game_common.click_next_one_btn()
    # endregion
    # region card clipper
    # game_common.click_card_flipper_close_btn()
    # card_flipper.click_duke_card()
    # game_common.click_ok_btn()
    # endregion
    # region eberyday notify

    # endregion
    # game_common.close_message_windows()
    game_common.choose_character()
