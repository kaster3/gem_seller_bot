import math


def calculate_summ(quantity: int) -> int:
    result = 0
    # if 1000 < quantity < 5000:
    #     result = 35 + (quantity - 1000) * 0.033
    # if 5000 < quantity < 10000:
    #     result = 165 + (quantity - 5000) * 0.03
    # if 10000 < quantity < 25000:
    #     result = 300 + (quantity - 10000) * 0.027
    # if 25000 < quantity < 50000:
    #     result = 675 + (quantity - 25000) * 0.025
    # if 50000 < quantity < 100000:
    #     result = 1300 + (quantity - 50000) * 0.023
    # if 100000 < quantity:
    #     result = 2450 + (quantity - 100000) * 0.02
    print(quantity)
    if quantity == 1000:  # 35 рублей
        result = quantity * 0.035
    elif quantity < 5000:  # 150 рублей
        result = quantity * 0.033
    elif quantity < 10000:  # 270 рублей
        result = quantity * 0.030
    elif quantity < 25000:  # 625 рублей
        result = quantity * 0.027
    elif quantity <= 50000:  # 1250 рублей
        result = quantity * 0.025
    elif quantity >= 100000:  # 2000 рублей
        result = quantity * 0.020

    return math.floor(result)
