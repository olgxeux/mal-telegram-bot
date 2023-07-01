from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from motor.motor_asyncio import AsyncIOMotorClient

from gql import Client
from gql.transport.aiohttp import AIOHTTPTransport

from config import BOT_TOKEN, CONNECTION_STRING, DATABASE_NAME, GQL_SERVER

# parse_mode="MarkdownV2"
bot = Bot(BOT_TOKEN, parse_mode="Markdown")
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

mongo_client = AsyncIOMotorClient(CONNECTION_STRING)
user_db = mongo_client[DATABASE_NAME]

gql_transport = AIOHTTPTransport(url=GQL_SERVER)
gql_client = Client(transport=gql_transport)
