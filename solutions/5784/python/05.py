from pathlib import Path
import sys


day = int(Path(__file__).stem )
year = int(Path(__file__).parent.parent.stem)
sys.path.append(f"{Path(__file__).parent.parent.parent.parent.absolute()}")
from python_hod import HOD, Customer, Order

def solve(hod: HOD) -> Customer:    
    def senior_cat_items(order: Order) -> int:
        return len([item for item in order.items if "Senior Cat" in item.sku_item.desc ])
    
    best_senior_cat_items = 0
    best_serionr_cat_customer = None
    for customer in hod.customers:
        tmp_senior_cat_items = 0
        orders = hod.get_orders_from_customer_id(customer.customerid)
        for order in orders:
            tmp_senior_cat_items += senior_cat_items(order)
        
        if tmp_senior_cat_items > best_senior_cat_items:
            print(f"New best: {tmp_senior_cat_items} for {customer.customerid} from {customer.}")
            best_senior_cat_items = tmp_senior_cat_items
            best_serionr_cat_customer = customer
    
    return best_serionr_cat_customer