
import time
import telebot
from threading import Thread
from telebot.apihelper import ApiTelegramException
import os
from pymatting import cutout


# основнйо бот
bot = telebot.TeleBot("")  #token of your bot


@bot.message_handler(commands=["start"])
def startjoin(message):
    bot.send_message(message.chat.id, "Привет. Я Kaifon. Я убираю фон с фотографий. Просто скинь мне фото")

@bot.message_handler(content_types=['photo'])
def photo(message):
    print ('message.photo =', message.photo)
    fileID = message.photo[-1].file_id
    print ('fileID =', fileID)
    file_info = bot.get_file(fileID)
    print ('file.file_path =', file_info.file_path)
    downloaded_file = bot.download_file(file_info.file_path)

    with open(fileID +".jpg", 'wb') as new_file:
        new_file.write(downloaded_file)

    bot.send_message(message.chat.id, "Загружаем фото")

    os.system("rembg i " + fileID +".jpg" + ' ' + fileID +"2.jpg")  # убираем фон

    bot.send_message(message.chat.id, "Делаем красиво")

    bot.send_photo(message.chat.id, photo=open(fileID +'2.jpg', 'rb'))

    bot.send_message(message.chat.id, "Фон удален! Будем рады фидбеку @tsimmoukr")

    print('done')

def main_loop():
    bot.polling(True)

if __name__ == '__main__':
    main_loop()