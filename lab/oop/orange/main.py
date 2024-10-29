from basket import Basket
from orange import Orange
from customer import Customer

basket = Basket("Sarayut Basket")
orange1 = Orange(0.5, "Suttun", "2022-10-9")
orange2 = Orange(0.4, "Holloway", "2022-10-11")
orange3 = Orange(0.3, "Oldham", "2022-10-8")

customer1 = Customer('Potter')
customer2 = Customer('Lupin')

# Adding oranges to the basket
basket.add_orange(orange1)
basket.add_orange(orange2)
basket.add_orange(orange3)

# Listing contents of the basket
print("Basket contents:")
for item in basket.list_contents():
    print(item)
