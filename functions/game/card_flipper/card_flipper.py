from functions.game import game_common
from setting.setting import CardFlipperImagesNames

image_names = CardFlipperImagesNames()


def click_duke_card():
    game_common.click_image(file_path=image_names.duke_file_path)
