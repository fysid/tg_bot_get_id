import aiogram
from aiogram import types
from aiogram.filters.command import Command

from lib.utils import BotConfig


class IdBot():
    def __init__(
        self,
        config: BotConfig,
    ) -> None:
        self.config = config()
        self.bot = aiogram.Bot(self.config.bot_token)
        self.dp = aiogram.Dispatcher()

        self.dp.message(Command("start"))(self.send_user_id)
        self.dp.message(lambda message: any(message))(self.send_user_id)

    
    async def send_user_id(self, message: types.Message) -> None:
        await self.bot.send_message(message.from_user.id, str(message.from_user.id))


    async def run_forever(self):
        await self.dp.start_polling(self.bot)
