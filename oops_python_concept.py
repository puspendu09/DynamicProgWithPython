import csv


class Item:  # this is class
    # class attribute
    pay_rate = 0.8  # pay rate after 20% discount
    all = []

    def __init__(self, name: str, price: float, qty: int = 0):  # this is constructor
        # run validation to received argument
        assert price >= 0, f"price {price} can't be  negative  for item {name}"
        assert qty >= 0, f"qty {qty}  of {name} can't be a negative value"

        # assign to self object
        self.name = name
        self.price = price
        self.qty = qty

        # Action to execute
        Item.all.append(self)

    def item_price(self):  # this is method
        return self.price * self.qty

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod  # declaration of class method
    def instantiate_from_csv(cls):
        with open('Item.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                qty=int(item.get('qty'))
            )

    @staticmethod
    def is_integer(num):

        # we will count out the float that sare point zero eg: 5.0,10.0
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):  # __repr__ means represent. It's used to convert object to a readable format
        return f"Item('{self.name}', {self.price}, {self.qty} )"


# item1 = Item("mobile", 100, 1)
# item2 = Item("laptop", 100, 1)
# item3 = Item("cable", 18, 5)
# item4 = Item("mouse", 50, 5)
# item5 = Item("keyboard", 75, 5)

# Item.instantiate_from_csv()
# print(Item.all)

print(Item.is_integer(7.0))
