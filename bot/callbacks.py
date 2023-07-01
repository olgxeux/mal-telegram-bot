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
    media_id: int
    is_new: bool = False


class ViewRemovingMenuCB(CallbackData, prefix="ViewReM"):
    media_type: str
    media_id: int
    from_page: int
    is_new: bool = False


class ViewAddingMenuCB(CallbackData, prefix="ViewAM"):
    media_id: int
