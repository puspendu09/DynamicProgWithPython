from item import Item
from phone import Phone

item1 = Phone("phone", 100, 6)

item1.send_mail()
item1.apply_increment(.3)
print(item1.price)
