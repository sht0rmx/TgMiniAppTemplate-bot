from aiogram import types
from aiogram.filters import Command

from handlers.commands import command_router
from utils.messages import get_data


@command_router.message(Command("help"))
async def send_help(msg: types.Message):
    text, markup, parse_mode = await get_data(msg, "help")
    await msg.answer(text, reply_markup=markup, parse_mode=parse_mode)