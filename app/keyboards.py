from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

reply_menu = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Каталог"), KeyboardButton(text="Корзина")],
    [KeyboardButton(text="Поддержка")]
], resize_keyboard=True, input_field_placeholder="выберите из пункта ниже")