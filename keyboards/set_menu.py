from aiogram import Bot
from aiogram.types import BotCommand


# Функция для настройки кнопок меню бота
async def set_main_menu(bot: Bot):
    commands = {
        "/375plus": "От 375 RTTF",
        "/300_575": "От 300 до 575 RTTF",
        "/boloto": "До 375 RTTF",
    }
    main_menu_commands = [
        BotCommand(command=command, description=description)
        for command, description in commands.items()
    ]
    await bot.set_my_commands(main_menu_commands)
