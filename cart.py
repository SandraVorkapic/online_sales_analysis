
from product import Product

class Cart:
    def __init__(self):
        self.cart_items = []

    def add_to_cart(self, product):
        if isinstance(product, Product):
            self.cart_items.append(product)
            print(f"Proizvod '{product.name}' je dodat u korpu.")
        else:
            print("Možete dodati samo proizvode tipa Product.")

    def calculate_total(self):
        total = sum(item.price for item in self.cart_items)
        return total

    def display_cart(self):
        if not self.cart_items:
            print("Korpa je prazna.")
        else:
            print("Sadržaj korpe:")
            for item in self.cart_items:
                print(f"- {item.name} | Cena: {item.price} RSD")
            print(f"Ukupno za naplatu: {self.calculate_total()} RSD")
