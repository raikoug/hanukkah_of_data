from dataclasses import dataclass

@dataclass
class Product:
    sku: str
    desc: str
    wholesale_cost: float
    dims_cm: str

    def __post_init__(self):
        # Convert dims_cm from string to a tuple of floats
        self.dims_cm = tuple(map(float, self.dims_cm.split('|')))