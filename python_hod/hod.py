from pathlib import Path
import csv
from typing import List, Dict
from dataclasses import dataclass
from datetime import datetime
from .customers import Customer
from .product import Product
from .orders import Order, OrderItem

class Sku(int):
    pass

class HOD:
    data_folder: Path
    customer_file: Path
    customers_dict: dict
    customers: List[Customer]
    products: Dict[Sku,Product]
    orders: Dict[int,Order]
    order_items: List[OrderItem]
    
    def __init__(self, year):
        self.data_folder = Path(__file__).parent.parent / "data" / f"{year}"
        self.customer_file = self.data_folder / "noahs-customers.csv"
        self.order_items_file = self.data_folder / "noahs-orders_items.csv"
        self.orders_file = self.data_folder / "noahs-orders.csv"
        self.product_file = self.data_folder / "noahs-products.csv"
        self.products : Dict[Sku,Product] = dict()
        self.customers : List[Customer] = list()
        self.orders : Dict[int,Order] = dict()
        self.order_items : List[OrderItem] = list()
        
        self.get_customers()
        self.get_products()
        self.get_orders()
        self.get_order_items()
        
        
    def get_customer_dict(self) -> dict:
        customer_dict = {}
        with open(self.customer_file, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                customer_id = row['customerid']
                customer_dict[customer_id] = row
        return customer_dict
    
    def get_customers(self) -> List[Customer]:
        self.customers_dict: Dict[int, dict] = self.get_customer_dict()
        self.customers: List[Customer] = list()
        for customer in self.customers_dict.values():
            self.customers.append(Customer(
                customerid = int(customer.get("customerid", 0)),
                full_name = customer.get("name",""),
                first_name = customer.get("name","").split(" ")[0],
                surname = customer.get("name","").split(" ")[1],
                initials= "".join([el[0] for el in customer.get("name","").split(" ")]),
                address = customer.get("address",""),
                citystatezip = customer.get("citystatezip",""),
                birthdate = datetime.strptime( customer.get("birthdate","1989-01-16"), "%Y-%m-%d"),
                phone = customer.get("phone",""),
                timezone = customer.get("timezone",""),
                lat = customer.get("lat",""),
                long = customer.get("long","")

            ))
    
    def get_product_dict(self) -> dict:
        product_dict = dict()
        with open(self.product_file, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                sku = row['sku']
                product_dict[sku] = row
        return product_dict
    
    def get_products(self):
        product_dict: Dict[str, dict] = self.get_product_dict()
        self.products: Dict[Sku,Product] = dict()
        for product in product_dict.values():
            # 
            # sku
            # desc
            # wholesale_cost
            # dims_cm
            # 
            
            sku = product.get("sku","")
            self.products[sku] = Product(
                sku = sku,
                desc = product.get("desc",""),
                wholesale_cost = float(product.get("wholesale_cost",0.0)),
                dims_cm = product.get("dims_cm","0.0|0.0|0.0")
            )
                    
    def get_order_dict(self) -> dict:
        order_dict = dict()
        with open(self.orders_file, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                
                    # orderid: int
                    # customerid: int
                    # ordered: datetime
                    # shipped: datetime
                    # items: Optional[List[OrderItem]]
                    # total: float
                order_id = row['orderid']
                order_dict[order_id] = row
                
        return order_dict
    
    def get_orders(self):
        order_dict: Dict[int, dict] = self.get_order_dict()
        self.orders: Dict[str,Order] = dict()
        for order in order_dict.values():
            orderid = int(order.get("orderid",0))
            self.orders[orderid] = Order(
                orderid = orderid,
                customerid = int(order.get("customerid",0)),
                ordered = order.get("ordered","1989-01-16 00:00:00"),
                shipped = order.get("shipped","1989-01-16 00:00:00"),
                items = list(),
                total = float(order.get("total",0.0))
                
                )
    
    def get_order_item_dict(self) -> dict:
        order_item_dict: dict = dict()
        with open(self.order_items_file, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                order_id = int(row['orderid'])
                if order_id not in order_item_dict:
                    order_item_dict[order_id] = []
                order_item_dict[order_id].append(row)
        return order_item_dict
    
    def get_order_items(self):
        order_item_dict: Dict[int, List[dict]] = self.get_order_item_dict()
        self.order_items: List[OrderItem] = list()
        for order_id, items in order_item_dict.items():
            for item in items:
                
                # orderid: int
                # sku: str
                # qty: int
                # unit_price: float
                # sku_item: Optional['Product'] = None
                
                order_item = OrderItem(
                    orderid = int(item.get("orderid",0)),
                    sku = item.get("sku",""),
                    qty = int(item.get("qty",0)),
                    unit_price = float(item.get("unit_price",0.0)),
                    sku_item = self.products.get(item.get("sku",""),None)
                )
                self.order_items.append(order_item)
                self.orders[order_id].items.append(order_item)
    
    def get_orders_from_customer_id(self, customer_id: int) -> List[Order]:
        return [order for order in self.orders.values() if order.customerid == customer_id]
                
    
    
if __name__ == "__main__":
    hod = HOD(5784)
    print(f"data_folder -> {hod.data_folder}")
    res = hod.get_customer_dict()
    