from pathlib import Path
import sys


day = int(Path(__file__).stem )
year = int(Path(__file__).parent.parent.stem)
sys.path.append(f"{Path(__file__).parent.parent.parent.parent.absolute()}")
from python_hod import HOD, Customer, Order

def solve(hod: HOD) -> Customer:
    best_noah_collection = 0
    best_noah_collection_customer = None
    
    def count_noah_items_in_order(order: Order) -> int:
        return sum([item.qty for item in order.items if "noah" in item.sku_item.desc.lower()])
    
    for costumer in hod.customers:
        tmp_noah_collection = 0
        orders = hod.get_orders_from_customer_id(costumer.customerid)
        for order in orders:
            tmp_noah_collection += count_noah_items_in_order(order)
        
        if tmp_noah_collection > best_noah_collection:
            best_noah_collection = tmp_noah_collection
            best_noah_collection_customer = costumer
        
    return best_noah_collection_customer
        