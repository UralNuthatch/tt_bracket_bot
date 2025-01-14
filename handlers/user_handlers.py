import logging

from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart


# Создаем объект - роутер
router = Router()

logger = logging.Logger(__name__)


# Хэндлер на /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer("Hello")