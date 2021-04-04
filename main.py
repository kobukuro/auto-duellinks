from setting import setting
from functions.game import game_common
from functions.game.duel import duel
from functions.game.card_flipper import card_flipper
from functions.game.everyday_notify import everyday_notify
import os
import pyautogui
import time

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
    # region everyday notify
    # everyday_notify.click_back_btn()
    # endregion
    # game_common.close_message_windows()
    # game_common.choose_character()
    duel_turns = 5
    for i in range(duel_turns):
        print(f'duel start {i}th run')
        game_common.click_gate()
        game_common.click_duel_btn()
        game_common.skip_dialog()
        game_common.click_inner_duel_btn()
        no_more_summon = False
        while True:
            duel.wait_until_my_draw_phase()
            time.sleep(2)
            duel.draw_card()
            duel.wait_until_my_main_phase()
            if not no_more_summon:
                game_common.move_mouse(x=950, y=900)
                game_common.click()
                duel.click_normal_summon()
                no_more_summon = True
            duel.click_option()
            is_can_battle = duel.is_can_battle()
            if is_can_battle:
                duel.click_go_to_battle_phase()
                game_common.move_mouse(x=950, y=600)
                time.sleep(0.5)
                game_common.click()
                if duel.is_can_attack():  # 假如可以攻擊
                    duel.click_attack()
                    is_more_than_one_enemy = duel.is_more_than_one_enemy()
                    if is_more_than_one_enemy:
                        game_common.move_mouse(x=700, y=700)
                        game_common.click()
                        duel.click_confirm_btn()
                    is_finish = duel.is_ok_btn_show()
                    if is_finish:
                        duel.click_ok_btn()
                        break
                    duel.click_option()
                    duel.click_go_to_end_phase()
                else:  # 假如不能攻擊
                    game_common.click()
                    duel.click_option()
                    duel.click_go_to_end_phase()
            else:  # 不能攻擊
                # click button to go to end phase
                duel.click_go_to_end_phase()
            is_need_to_discard_card = duel.is_need_to_discard_card()
            if is_need_to_discard_card:
                game_common.move_mouse(x=700, y=700)
                game_common.click()
                duel.click_confirm_btn()
        try:
            duel.click_next_btn(wait_seconds_limit=80)  # 經驗值畫面next
        except:  # 遇到升級的時候
            game_common.click()
            duel.click_next_btn()  # 經驗值畫面next
        duel.click_next_btn()  # duel results
        # region 活動按ok
        is_event_ok_btn_show = duel.is_event_ok_btn_show()
        if is_event_ok_btn_show:
            duel.click_event_ok_btn()
        # endregion
        game_common.skip_dialog()
        game_common.close_message_windows()
        # print(f'duel end {i}th run')
