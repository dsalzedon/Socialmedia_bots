"""
pip install -U instabot
git clone https://github.com/instagrambot/instabot --recursive
cd instabot/examples

"""

from instabot import Bot
import datetime

bot = Bot()
bot.login(username="xxx", password="xxx")


# CAPTION Y HASHTAGS
def caption():
    txt = "Los @insurgentes.mx at Cafe Iguana. \n" + "Shot with Fujifilm xt20"

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
    txt_path = "/Users/dsalzedo/Documents/Python/Scripts/Instabot/photonum.txt"

    with open(txt_path, "r") as file:
        pic_num = str(file.readline())

    with open(txt_path, "w") as file:
        pic_num2 = int(pic_num) + 1
        file.write(str(pic_num2))

    return f"/Users/dsalzedo/Documents/Python/Scripts/Instabot/pic/pic{pic_num}.jpg"


def upload_img():
    complete_caption = caption()
    img_path = selecting_img()
    bot.upload_photo(img_path, caption=complete_caption)


date = datetime.datetime.now()
day = date.strftime("%A")

if day == "Monday":
    upload_img()
else:
    quit()

