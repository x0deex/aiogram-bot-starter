from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

reply_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Администрторы"),
            KeyboardButton(text="Пользователи"),
        ],
        [
            KeyboardButton(text="Статистика"),
            KeyboardButton(text="Платежи"),
            KeyboardButton(text="Активность"),
        ],
        [
            KeyboardButton(text="Заблокировать"),
            KeyboardButton(text="Разблокировать"),
        ],
    ],
resize_keyboard=True, 
input_field_placeholder="выберите из пункта ниже", 
one_time_keyboard=True)
