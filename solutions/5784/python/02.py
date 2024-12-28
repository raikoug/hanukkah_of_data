from pathlib import Path
import sys
from typing import List
day = int(Path(__file__).stem )
year = int(Path(__file__).parent.parent.stem)
sys.path.append(f"{Path(__file__).parent.parent.parent.parent.absolute()}")
from python_hod import HOD, Customer

def solve(hod: HOD) -> Customer:
    for customer in hod.customers:
        if customer.initials == "JP":
            orders: List[Order] = hod.get_orders_from_customer_id(customer.customerid)
            bagel = False
            coffee = False
            for order in orders:
                for item in order.items:
                    if "bagel" in item.sku_item.desc.lower():
                        bagel = True
                    if "coffee" in item.sku_item.desc.lower():
                        coffee = True
            if bagel and coffee:
                return customer