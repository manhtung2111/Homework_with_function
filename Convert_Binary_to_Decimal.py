def binary_to_decimal(bin_num):
    if (bin_num == 0):
        return 0
    else:
        return round((bin_num % 10)) + 2 * binary_to_decimal(round(bin_num / 10))


print(binary_to_decimal(10101011))
