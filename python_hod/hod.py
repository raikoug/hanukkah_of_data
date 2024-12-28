from pathlib import Path
import csv
from typing import List

class HOD:
    def __init__(self, year):
        self.data_folder = Path(__file__).parent.parent / "data" / f"{year}"
        self.customer_file = self.data_folder / "noahs-customers.csv"
        
    def get_customer_dict(self) -> dict:
        customer_dict = {}
        with open(self.customer_file, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                customer_id = row['customerid']
                customer_dict[customer_id] = row
        return customer_dict
        
if __name__ == "__main__":
    hod = HOD(5784)
    print(f"data_folder -> {hod.data_folder}")
    res = hod.get_customer_dict()
    print(res.keys())