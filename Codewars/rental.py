def rental_car_cost(d):
    cost_per_day = 40

    if d >= 7:
        price = 50
    else:
        price = 20

        total_price = cost_per_day * d - price

rental_car_cost(4)
