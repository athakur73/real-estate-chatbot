def is_save_intent(message: str) -> bool:
    keywords = ["save", "bookmark", "favorite", "add"]
    return any(k in message.lower() for k in keywords)


def is_show_saved_intent(message: str) -> bool:
    keywords = ["saved", "favorites", "wishlist"]
    return any(k in message.lower() for k in keywords)
