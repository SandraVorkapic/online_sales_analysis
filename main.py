# main.py

from product import Product
from product_manager import ProductManager

# Kreiranje instance ProductManager
manager = ProductManager()

p1 = Product("Tablet", 45000, 3)
p2 = Product("Slušalice", 2500, 8)
p3 = Product("Web kamera", 5000, 6)
p4 = Product("Punjač", 2000, 7)


manager.add_product(p1)
manager.add_product(p2)
manager.add_product(p3)
manager.add_product(p4)
