# items = {
#     0: {"name": "First item"},
# }


# def search() -> list:
#     return items

from flask_injector import inject
from services.provider import ItemsProvider

@inject(data_provider=ItemsProvider)
def search(data_provider) -> list:
    return data_provider.get()