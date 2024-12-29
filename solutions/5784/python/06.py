from pathlib import Path
import sys


day = int(Path(__file__).stem )
year = int(Path(__file__).parent.parent.stem)
sys.path.append(f"{Path(__file__).parent.parent.parent.parent.absolute()}")
from python_hod import HOD, Customer

def solve(hod: HOD) -> Customer:
    
    best_discount = 0
    best_discount_customer = None
    
    for customer in hod.customers:
        tmp_discount = 0
        for order in hod.get_orders_from_customer_id(customer.customerid):
            noahs_cost = sum([item.qty * item.sku_item.wholesale_cost for item in order.items])
            tmp_discount += noahs_cost - order.total
        if tmp_discount > best_discount:
            best_discount = tmp_discount
            best_discount_customer = customer
        
    return best_discount_customer