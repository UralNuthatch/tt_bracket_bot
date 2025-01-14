import asyncio
import logging
from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config
from handlers import user_handlers


async def main():
    # Получаем token бота из конфига(через переменные окружения)
    config: Config = load_config()

    bot = Bot(token=config.tgbot.token)
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

    # Запускаем бота на long-polling
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())