from pathlib import Path
import sys


day = int(Path(__file__).stem )
year = int(Path(__file__).parent.parent.stem)
sys.path.append(f"{Path(__file__).parent.parent.parent.parent.absolute()}")
from python_hod import HOD, Customer

def solve(hod: HOD) -> Customer:
    def find_t9(word: str, dynamic: bool = True) -> int:
        D = {
            "abc":  "2",
            "def":  "3",
            "ghi":  "4",
            "jkl":  "5",
            "mno":  "6",
            "pqrs": "7",
            "tuv":  "8",
            "wxyz": "9"
        }
        def get_static_n(letter: str) -> str:
            try:
                block = [el for el in D.keys() if letter in el][0]
                count = block.index(letter) + 1
                return D[block] * count
            except:
                print(f"Che lettera è?! {letter}")
        
        def get_dynamic_n(letter: str) -> str:
            try:
                block = [el for el in D.keys() if letter in el][0]
                return D[block]
            except:
                print(f"Che lettera è?! {letter}")
        
        if dynamic:
            get_n = get_dynamic_n
        else:
            get_n = get_static_n
        
        res = ""
        for letter in word:
            res += get_n(letter)
            
        return int(res)

    for customer in hod.customers:
        t9 = find_t9(customer.surname.lower())
        if t9 ==  int(customer.phone.replace("-", "")):
            return customer