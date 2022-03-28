def no_numpy_mult(first, second):
    """
    param first: list of "size" lists, each contains "size" floats
    param second: list of "size" lists, each contains "size" floats
    """
    meta = len(first)
    f = []
    s = []
    for i in range(meta):
        f += first[i]
        s += second[i]
    result = []
    for a in range(meta):
        helper = []
        for b in range(meta):
            dop = 0
            for c in range(meta):
                one = meta*a + c
                two = (meta*c + b)
                dop += f[one]*s[two]
            helper.append(dop)
        result.append(helper)
    return result


a = [[1, 2, 4],
     [6, 3, 4],
     [7, 8, 9]]
b = [[1, 2, 4],
     [6, 3, 4],
     [7, 8, 9]]
print(no_numpy_mult(a, b))