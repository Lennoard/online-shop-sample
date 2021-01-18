class Item(object):
    def __init__(self, item_id: str, name: str, description: str, price: float, stock: int):
        self.id = item_id
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock
