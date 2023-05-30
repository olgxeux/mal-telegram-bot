from dotenv import dotenv_values

env_vars = dotenv_values('.env')

CONNECTION_STRING = env_vars["CONNECTION_STRING"]
DATABASE_NAME = env_vars["DATABASE_NAME"]
BOT_TOKEN = env_vars["BOT_TOKEN"]
