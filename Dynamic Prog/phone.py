from item import Item


class Phone(Item):

    # all = []

    def __init__(self, name: str, price: float, qty: int = 0, broken_phones=0):
        super().__init__(
            name,
            price,
            qty
        )
        assert broken_phones >= 0, f"broken phone {broken_phones} is not equal or greater than zero"

        self.broken_phones = broken_phones

        # Action to execute
        # Phone.all.append(self)
