import telebot
import webbrowser
from telebot import types

TOKEN = "7786992633:AAFqIm_HQLf-YXMDLd9-1EOgqkqMn6U9-zM"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.username} ')

@bot.message_handler(commands=['hello'])
def main(message):
    bot.send_message(message.chat.id, '<b>Приветики!</b> <em><u>Голубчик мой!</u></em> ', parse_mode='html')

@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://kwork.ru')

@bot.message_handler(content_types=['audio'])
def get_photo(message):
    bot.reply_to(message, 'Какой же у вас приятный голос!')

@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Перейти на сайт', url='https://ru.pinterest.com'))
    markup.add(types.InlineKeyboardButton('Удалить фото', callback_data='delete'))
    markup.add(types.InlineKeyboardButton('Изменить текст', callback_data='edit'))
    bot.reply_to(message, 'Кликни по кнопке, чтобы посмотреть офигенные тела красоток', reply_markup=markup)

bot.polling(none_stop=True)
