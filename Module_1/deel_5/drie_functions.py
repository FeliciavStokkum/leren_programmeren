from math import pi
from test_lib import *

# def calculate_cilinder_content(diameter, hoogte):
#     inhoud = (diameter/2) * (diameter/2) * pi * hoogte
#     afgeronde_inhoud = round(inhoud, 1)

#     diameter = 8.0
#     hoogte = 5.0
#     return afgeronde_inhoud

# resultaat = calculate_cilinder_content(8.0,5.0)
# print(resultaat)

# diameter = 8.0
# height = 5.0
# expect_content = 251.3
# calculated_content = calculate_cilinder_content(diameter,height)
# name = f'test diameter: {diameter} height: {height}'
# test(name, expect_content, calculated_content )

# report()
# # -------------------------------------------------------------------------

# def afronden_naar_5(bedrag):
#     AFRONDEN_CENTEN = 5
#     totaal = round(bedrag * 100 / AFRONDEN_CENTEN) * AFRONDEN_CENTEN / 100
#     return totaal

# bedrag = 23.4
# resultaat = afronden_naar_5(bedrag)
# print(resultaat)

# -----------------------------------------------------------------------------

month_discount_brands = 'Vespa,Kymco,Yamama'
MONTH_DISCOUNT_PERC = 10

def calc_discount(price: float, brand: str, month_discount_brands: str) -> float:
    if brand in month_discount_brands:
        discounted_price = round(price * MONTH_DISCOUNT_PERC / 100, 2)
        return discounted_price
    else:
        discounted_price = 0.0
        return discounted_price

result = calc_discount(100.0, "Vespa", month_discount_brands)
print(result)
        