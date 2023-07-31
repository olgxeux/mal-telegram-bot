from aiogram.filters.callback_data import CallbackData


class ViewMainMenuCB(CallbackData, prefix="ViewMM"):
    pass


class ViewUsersListCB(CallbackData, prefix="ViewUL"):
    media_type: str
    page: int
    is_back: bool = False


class ViewUsersMediaCB(CallbackData, prefix="ViewUM"):
    media_type: str
    media_id: int
    from_page_user: int
    from_page_search: int = 0
    search_prompt: str | None = None



class ViewRatingMenuCB(CallbackData, prefix="ViewRaM"):
    media_type: str
    media_id: int
    from_page_user: int
    is_new: bool = False


class ChangeRatingCB(CallbackData, prefix="ChangeRa"):
    media_type: str
    media_id: int
    rating: int
    from_page_user: int
    is_new: bool = False


class ViewStatusMenuCB(CallbackData, prefix="ViewSM"):
    media_type: str
    media_id: int
    from_page_user: int
    is_new: bool = False


class ChangeStatusCB(CallbackData, prefix="ChangeS"):
    media_type: str
    media_id: int
    status: int
    from_page_user: int
    is_new: bool = False


class ViewRemovingMenuCB(CallbackData, prefix="ViewReM"):
    media_type: str
    media_id: int
    from_page_user: int
    is_new: bool = False


class RemoveMediaCB(CallbackData, prefix="RemoveM"):
    media_type: str
    media_id: int
    from_page_user: int
    is_new: bool = False


class SearchMediaCB(CallbackData, prefix="SearchM"):
    media_type: str
    from_page_user: int


class ViewSearchListCB(CallbackData, prefix="ViewSL"):
    search_prompt: str | None
    media_type: str
    page: int
    from_page_user: int
    is_back: bool = False


class ViewSearchMediaCB(CallbackData, prefix="ViewSeM"):
    media_type: str
    media_id: int
    from_page_user: int
    from_page_search: int
    search_prompt: str


class ViewAddRatingMenuCB(CallbackData, prefix="ViewARM"):
    media_type: str
    media_id: int
    from_page_user: int
    from_page_search: int
    search_prompt: str | None


class ViewAddStatusMenuCB(CallbackData, prefix="ViewASM"):
    media_type: str
    media_id: int
    from_page_user: int
    search_prompt: str
    rating: int
    from_page_search: int



class AddMediaCB(CallbackData, prefix="AddM"):
    media_type: str
    media_id: int
    from_page_user: int
    search_prompt: str
    rating: int
    status: int
    from_page_search: int


# class AddStatusMenuCB(CallbackData, prefix="ViewSM"):
#     media_type: str
#     media_id: int
#     from_page_user: int
#     is_new: bool = False
