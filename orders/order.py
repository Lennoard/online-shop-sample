from datetime import datetime


class Order:

    def __init__(self, order_id: str, user_id: str, items: [], date: datetime, finished: bool):
        self.id = order_id
        self.uid = user_id
        self.items = items  # Array of OrderItem
        self.date = date
        self.finished = finished
