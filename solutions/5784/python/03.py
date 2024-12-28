from pathlib import Path
import sys
from datetime import datetime

day = int(Path(__file__).stem )
year = int(Path(__file__).parent.parent.stem)
sys.path.append(f"{Path(__file__).parent.parent.parent.parent.absolute()}")
from python_hod import HOD, Customer

def solve(hod: HOD, prev: Customer) -> Customer:
    def is_rabbit_year(date: datetime):
        rabbit_years = [
            [datetime(year=1915, month=2, day=14), datetime(year=1916, month=2, day=2)],
            [datetime(year=1927, month=2, day=2), datetime(year=1928, month=1, day=22)],
            [datetime(year=1939, month=2, day=19), datetime(year=1940, month=2, day=7)],
            [datetime(year=1951, month=2, day=6), datetime(year=1952, month=1, day=26)],
            [datetime(year=1963, month=1, day=25), datetime(year=1964, month=2, day=12)],
            [datetime(year=1975, month=2, day=11), datetime(year=1976, month=1, day=30)],
            [datetime(year=1987, month=1, day=29), datetime(year=1988, month=2, day=16)],
            [datetime(year=1999, month=2, day=16), datetime(year=2000, month=2, day=4)],
            [datetime(year=2011, month=2, day=3), datetime(year=2012, month=1, day=22)],
            [datetime(year=2023, month=1, day=22), datetime(year=2024, month=2, day=9)]
        ]
        for start, end in rabbit_years:
            if start <= date <= end:
                return True
        return False
    
    def is_cancer(date: datetime):
        # between June 21 - July 22
        return datetime(year=date.year, month=6, day=21) <= date <= datetime(year=date.year, month=7, day=22)
    
    def same_citystatezip(customer1: Customer, customer2: Customer):
        return customer1.citystatezip == customer2.citystatezip
    
    for costumer in hod.customers:
        if is_rabbit_year(costumer.birthdate) and \
            is_cancer(costumer.birthdate) and \
            same_citystatezip(costumer, prev) and \
            len(hod.get_orders_from_customer_id(costumer.customerid)) > 0:
            return costumer
            