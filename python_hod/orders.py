from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List
from .product import Product

@dataclass
class OrderItem:
    orderid: int
    sku: str
    qty: int
    unit_price: float
    sku_item: Optional['Product'] = None


@dataclass
class Order:
    orderid: int
    customerid: int
    ordered: datetime
    shipped: datetime
    items: Optional[List[OrderItem]]
    total: float

    def __post_init__(self):
        # Convert ordered and shipped from string to datetime
        self.ordered = datetime.strptime(self.ordered, '%Y-%m-%d %H:%M:%S')
        self.shipped = datetime.strptime(self.shipped, '%Y-%m-%d %H:%M:%S')

