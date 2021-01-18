from items import item_database_manager
from orders import order_database_manager
from users import user_database_manager


class App:
    users = []
    items = []

    orders = []
    cart = []

    @staticmethod
    def init():
        App.users = user_database_manager.get_users()
        App.items = item_database_manager.get_items()
