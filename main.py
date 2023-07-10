import logging
import asyncio
from loader import dp, bot
from bot.handlers.start import *
from bot.handlers.main_menu import *
from bot.handlers.users_media_list import *
from bot.handlers.users_media import *
from bot.handlers.search_media import *


async def main() -> None:
    await dp.start_polling(bot)


logging.basicConfig(level=logging.INFO)
if __name__ == '__main__':
    asyncio.run(main())
