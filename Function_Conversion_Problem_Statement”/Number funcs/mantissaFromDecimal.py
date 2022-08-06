def mantissaFromDecimal(a):
    if a >= 1:
        while a > 10:
            a /= 10
    elif a < 1:
        while a < 1:
            a *= 10
    return a