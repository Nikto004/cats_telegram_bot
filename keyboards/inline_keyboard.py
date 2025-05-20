from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def main_button():
    main_markup = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton(text='Да', callback_data='yes')
    btn2 = InlineKeyboardButton(text='Нет', callback_data='no')
    btn3 = InlineKeyboardButton(text='Покажи котиков', callback_data='cats')
    main_markup.add(btn1, btn2).add(btn3)
    return main_markup


def seconds_cat():
    markup = InlineKeyboardMarkup()
    btn = InlineKeyboardButton(text='Больше котиков', callback_data='cats')
    markup.add(btn)
    return markup
