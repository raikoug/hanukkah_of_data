from pathlib import Path
import sys
from typing import List, Tuple
from datetime import datetime


day = int(Path(__file__).stem )
year = int(Path(__file__).parent.parent.stem)
sys.path.append(f"{Path(__file__).parent.parent.parent.parent.absolute()}")
from python_hod import HOD, Customer, Order,OrderItem

def solve(hod: HOD, prev: Customer =None) -> Customer:
    if prev is None:
        prev = hod.customers[4167]
    def get_colored_items_in_orders(orders: List[Order])-> List[Tuple[OrderItem,Order]]:
        return [(item,order) for order in orders for item in order.items if "COL" in item.sku_item.sku]
    
    target_items: List[Tuple[OrderItem,Order]] = get_colored_items_in_orders(hod.get_orders_from_customer_id(prev.customerid))
    for item, order_date in target_items:
        same_date_orders = hod.get_orders_on_date(order_date.ordered.date() )
        for same_date_order in same_date_orders:
            if same_date_order.customerid == prev.customerid:
                continue
            for same_order_date_item in same_date_order.items:
                target_item_desc = item.sku_item.desc.split("(")[0]
                same_order_date_item_desc = same_order_date_item.sku_item.desc.split("(")[0]
                if target_item_desc == same_order_date_item_desc:
                    return hod.customers[same_date_order.customerid]

if __name__ == "__main__":
    hod = HOD(year)
    day_07: Customer = solve(hod)