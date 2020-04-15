import telebot
from telebot import types
import COVID19Py

covid19 = COVID19Py.COVID19()
bot = telebot.TeleBot('981563400:AAHgKqCZIF0rBRcNmmS5_upaFDMJ0pYGPfs')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('Во всём мире')
    btn2 = types.KeyboardButton('Кыргызстан')
    markup.add(btn1, btn2)

    send_message = f"Привет {message.from_user.first_name}!"
    bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=markup)

# TEMPLATES
confirmed_text = 'Подтвержденные случаи: '
deaths_text = 'Летальные исходы: '

# Функция, что сработает при отправке какого-либо текста боту
# Здесь мы создаем отслеживания данных и вывод статистики по определенной стране
data_kg = covid19.getLocationByCountryCode("KG")
confirmed_kg = data_kg[0]['latest']['confirmed']
deaths_kg = data_kg[0]['latest']['deaths']

data_world = covid19.getAll()
confirmed_world = data_world['latest']['confirmed']
deaths_world = data_world['latest']['deaths']

@bot.message_handler(content_types=['text'])
def mess(message):
    if message.text == 'Кыргызстан':
        bot.send_message(message.from_user.id, confirmed_text + str(confirmed_kg))
        bot.send_message(message.from_user.id, deaths_text + str(deaths_kg))
    else:
        bot.send_message(message.from_user.id, confirmed_text + str(confirmed_world))
        bot.send_message(message.from_user.id, deaths_text + str(deaths_world))

    # get_message_bot = message.text.strip().lower()
    # if get_message_bot == "кыргызстан":
    # 	location = covid19.getLocationByCountryCode("KG")
    # else:
    # 	location = covid19.getLatest()
    # final_message = f"Данные по всему миру: Заболевших: {location['confirmed']:,} Сметрей: {location['deaths']:,}"
    #
    # if final_message == "":
    # 	date = location[0]['last_updated'].split("T")
    # 	time = date[1].split(".")
    # 	final_message = f"Данные по стране: Население: {location[0]['country_population']:,}" \
    # 			f"Последнее обновление: {date[0]} {time[0]}<br>Последние данные:" \
    # 			f"Заболевших: {location[0]['latest']['confirmed']:,} Сметрей: " \
    # 			f"{location[0]['latest']['deaths']:,}"
    #
    # bot.send_message(message.chat.id, final_message, parse_mode='html')

# Это нужно чтобы бот работал всё время
bot.polling(none_stop=True)

#print(location)