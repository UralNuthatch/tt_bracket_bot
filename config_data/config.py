from environs import Env
from dataclasses import dataclass


@dataclass
class TgBot:
    token: str


@dataclass
class Config:
    tgbot: TgBot
    google_doc: str


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)

    return Config(tgbot=TgBot(token=env("BOT_TOKEN")), google_doc=env("GOOGLE_DOC"))