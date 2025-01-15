import asyncio
import logging
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config
from handlers import user_handlers
from keyboards.set_menu import set_main_menu


async def main():
    # Получаем token бота из конфига(через переменные окружения)
    config: Config = load_config()

    bot = Bot(token=config.tgbot.token, default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN),)
    dp = Dispatcher()

    # Конфигурируем и запускаем логирование
    logger = logging.getLogger("tt_bracket_bot")
    logging.basicConfig(
        format="[{asctime}] #{levelname:8} {filename}:" "{lineno} - {name} - {message}",
        style="{",
        level=logging.WARNING,
    )
    logger.warning("Starting bot...")

    # Регистрируем роутеры в диспетчере
    dp.include_router(user_handlers.router)

    # Регистрируем асинхронную функцию в диспетчере,
    # которая будет выполняться на старте бота
    dp.startup.register(set_main_menu)

    # Временно хранилище участников
    dp.workflow_data.update({"participants":
                                {
                                    "375plus": None,
                                    "300_575": None,
                                    "boloto": None
                                }
                             })

    # Запускаем бота на long-polling
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())