import math


def calculate_summ(quantity: int) -> int:
    result = 0

    if quantity == 1000:
        result = quantity * 0.035
    elif quantity < 5001:
        result = quantity * 0.033
    elif quantity < 10001:
        result = quantity * 0.030
    elif quantity < 25001:
        result = quantity * 0.027
    elif quantity < 50001:
        result = quantity * 0.025
    elif quantity < 100000:
        result = quantity * 0.023
    elif quantity >= 100000:
        result = quantity * 0.020

    return math.floor(result)
