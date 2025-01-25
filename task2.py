def random_number_sum():
    import random
    num = random.randint(1, 999999)
    return sum(int(digit) for digit in str(num))


print(random_number_sum())
