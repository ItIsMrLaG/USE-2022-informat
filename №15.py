# Пример - с отрезками
'''
Найти наибольшую длину отрезка А, при которой формула всегда истинна.
'''
P = [3, 15]
Q = [14, 25]

def inside(x, l):
    return (l[0] <= x <= l[1])

def func1(x, A):
    return ((inside(x, P) == inside(x, Q)) <= (not (inside(x, A))))

k = 2
maximum = 0
for a in range(0, 35*k):
    for b in range(a, 35*k):
        A = [a/k, b/k]
        pofi = True
        for x in range(0, 31):
            if not(func1(x, A)):
                pofi = False
                break
        if pofi == True:
            dlin = A[1] - A[0]
            maximum = max(maximum, dlin)
print(maximum)

# Пример - с числами
'''
для какого наибольшего числа A функция всегда истинна 
'''

def func2(x, y, A):
    return (((x <= 5) <= (x**2 <= A)) and ((y**2 <= A) <= (y <= 5)))

maximum = 0
for A in range(70):
    pofi = True
    for x in range(70):
        for y in range(70):
            if not(func2(x, y, A)):
                pofi = False
    if pofi:
        maximum = max(maximum, A)
print(maximum)

# Пример - c множествами
'''
максимально возможное число элементов в A, при которых функция истинна 
'''

P = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
Q = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
Ans = []

def func3(A, x):
    return ((x in A) <= (x in P) or (not(x in Q) <= (not(x in A))))

for el in range(80):
    pofi = True
    hm = [el]
    for x in range(0, 80):
        if not(func3(hm, x)):
            pofi = False
            break
    if pofi:
        Ans.append(el)
print(len(Ans))

# Пример - c ДЕЛ
'''
максимально возможное число элементов в A, при которых функция истинна 
'''

def DEL(n, m):
    return ((n % m) == 0)

def func4(x, A):
    return (((not DEL(x, A)) and (DEL(x, 6))) <= (not DEL(x, 3)))

maximum = 0
for A in range(1, 500):
    pofi = True
    for x in range(500):
        if not func4(x, A):
            pofi = False
            break
    if pofi:
        maximum = max(maximum, A)
print(maximum)

# Пример - c побитовой конъюнкцией
'''
максимально возможное число элементов в A, при которых функция истинна 
'''

def func5(x, A):
    return (x&A != 0) <= (((x&17 == 0) and (x&5 == 0)) <= (x&3 != 0))

maximum = 0
for A in range(0, 500):
    pofi = True
    for x in range(0, 1000):
        if not func5(x, A):
            pofi = False
            break
    if pofi == True:
        maximum = max(A, maximum)
print(maximum)
