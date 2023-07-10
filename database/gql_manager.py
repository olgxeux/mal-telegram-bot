from database.gql_strings import *
from gql import gql
from loader import gql_client


async def get_media(id: int) -> dict:
    async with gql_client as client:
        query = gql(GET_MEDIA_QUERY_STRING)
        variables = {"id": id}
        result = await client.execute(query, variable_values=variables)

        return result


async def get_short_media(id: int) -> dict:
    async with gql_client as client:
        query = gql(GET_SHORT_MEDIA_QUERY_STRING)
        variables = {"id": id}
        result = await client.execute(query, variable_values=variables)

        return result


async def get_page(page_number: int, title_name: str, title_type: str) -> dict:
    async with gql_client as client:
        query = gql(GET_PAGE_QUERY_STRING)
        variables = {
            "page": page_number,
            "search": title_name,
            "type": title_type
        }
        result = await client.execute(query, variable_values=variables)

        return result


# async def main():
#     result = await get_short_media(105778)
#     # result = await get_media(105778)
#     # result = await get_page(1, "naruto", "ANIME")
#     print(result)

# asyncio.run(main())
