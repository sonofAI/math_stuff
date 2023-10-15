# Pearson correlation coefficient (r)

def sigma_xy(x: list, y: list):
    # sigma(x*y)
    product = 0
    for i in range(len(x)):
        a = x[i] * y[i]
        product += a

    return product

def sigma_set_sq(numset: list):
    # sigma(x**2)
    sum = 0
    for i in numset:
        sum += i**2

    return sum

def pearson_cc(numset1, numset2):
    n = len(numset1)
    if len(numset2) != n:
        return 'cannot calculate pearson_cc for sets not same length'

    n1_sum = sum(numset1)
    n2_sum = sum(numset2)

    top = n * sigma_xy(numset1, numset2) - n1_sum * n2_sum
    bottom = (n * sigma_set_sq(numset1) - n1_sum**2) * (n * sigma_set_sq(numset2) - n2_sum**2)

    r = top / (bottom**0.5)
    return r




numset1 = [3, 8, -1]
numset2 = [-6, -16, 2]

print(pearson_cc(numset1, numset2))
