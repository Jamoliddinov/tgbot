from telebot import types


def generate_main_menu():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton(text="Ноутбуки")
    keyboard.row(btn)
    return keyboard


def generate_pagination():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_next = types.KeyboardButton(text="Далее")
    btn_prev = types.KeyboardButton(text="Назад")
    btn_menu = types.KeyboardButton(text="На главную страницу")
    keyboard.row(btn_prev, btn_next)
    keyboard.row(btn_menu)
    return keyboard


def generate_message_menu(url):
    keyboard = types.InlineKeyboardMarkup()
    btn_more = types.InlineKeyboardButton(text="Подробнее", url=url)
    btn_buy = types.InlineKeyboardButton(text="Купить", callback_data="buy")
    keyboard.row(btn_more, btn_buy)
    return keyboard
