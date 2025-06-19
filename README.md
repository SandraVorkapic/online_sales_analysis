# Online Sales Analysis

Ovaj projekat je deo vežbe upravljanja verzijama i objektno-orijentisanog programiranja u Pythonu.  
Cilj je modelovanje jednostavnog sistema za analizu i upravljanje proizvodima i korpom kupca u online prodavnici.

---

## Funkcionalnosti

- Upravljanje proizvodima (dodavanje, prikaz, ažuriranje i uklanjanje)
- Upravljanje korpom kupca (dodavanje proizvoda, prikaz sadržaja, izračunavanje vrednosti)
- Verziona kontrola sa Git granama i spajanjem
- Sigurnost podataka putem `.gitignore`

---

## Klase i fajlovi

### `product.py`
**Klasa `Product`**  
Atributi: `name`, `price`, `quantity`  
Metodi:
- `display_info()`
- `update_quantity(new_quantity)`

---

### `product_manager.py`
**Klasa `ProductManager`**  
Atribut: lista proizvoda  
Metodi:
- `add_product(product)`
- `display_all_products()`
- `total_value()`
- `remove_product_by_name(name)`

---

### `cart.py`
**Klasa `Cart`**  
Atribut: lista proizvoda u korpi  
Metodi:
- `add_to_cart(product)`
- `calculate_total()`
- `display_cart()`

---

### `main.py`
- Kreira instance menadžera i korpe
- Dodaje proizvode
- Dodaje nasumične proizvode u korpu
- Prikazuje sadržaj korpe i ukupnu vrednost za naplatu

---

## `.gitignore`
- Ignoriše poverljive fajlove kao što je `config.json`
- Ignoriše sve snimke ekrana (*.png, *.jpg, itd.)

---

##  Pokretanje

Pokreni aplikaciju komandnom:
```bash
python main.py
