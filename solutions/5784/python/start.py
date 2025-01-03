from pathlib import Path
import sys
import importlib

solve_01 = importlib.import_module(f"01").solve
solve_02 = importlib.import_module(f"02").solve
solve_03 = importlib.import_module(f"03").solve
solve_04 = importlib.import_module(f"04").solve
solve_05 = importlib.import_module(f"05").solve
solve_06 = importlib.import_module(f"06").solve
solve_07 = importlib.import_module(f"07").solve
solve_08 = importlib.import_module(f"08").solve

year = int(Path(__file__).parent.parent.stem)
sys.path.append(f"{Path(__file__).parent.parent.parent.parent.absolute()}")
from python_hod import HOD, Customer
hod = HOD(year)

# day_01: Customer = solve_01(hod)
# print(f"Day 01: {day_01.phone}")
# day_02: Customer = solve_02(hod)
# print(f"Day 02: {day_02.phone}")
# day_03: Customer = solve_03(hod, day_02)
# print(f"Day 03: {day_03.phone}")
# day_04: Customer = solve_04(hod)
# print(f"Day 04: {day_04.phone}")
# day_05: Customer = solve_05(hod)
# # print(f"Day 05: {day_05.phone}")
# day_06: Customer = solve_06(hod)
# print(f"Day 06: {day_06.phone}")
# day_07: Customer = solve_07(hod, day_06)
# print(f"Day 07: {day_07.phone}")
day_08: Customer = solve_08(hod)
print(f"Day 08: {day_08.phone}")