from instabot import Bot


def caption():

    txt = (
        "August series.\n"
        + "\nThese past months I decided to capture the few times I leave my home and try to make an album per month that summarizes them."
    )

    hashtags = (
        ".\n"
        + ".\n"
        + ".\n"
        + ".\n"
        + ".\n"
        + ".\n"
        + "#myfujifilm #myfujilove #Fujifilmmx #fujixpassion #tnscollective #StreetNL #CrosswalkAllStars #republicofstreet #fujifilm_street #sublimestreet #photooftheday #thecitymag #passionpassport #TheCoolMagazine #JustGoShoot #tonekillers #grupo_intestino #mydaidia"
    )
    return txt + hashtags


def selecting_img():

    txt_path = "/home/dsalzedon/ivnavarr/photonum.txt"

    with open(txt_path, "r") as file:
        pic_num = str(file.readline())

    with open(txt_path, "w") as file:
        pic_num2 = int(pic_num) + 1
        file.write(str(pic_num2))

    return f"/home/dsalzedon/ivnavarr/pic/pic{pic_num}.jpg"


def upload_img():
    complete_caption = caption()
    img_path = selecting_img()
    bot = Bot()
    bot.login(username="xxx", password="xxx")
    bot.upload_photo(img_path, caption=complete_caption)


if __name__ == "__main__":
    pass
