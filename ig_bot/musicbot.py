from instabot import Bot
import random
import datetime


# empezar y obtener el artista, tag y caption
def day_of_the_week():
        if day == "Monday":
                working()
        elif day == "Thursday":
                working()
        else:
                print("NOT TODAY BABY")

def working():
        login()
        random_artist()
        day_photo(file_line)
        rw_data()
        rw_txt()
        # ruta de acceso a las fotos y subir caption y hashtags
        img_path = "/home/dsalzedon/ivaninthemusic/{}/{}.jpg".format(day, num)

        hashtags = ".\n" + ".\n" + ".\n"
                + ".\n" + ".\n" + ".\n"
                + "#iconcertphoto #raw_concert #audioloveofficial #livemusiccollective #htbarp #concertjunkie #livemusicphotographer #bestmusicshots #concertphoto #livephotographer #livephotography #musicphotography #tonekillers #AGameofTones #sonyalpha #sonya6000 #tamronglobal #mytamronlens #bandphotography #5framerecords #instrumentals #musiclovers #liveconcert #band #concertphotographersaroundtheworld #concertphotographer #liveshows #livemusic #livemusicphotography"

        complete_caption = txt + hashtags

        users_to_tag = [{"xxx": 0, 'x': 0, 'y': 0},
                        {'raw_concert': 13745410234, 'x': 0.2, 'y': 0.1},
                        {'iconcertphoto': 2020362794, 'x': 0.3, 'y': 0.1},
                        {'audioloveofficial': 1758408188, 'x': 0.3, 'y': 0.1},
                        {'livemusiccollective': 5596681455, 'x': 0.4, 'y': 0.1},
                        {'htbarp': 7170758637, 'x': 0.5, 'y': 0.1},
                        {'fujifilmmx': 1452044037, 'x': 0.6, 'y': 0.9},
                        {'fujixlovers': 2897691882, 'x': 0.7, 'y': 0.9},
                        {'_fujilove_': 1981778444, 'x': 0.8, 'y': 0.9},
                        {'fujifilm_northamerica': 1703295748, 'x': 0.9, 'y': 0.9},
                        {'5framerecords': 30420593786, 'x': 0.9, 'y': 0.1}]
        users_to_tag[0] = acc_tag

        bot.upload_photo(img_path, user_tags=users_to_tag, caption=complete_caption)

# iniciar sesion en ig y abrir el archivo de texto
def login():
        global file_txt
        bot = Bot()
        bot.login(username="xxx", password="xxxx")
        
        file_txt = open(file_path, "rt")


# escoger artista, sus tags y caption
def random_artist():
        global acc_tag, txt, file_line
        artists = ["insurgentes", "medina", "filip"]
        artist_choice = random.choice(artists)

        if artist_choice == "insurgentes":
                acc_tag = {"insurgentes.mx": 4609726865, 'x': 0.1, 'y': 0.1}
                txt = "Los insurgentes at Café iguana. \n" + "Shot with Fujifilm xt20"
                file_line = 0

        elif artist_choice == "medina":
                acc_tag = {"medinnaoficial": 4749207001, 'x': 0.1, 'y': 0.1}
                txt = "Medinna at Café iguana. \n" + "Shot with Fujifilm xt20"
                file_line = 1

        elif artist_choice == "filip":
                acc_tag = {"filipywoppe": 8357320115, 'x': 0.1, 'y': 0.1}
                txt = "Filip y Woppe, la cumbia poderosa en Xalapa. \n" + "Shot with Fujifilm xt20"
                file_line = 2


# saber la foto que se va a subir
def day_photo(file_line):
        global data
        line_to_read = [file_line]
        for position, line in enumerate(file_txt):
                if position in line_to_read:
                        data = int(line)
        file_txt.close()


# convertir los datos  a string  para poder usarlos en las formulas
def rw_data():
        global num, num2
        num = data
        num2 = num + 1
        num, num2 = str(num), str(num2)


# reemplazar los datos en el archivo de texto
def rw_txt():
        file_txt = open(file_path, "r")
        line_to_write = file_txt.readlines()
        line_to_write[file_line] = "{}\n".format(num2)
        file_txt = open(file_path, "w")
        file_txt.writelines(line_to_write)
        file_txt.close()


# obtener la fecha y obtener el dia de hoy
date = datetime.datetime.now()
day = (date.strftime("%A"))

# ruta de acceso al archivo
file_path = "/home/dsalzedon/ivaninthemusic/photonum.txt"

# seleccionar la foto y el caption segun el dia
day_of_the_week()
