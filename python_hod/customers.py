from dataclasses import dataclass
from datetime import datetime

@dataclass
class Customer:
    customerid: int
    full_name: str
    first_name: str
    surname: str
    initials: str
    address: str
    citystatezip: str
    birthdate: datetime
    phone: str
    timezone: str
    lat: float
    long: float
    
    def __str__(self):
        res = ""
        res += "customerid: " + str(self.customerid) + " - full_name: " + str(self.full_name) + "\n"
        res += f"  {'first_name': <12}: " + str(self.first_name) + "\n"
        res += f"  {'surname': <12}: " + str(self.surname) + "\n"
        res += f"  {'address': <12}: " + str(self.address) + "\n"
        res += f"  {'citystatezip': <12}: " + str(self.citystatezip) + "\n"
        res += f"  {'birthdate': <12}: " + str(self.birthdate) + "\n"
        res += f"  {'phone': <12}: " + str(self.phone) + "\n"
        res += f"  {'timezone': <12}: " + str(self.timezone) + "\n"
        res += f"  {'lat': <12}: " + str(self.lat) + "\n"
        res += f"  {'long': <12}: " + str(self.long) + "\n"
        
        return res