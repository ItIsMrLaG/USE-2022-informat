# hard

# №10

def khm(a, n = 0):
    if n == 1:
        return a
    if n == 0:
        return 1
    if n%2 == 0:
        return a*khm(a, n-1)
    if n%2 != 0:
        return a*khm(a, n//2)*khm(a, n//2)

# №9
'''
У исполнителя есть команды: 
1) *2
2) *2 + 1
Сколько различных результатов можно получить из исходного числа 1 после выполнения программы, содержащей 9 команд?
'''
from functools  import lru_cache

ANS = 0

@lru_cache(1000)
def func9(n, first=1):
    global ANS
    if n == 0:
        ANS += 1
    else:
        func9(n-1, first*2)
        func9(n-1, first*2 + 1)

func9(9)
print(ANS) # 512


# №7
'''
У исполнителя есть команды: 
1) +1
2) +4
3) *4
Сколько существует программ, для которых при исходном числе 3 результатом является число 27 и при этом троектория 
содержит число 11?
'''
from functools  import lru_cache

@lru_cache(None)
def func7(n=3, first=27, flag = False):
    Flag1, Flag2, Flag3 = flag, flag, flag
    if n < first:
        if (n + 1) == 11:
            Flag1 = True
        if (n + 4) == 11:
            Flag2 = True
        if (n * 4) == 11:
            Flag3 = True
        return func7(n + 1, first, Flag1) + func7(n + 4, first, Flag2) + func7(n * 4, first, Flag3)
    elif n == first and Flag1:
        return 1
    else:
        return 0

print(func7(3, 27)) #665


# s = set()
# l = list()
# for a in [' + 1)', ' + 4)', '*4)']:
#     for b in [' + 1)', ' + 4)', '*4)']:
#         n = '((3' + a + b
#         s.add(eval(n))
#         l.append(eval(n))
# print(*l)
# print(*s)
