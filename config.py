from dotenv import dotenv_values

env_vars = dotenv_values('.env')

CONNECTION_STRING = str(env_vars["CONNECTION_STRING"])
DATABASE_NAME = str(env_vars["DATABASE_NAME"])
BOT_TOKEN = str(env_vars["BOT_TOKEN"])

GQL_SERVER = "https://graphql.anilist.co"
