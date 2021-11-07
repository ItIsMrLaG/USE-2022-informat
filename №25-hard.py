from itertools import combinations

"""
Напишите прогу, которая ищет на отрезке [12345, 12425] числа, в состав которых входит полиндром

пример:
в диапазоне (1000, 1012):
1001 1001
1008 252
1010 505
"""

def finder(n):
    ans = [1]
    while n > 1:
        for i in range(2, n + 1):
            if n%i == 0:
                ans.append(i)
                n = n//i
                break
    return ans

def seed (l):
    polin = []
    helper = 1
    for i in range(len(l), 1, -1):
        for el in combinations(l, r=i):
            for j in el:
                helper = helper*j
            s = str(helper)
            ss = s[::-1]
            if (s == ss) and (len(s) != 1):
                polin.append(helper)
            helper = 1
    if len(polin) > 0:
        return max(polin)
    else:
        return False

for i in range(12345, 12425):
    pol = seed((finder(i)))
    if pol != 0:
        print(i, pol, end=', ')
