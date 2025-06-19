# main.py

from product import Product
from product_manager import ProductManager

# Kreiranje instance ProductManager
manager = ProductManager()

# Dodavanje nekoliko proizvoda
p1 = Product("Laptop", 85000, 2)
p2 = Product("Miš", 1500, 10)
p3 = Product("Tastatura", 3000, 5)
p4 = Product("Monitor", 25000, 3)

manager.add_product(p1)
manager.add_product(p2)
manager.add_product(p3)
manager.add_product(p4)

manager.display_all_products()

manager.total_value()

from cart import Cart


cart = Cart()

if len(manager.products) >= 3:
    cart.add_to_cart(manager.products[0])
    cart.add_to_cart(manager.products[1])
    cart.add_to_cart(manager.products[2])

cart.display_cart()
