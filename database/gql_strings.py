GQL_SERVER = "https://graphql.anilist.co"

GET_MEDIA_QUERY_STRING = """
query GetMedia($id: Int!) {
  Media(id: $id) {
    id
    averageScore
    type
    title {
      userPreferred
      english
      romaji
    }
    format
    status
    episodes
    chapters
    startDate {
      year
    }
    coverImage {
      extraLarge
    }
    description(asHtml: false)
  }
}"""

GET_SHORT_MEDIA_QUERY_STRING = """
query GetShortMedia($id: Int!) {
  Media(id: $id) {
    id
    title {
      userPreferred
      english
      romaji
    }
    format
  }
}"""

GET_PAGE_QUERY_STRING = """
query GetPage($page: Int!, $search: String!, $type: MediaType!) {
  Page(page: $page, perPage: 3) {
    media(search: $search, type: $type, sort: POPULARITY_DESC) {
      id
      title {
        userPreferred
        romaji
        english
      }
      format
    }
    pageInfo {
      hasNextPage
    }
  }
}"""
