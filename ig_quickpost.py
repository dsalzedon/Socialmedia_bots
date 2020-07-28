"""
ESTE PROGRAMA ES SOLO PARA SUBIR RAPIDAMENTE UNA FOTO
UNO DANDO EL DIA Y EL NUMERO DE LA FOTO
"""

from instabot import Bot

bot = Bot()
bot.login(username="xxx", password="xxx")

num = str(1)

day = "Monday"

# ruta de acceso a las fotos y subir caption y hashtags
bot.upload_photo("/Users/dsalzedo/Documents/Python/pruebas/{}/{}.jpg".format(day, num),
                 caption="nuevas pruebas nuevas de verdad" + '\n' + '.\n'
                 + '.\n' + '.\n'
                 + '.\n' + '.\n'
                 + "#iconcertphoto #raw_concert #audioloveofficial #livemusiccollective #htbarp #concertjunkie #livemusicphotographer #bestmusicshots #concertphoto #livephotographer #livephotography #musicphotography #tonekillers #AGameofTones #sonyalpha #sonya6000 #tamronlens #mytamronlens #tamron #70200")
