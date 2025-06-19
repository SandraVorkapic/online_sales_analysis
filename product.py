# product.py

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print(f"Proizvod: {self.name}")
        print(f"Cena: {self.price} RSD")
        print(f"Kolicina na stanju: {self.quantity}")

    def update_quantity(self, new_quantity):
        if new_quantity >= 0:
            self.quantity = new_quantity
            print(f"Kolicina za proizvod '{self.name}' je azurirana na {self.quantity}.")
        else:
            print("Greska: Kolicina ne moze biti negativna.")
