from functools  import lru_cache
# №1
'''
Возведение в степень через рекурсию, без использования циклов
'''
def khm(a, n = 0):
    if n == 1:
        return a
    if n == 0:
        return 1
    if n%2 == 0:
        return a*khm(a, n-1)
    if n%2 != 0:
        helper = khm(a, n//2)
        return a*helper**2


# №2
'''
У исполнителя есть команды: 
1) *2
2) *2 + 1
Сколько различных результатов можно получить из исходного числа 1 после выполнения программы, содержащей 9 команд?
'''

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


# №3
'''
У исполнителя есть команды: 
1) *2
2) *2 + 1
Сколько существует программ, для которых при исходном числе 1 результатом является число 41?
'''
def func6(first, second):
    if first == second:
        return 1
    elif first > second:
        return 0
    else:
        return func6(first * 3, second) + func6(first + 2, second)

print(func6(1, 41))


# №4
'''
У исполнителя есть команды: 
1) +1
2) +4
3) *4
Сколько существует программ, для которых при исходном числе 3 результатом является число 27 и при этом троектория 
содержит число 11?
'''
# -----v1-----
@lru_cache(None)
def func7(n=3, first=27, flag=False):
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

# -----v2-----
def func8(n=3, first=27, flag=False):
    Flag = flag
    if n == 11:
        Flag = True
    if n == first and Flag:
        return 1
    elif n < first:
        return func8(n + 1, first, Flag) + func8(n + 4, first, Flag) + func8(n*4, first, Flag)
    else:
        return 0

print(func8(3, 27)) #665

# Здесь показана фишка задания сверху
# s = set()
# l = list()
# for a in [' + 1)', ' + 4)', '*4)']:
#     for b in [' + 1)', ' + 4)', '*4)']:
#         n = '((3' + a + b
#         s.add(eval(n))
#         l.append(eval(n))
# print(*l)
# print(*s)

