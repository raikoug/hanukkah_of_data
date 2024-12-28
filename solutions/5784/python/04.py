from pathlib import Path
import sys


day = int(Path(__file__).stem )
year = int(Path(__file__).parent.parent.stem)
sys.path.append(f"{Path(__file__).parent.parent.parent.parent.absolute()}")
from python_hod import HOD, Customer, Order

def solve(hod: HOD) -> Customer:
    def order_is_between_4am_5am(order: Order) -> bool:
        return order.ordered.hour == 4
    
    def order_is_bakery(order: Order) -> bool:
        for item in order.items:
            if "BKY" in item.sku_item.sku:
                return True
        return False
    
    best_customer = None
    best_orders = 0
    for customer in hod.customers:
        orders = hod.get_orders_from_customer_id(customer.customerid)
        if len(orders) < 150:
            continue
        
        tmp_good_orders: int = 0
        for order in orders:
            if order_is_between_4am_5am(order):
                if order_is_bakery(order):
                    tmp_good_orders += 1
        
        if tmp_good_orders > best_orders:
            best_orders = tmp_good_orders
            best_customer = customer

    
    return best_customer
        