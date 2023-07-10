from typing import Optional


def type_to_list_name(media_type: str) -> Optional[str]:
    if media_type == "anime":
        return "AnimeList"
    elif media_type == "manga":
        return "MangaList"
    else:
        return None
