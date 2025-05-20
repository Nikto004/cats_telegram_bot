from telebot import TeleBot, types
from conf import settings
from keyboards.inline_keyboard import main_button, seconds_cat
import requests


bot = TeleBot(settings.BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start_cmd(message: types.Message):
    bot.send_message(
        message.chat.id,
        "Привет я инфо бот\nХочешь узнать свои данные",
        reply_markup=main_button()
    )


@bot.callback_query_handler(func=lambda call: call.data == 'yes' or call.data == 'no')
def answer_cmd(callback: types.CallbackQuery):
    if callback.data == 'yes':
        user_id = callback.message.chat.id
        username = callback.message.from_user.username
        bot.send_message(callback.message.chat.id, f'Id: {user_id}\nUsername:{username}')
    if callback.data == 'no':
        print("Отказ")


def get_cats():
    response = requests.get(settings.URL_ROOT)
    print("Фотография котика отправлена пользователю!")
    return response.content


@bot.callback_query_handler(func=lambda call: call.data == 'cats')
def show_cats(callback: types.CallbackQuery):
    get_photo = get_cats()
    bot.send_photo(callback.message.chat.id, get_photo, reply_markup=seconds_cat())


bot.infinity_polling()
