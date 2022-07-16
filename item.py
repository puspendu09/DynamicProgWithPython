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
        self.__name = name
        self.__price = price
        self.qty = qty

        # Action to execute
        Item.all.append(self)

    @property
    def price(self):
        return self.__price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("your name is too long")
        else:
            self.__name = value

    def item_price(self):  # this is method
        return self.__price * self.qty

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value

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

    def __connect(self):
        pass

    def __body(self):
        pass

    def __title(self):
        pass

    def send_mail(self):
        print(f"mail sent{self.name}")

    def __repr__(self):  # __repr__ means represent. It's used to convert object to a readable format
        return f"{self.__class__.__name__}('{self.name}', {self.__price}, {self.qty} )"
