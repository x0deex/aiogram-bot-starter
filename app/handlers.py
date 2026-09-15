from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, CommandObject, Command

import app.keyboards as kb
from app.database.requests import set_user
router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await set_user(message.from_user.id)
    await message.answer("Добро пожаловать!", reply_markup=kb.reply_menu)