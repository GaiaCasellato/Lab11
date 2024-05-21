from dataclasses import dataclass

@dataclass
class Product:
    Product_number : int
    Product_line : str
    Product_type : str
    Product : str
    Product_brand : str
    Product_color : str
    Unit_cost : float
    Unit_price : float

    @property
    def id(self):
        return self.Product_number

    def __str__(self):
        return f"Il tuo prodotto numero {self.Product_number} è {self.Product}"

    def __hash__(self):
        return hash(self.Product_number)