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
    # is_in_list: bool
    from_page: int


class ViewRatingMenuCB(CallbackData, prefix="ViewRaM"):
    media_type: str
    media_id: int
    from_page: int
    is_new: bool = False


class ChangeRatingCB(CallbackData, prefix="ChangeRa"):
    media_type: str
    media_id: int
    rating: int
    from_page: int
    is_new: bool = False


class ViewStatusMenuCB(CallbackData, prefix="ViewSM"):
    media_type: str
    media_id: int
    from_page: int
    is_new: bool = False


class ChangeStatusCB(CallbackData, prefix="ChangeS"):
    media_type: str
    media_id: int
    status: int
    from_page: int
    is_new: bool = False


class ViewRemovingMenuCB(CallbackData, prefix="ViewReM"):
    media_type: str
    media_id: int
    from_page: int
    is_new: bool = False


class RemoveMediaCB(CallbackData, prefix="RemoveM"):
    media_type: str
    media_id: int
    from_page: int
    is_new: bool = False


class SearchMediaCB(CallbackData, prefix="SearchM"):
    media_type: str
    from_page: int


class ViewSearchListCB(CallbackData, prefix="ViewSL"):
    search_prompt: str | None
    media_type: str
    page: int
    from_page: int
    is_back: bool = False


class ViewSearchMediaCB(CallbackData, prefix="ViewSeM"):
    media_type: str
    media_id: int
    # is_in_list: bool
    from_page: int
    search_prompt: str


class ViewAddingMenuCB(CallbackData, prefix="ViewAM"):
    media_id: int
