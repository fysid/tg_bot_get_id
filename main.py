#! /usr/bin/python3

import asyncio

from lib.utils import BotConfig
from lib.IdBot import IdBot

async def main():
    bot = IdBot(BotConfig)
    await bot.run_forever()


if __name__ == '__main__':
    asyncio.run(main())