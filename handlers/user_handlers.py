import logging
import asyncio

from aiogram import Router, F
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from aiogram.filters import CommandStart, Command

from handlers.google_tables import get_participants
from handlers.create_groups import create_groups
from handlers.rttf import refresh_rttf_ratings


# Создаем объект - роутер
router = Router()

logger = logging.Logger(__name__)


# Хэндлер на /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer("Hello")


@router.message(Command(commands="375plus"))
async def get_players_375plus(message: Message, participants: dict):
    try:
        participants["375plus"] = get_participants("375plus")
        players = ""
        for player in participants["375plus"]:
            players += " ".join(player) + "\n"

        button_rttf = InlineKeyboardButton(text="ОБНОВИТЬ RTTF", callback_data="refresh_rttf_375plus")
        button_groups = InlineKeyboardButton(text="ГРУППЫ", callback_data="create_groups_375plus")
        keyboard = InlineKeyboardMarkup(inline_keyboard=[[button_rttf], [button_groups]])

        await message.answer(text=players, reply_markup=keyboard)
    except Exception as ex:
        logging.error(ex)
        await message.answer("Что-то пошло не так")


# Обновление рттф рейтингов запускается в отдельном потоке
async def refresh_rttf_375plus_task(participants: dict, callback: CallbackQuery):
    try:
        await refresh_rttf_ratings(participants["375plus"])
        players = ""
        for player in participants["375plus"]:
            players += " ".join(player) + "\n"

        button_groups = InlineKeyboardButton(text="ГРУППЫ", callback_data="create_groups_375plus")
        keyboard = InlineKeyboardMarkup(inline_keyboard=[[button_groups]])
        await callback.message.answer(text=players, reply_markup=keyboard)
    except Exception as ex:
        logging.error(ex)
        await callback.message.answer("Что-то пошло не так")


@router.callback_query(F.data == "refresh_rttf_375plus")
async def refresh_rttf_375plus(callback: CallbackQuery, participants: dict):
    try:
        await callback.message.edit_text(text=callback.message.text)
        await callback.message.answer("Идет обновление рейтингов RTTF...")

        asyncio.create_task(refresh_rttf_375plus_task(participants, callback))
        
    except Exception as ex:
        logging.error(ex)
        await callback.message.answer("Что-то пошло не так")


@router.callback_query(F.data == "create_groups_375plus")
async def create_groups_375plus(callback: CallbackQuery, participants: dict):
    try:
        await callback.message.edit_text(text=callback.message.text)
        groups = create_groups(participants=participants["375plus"])
        if groups is None:
            await callback.answer("Количество участников меньше 16")
            return
        ans = ""
        for i, group in enumerate(groups):
            ans += f"\n*ГРУППА {str(i + 1)}*:\n"
            for participant in group:
                ans += " ".join(participant) + "\n"
        await callback.message.answer(text=ans)
    except Exception as ex:
        logging.error(ex)
        await callback.message.answer("Что-то пошло не так")


@router.message(Command(commands="300_575"))
async def get_players_300_575(message: Message, participants: dict):
    try:
        participants["300_575"] = get_participants("300_575")
        players = ""
        for player in participants["300_575"]:
            players += " ".join(player) + "\n"

        button_rttf = InlineKeyboardButton(text="ОБНОВИТЬ RTTF", callback_data="refresh_rttf_300_575")
        button_groups = InlineKeyboardButton(text="ГРУППЫ", callback_data="create_groups_300_575")
        keyboard = InlineKeyboardMarkup(inline_keyboard=[[button_rttf], [button_groups]])

        await message.answer(text=players, reply_markup=keyboard)
    except Exception as ex:
        logging.error(ex)
        await message.answer("Что-то пошло не так")


