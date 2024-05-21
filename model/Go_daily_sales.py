import datetime
from dataclasses import dataclass

@dataclass
class Sale:
    Date : datetime.time
    Order_method_code : int
    Product_number : int
    Quantity : int
    Retailer_code: int
    Unit_price: float
    Unit_sale_price : float

    @property
    def id(self):
        return self.Retailer_code

    def __str__(self):
        return f"{self.Retailer_code} "

    def __hash__(self):
        return hash(self.Retailer_code)