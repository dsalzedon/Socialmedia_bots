"""
pip install -U instabot
git clone https://github.com/instagrambot/instabot --recursive
cd instabot/examples

"""

from instabot import Bot
import datetime

bot = Bot()


# CAPTION Y HASHTAGS
def caption(day):

    if day == "Monday":

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

    else:
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


def selecting_img(day):
    if day == "Monday":

        txt_path = "/home/dsalzedon/ivaninthemusic/photonum.txt"

        with open(txt_path, "r") as file:
            pic_num = str(file.readline())

        with open(txt_path, "w") as file:
            pic_num2 = int(pic_num) + 1
            file.write(str(pic_num2))

        return f"/home/dsalzedon/ivaninthemusic/pic/pic{pic_num}.jpg"

    else:
        txt_path = "/home/dsalzedon/ivnavarr/photonum.txt"

        with open(txt_path, "r") as file:
            pic_num = str(file.readline())

        with open(txt_path, "w") as file:
            pic_num2 = int(pic_num) + 1
            file.write(str(pic_num2))

        return f"/home/dsalzedon/ivnavarr/pic/pic{pic_num}.jpg"


def upload_img(day):
    complete_caption = caption(day)
    img_path = selecting_img(day)
    bot.upload_photo(img_path, caption=complete_caption)


date = datetime.datetime.now()
day = date.strftime("%A")

if day == "Monday":
    bot.login(username="xxx", password="xxx")
    upload_img(day)
elif day == "Tuesday":
    bot.login(username="xxx", password="xxx")
    upload_img(day)
else:
    quit()

