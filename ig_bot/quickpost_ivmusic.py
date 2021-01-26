from instabot import Bot


def caption():

    txt = "Los @insurgentes.mx at Cafe Iguana.\n" + "Shot with Fujifilm xt20"

    hashtags = (
        ".\n"
        + ".\n"
        + ".\n"
        + ".\n"
        + ".\n"
        + ".\n"
        + "#myfujifilm #myfujilove #fujifilm #fujixpassion #iconcertphoto #raw_concert #audioloveofficial #audioblush_ #livemusiccollective #fazefeatures #5framerecords #musicphotomag #livemusicpictures #concertphoto #concertpics #concertphotography #musiclovers #musicphotography #bestmusicshots #bandphotography #livephotographer #livemusicphotographer #liveshows #livephotography #liveconcert #concertphotographersaroundtheworld #concertphotographer #concertjunkie #htbarp #photooftheday"
    )

    return txt + hashtags


def selecting_img():

    txt_path = "/home/dsalzedon/ivaninthemusic/photonum.txt"

    with open(txt_path, "r") as file:
        pic_num = str(file.readline())

    with open(txt_path, "w") as file:
        pic_num2 = int(pic_num) + 1
        file.write(str(pic_num2))

    return f"/home/dsalzedon/ivaninthemusic/pic/pic{pic_num}.jpg"


def upload_img():
    complete_caption = caption()
    img_path = selecting_img()
    bot = Bot()
    bot.login(username="xxx", password="xxx")
    bot.upload_photo(img_path, caption=complete_caption)


if __name__ == "__main__":
    pass