# Обновление рттф рейтингов запускается в отдельном потоке
async def refresh_rttf_300_575_task(participants: dict, callback: CallbackQuery):
    try:
        await refresh_rttf_ratings(participants["300_575"])
        players = ""
        for player in participants["300_575"]:
            players += " ".join(player) + "\n"

        button_groups = InlineKeyboardButton(text="ГРУППЫ", callback_data="create_groups_300_575")
        keyboard = InlineKeyboardMarkup(inline_keyboard=[[button_groups]])
        await callback.message.answer(text=players, reply_markup=keyboard)
    except Exception as ex:
        logging.error(ex)
        await callback.message.answer("Что-то пошло не так")


@router.callback_query(F.data == "refresh_rttf_300_575")
async def refresh_rttf_300_575(callback: CallbackQuery, participants: dict):
    try:
        await callback.message.edit_text(text=callback.message.text)
        await callback.message.answer("Идет обновление рейтингов RTTF...")

        asyncio.create_task(refresh_rttf_300_575_task(participants, callback))

    except Exception as ex:
        logging.error(ex)
        await callback.message.answer("Что-то пошло не так")


@router.callback_query(F.data == "create_groups_300_575")
async def create_groups_300_575(callback: CallbackQuery, participants: dict):
    try:
        await callback.message.edit_text(text=callback.message.text)
        groups = create_groups(participants=participants["300_575"])
        if groups is None:
            await callback.answer("Количество участников меньше 16")
            return
        ans = ""
        for i, group in enumerate(groups):
            ans += f"\n*ГРУППА {str(i + 1)}*:\n"
            for participant in group:
                ans += " ".join(participant) + "\n"
        await callback.message.answer(text=ans)
    except Exception as ex:
        logging.error(ex)
        await callback.message.answer("Что-то пошло не так")


@router.message(Command(commands="boloto"))
async def get_players_boloto(message: Message, participants: dict):
    try:
        participants["boloto"] = get_participants("boloto")
        players = ""
        for player in participants["boloto"]:
            players += " ".join(player) + "\n"

        button_rttf = InlineKeyboardButton(text="ОБНОВИТЬ RTTF", callback_data="refresh_rttf_boloto")
        button_groups = InlineKeyboardButton(text="ГРУППЫ", callback_data="create_groups_boloto")
        keyboard = InlineKeyboardMarkup(inline_keyboard=[[button_rttf], [button_groups]])

        await message.answer(text=players, reply_markup=keyboard)
    except Exception as ex:
        logging.error(ex)
        await message.answer("Что-то пошло не так")


# Обновление рттф рейтингов запускается в отдельном потоке
async def refresh_rttf_boloto_task(participants: dict, callback: CallbackQuery):
    try:
        await refresh_rttf_ratings(participants["boloto"])
        players = ""
        for player in participants["boloto"]:
            players += " ".join(player) + "\n"

        button_groups = InlineKeyboardButton(text="ГРУППЫ", callback_data="create_groups_boloto")
        keyboard = InlineKeyboardMarkup(inline_keyboard=[[button_groups]])
        await callback.message.answer(text=players, reply_markup=keyboard)
    except Exception as ex:
        logging.error(ex)
        await callback.message.answer("Что-то пошло не так")


@router.callback_query(F.data == "refresh_rttf_boloto")
async def refresh_rttf_boloto(callback: CallbackQuery, participants: dict):
    try:
        await callback.message.edit_text(text=callback.message.text)
        await callback.message.answer("Идет обновление рейтингов RTTF...")
        asyncio.create_task(refresh_rttf_boloto_task(participants, callback))

    except Exception as ex:
        logging.error(ex)
        await callback.message.answer("Что-то пошло не так")


@router.callback_query(F.data == "create_groups_boloto")
async def create_groups_boloto(callback: CallbackQuery, participants: dict):
    try:
        await callback.message.edit_text(text=callback.message.text)
        groups = create_groups(participants=participants["boloto"])
        if groups is None:
            await callback.answer("Количество участников меньше 16")
            return
        ans = ""
        for i, group in enumerate(groups):
            ans += f"\n*ГРУППА {str(i + 1)}*:\n"
            for participant in group:
                ans += " ".join(participant) + "\n"
        await callback.message.answer(text=ans)
    except Exception as ex:
        logging.error(ex)
        await callback.message.answer("Что-то пошло не так")