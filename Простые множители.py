# Функция, позволяющая разбить число на простые множители
def finder_prime(n):
    if (n == 1) or (n == 2) or (n==3):
        return [n]
    l = []
    for de in range(1, int(n**0.5)+1):
        if n%de == 0:
            l.append(de)
        if len(l) > 1:
            return [*finder_prime(n//de)] + [*finder_prime(de)]
    if len(l) == 1:
        return [n]
print(finder_prime(277))