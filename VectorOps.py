def dot(a, b):
    if len(a) != len(b):
        raise ArithmeticError("Dot product of vectors with lengths" + str(len(a)) + " and " + str(len(b))
                              + " is undefined")
    dp = 0
    for i in range(len(a)):
        dp += a[i] * b[i]
    return dp


def add_vector(a, b):
    return [a[i] + b[i] for i in range(len(a))]
