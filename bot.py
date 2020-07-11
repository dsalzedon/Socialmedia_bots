from instabot import Bot
import datetime


# funcion para escoger el dia y el caption
def day_cap():
    global day_num, cap, x
    if day == "Monday":
        # asignar la linea (0=lunes, 1=miercoles, 2=viernes, 3=sabado)
        day_num = 0
        # obtener el numero de foto q se va a subir
        day_photo(day_num)
        cap = "Diego Gongora"

    elif day == "Wednesday":
        day_num = 1
        day_photo(day_num)
        cap = "Kahlo"

    elif day == "Friday":
        day_num = 2
        day_photo(day_num)
        # si el numero es par usar fotos del lunes si es impar del miercoles
        if data % 2 == 0:
            x = 0
        else:
            x = 1

    elif day == "Saturday":
        day_num = 3
        day_photo(day_num)
        cap = "Los Insurgentes"

    else:
        print("NOT TODAY BABY")


# funcion para saber la foto que se va a subir
def day_photo(day_num):
    global data
    line_to_read = [day_num]
    for position, line in enumerate(file_txt):
        if position in line_to_read:
            # el valor de a linea q se lee
            data = int(line)


# funcion para el viernes subir foto del lunes o del miercoles y su caption
def photo_friday():
    global day, day_num, cap
    if x == 0:
        day = "Monday"
        day_num = 0
        day_photo(day_num)
        cap = "Diego Gongora"
    else:
        day = "Wednesday"
        day_num = 1
        day_photo(day_num)
        cap = "Kahlo"


# funcion para convertir los datos y poder usarlos en las formulas
def rw_data():
    global num, num2
    # num = el dato que se lee en el archivo
    num = data
    # num2 es el q va a reemplazar
    num2 = num + 1
    # convierto a string para remplazar en las formulas
    num, num2 = str(num), str(num2)


# funcion para sobreescribir en el archivo los nuevos valores
def rw_txt():
    # abrir el archivo en lectura
    file_txt = open(file_path, "r")
    # leer todas las lineas
    line_to_write = file_txt.readlines()
    # seleccionar linea para escribir
    line_to_write[day_num] = "{}\n".format(num2)
    # parametro escribir(write) en el archivo
    file_txt = open(file_path, "w")
    # sobreescribir en la linea escogida
    file_txt.writelines(line_to_write)
    file_txt.close()


# obtener la fecha y obtener el dia de hoy
date = datetime.datetime.now()
day = (date.strftime("%A"))

# iniciar bot y cuenta de IG
bot = Bot()
bot.login(username="xxxx", password="xxxx")

# ruta de acceso al archivo
file_path = "/Users/dsalzedo/Documents/Python/PyInsta/ivaninthemusic/photonum.txt"

# abrir archivo de texto
file_txt = open(file_path, "rt")

# seleccionar la foto y el caption segun el dia
day_cap()

# cerrar el archivo para llevar un orden
file_txt.close()

# darle formato para trabajar con los datos
rw_data()

# reemplazar los datos en el texto
rw_txt()

# leer y reemplaar el valor del dia distinto al viernes (i.e. Lunes o Miercoles)
if day == "Friday":
    # abrir archivo de texto
    file_txt = open(file_path, "rt")
    # escoger si subir de lunes o miercoles
    photo_friday()
    # cerrar archivo de texto
    file_txt.close()
    # darle formato para trabajar con los datos
    rw_data()
    # reemplazar los datos en el texto
    rw_txt()

# ruta de acceso a las fotos y subir caption y hashtags
bot.upload_photo("/Users/dsalzedo/Documents/Python/PyInsta/ivaninthemusic/{}/{}.jpg".format(day, num),
                 caption="{} at Dakota Studio Bar. Shot with a Sony a6000 and a Tamron 70-200mm 2.8.".format(
                     cap) + '\n' + '.\n'
                 + '.\n' + '.\n'
                 + '.\n' + '.\n'
                 + "#iconcertphoto #raw_concert #audioloveofficial #livemusiccollective #htbarp #concertjunkie #livemusicphotographer #bestmusicshots #concertphoto #livephotographer #livephotography #musicphotography #tonekillers #AGameofTones #sonyalpha #sonya6000 #tamronglobal #mytamronlens #bandphotography #5framerecords #instrumentals #musiclovers #liveconcert #band #concertphotographersaroundtheworld #concertphotographer #liveshows #livemusic #livemusicphotography")
