from functions.game import game_common
from setting.setting import EverydayNotifyImagesNames

image_names = EverydayNotifyImagesNames()


def click_back_btn():
    game_common.click_image(file_path=image_names.back_arrow_file_path)
