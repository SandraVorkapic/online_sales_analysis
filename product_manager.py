# product_manager.py

from product import Product

class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        if isinstance(product, Product):
            self.products.append(product)
            print(f"Proizvod '{product.name}' je dodat u listu.")
        else:
            print("Greška: Možete dodati samo objekte klase Product.")

    def display_all_products(self):
        if not self.products:
            print("Nema proizvoda za prikaz.")
        else:
            print("Lista svih proizvoda:")
            for product in self.products:
                product.display_info()
                print("-" * 30)

    def total_value(self):
        ukupno = sum(p.price * p.quantity for p in self.products)
        print(f"Ukupna vrednost svih proizvoda: {ukupno} RSD")
        return ukupno
    
    def remove_product_by_name(self, name):
        for product in self.products:
            if product.name.lower() == name.lower():
                self.products.remove(product)
                print(f"Proizvod '{name}' je uklonjen iz liste.")
                return
        print(f"Proizvod '{name}' nije pronađen.")
