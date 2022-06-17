# 'Алгоритм Евклида' + 'Основная Теорема арифметики'

##################################################################################################################
# url - https://www.youtube.com/watch?v=iVaMZVRMX4M

# @1_Вводная часть
"""
[a/b] --> [a = b*n + r]
> 'a' - делимое
> 'b' - делитель
> 'n' - частное
> 'r' - остаток
* в этом случае 'r' принадлежит множеству - [0, 1, ... , b-1]
* всего b остатков
* НОД - наибольший общий делитель {НОД(4, 8) == 4}
* НОК - наименьшее общее кратное  {НОK[4, 8] == 16}
"""
# @2_Основная Теорема арифметики:
"""
[a = (p1**l1) * (p2**l2) * ... * (pn**ln)]
> a - любое число 
> p1-n - любые простые числа 
простое число - число, которое имеет только два делителя (оно само и 1), (1 - не простое число) [2, 3, 5, 7, 11...] 
> l1-n - степени 

# пример - (180 = 2**2 * 3**2 * 5**1)

# вытаскивание НОД и НОК из этой теоремы #

# > a == 2**2 * 3**1 * 5**3 * 11*1
# > a == 2**1 * 3**2 * 5**1 * 13*1

# НОД(a,b) == 2**1 * 3**1 * 5**1
# НОК(a,b) == 2**2 * 3**2 * 5**3 * 11*1 * 13*1 
"""
# @3_Интересный вывод из предыдущего пункта:
"""
> x;y - числа 
> t - НОД(x;y)
> s - любое число
факт, что - если s является общим делителем для (x;y), то s является делителем для t (t % s == 0)
// так происходит, потому что НОД (t) является произведением максимального набора простых чисел, которые входят 
// в (x;y)
"""
# @4__Доказательство алгоритма Евклида (Euq_slow):
"""
> НОД(a;b) - x
> НОД(a-b;b) - y 
> a;b - любые числа
докажем что: НОД(a;b) =? НОД(a-+b;b)

1.[для этого случая "x - НОД; у - просто общий делитель"] (a % x == 0) и (b % x == 0),  
так как х - их НОД --> (( a-+ b) % x == 0) && (b % x == 0)--> (x % y == 0), 
так как "x" - НОД по условию, для левой части; а "y" является делителем. 
ВЫВОД_1: (x / y == 1) - для правой части

2.[для этого случая "у - НОД; х - просто общий делитель"] (( a-+ b) % y == 0) и (b % y == 0) --> 
(a % y == 0) и (b % y == 0) -->  (a % x == 0) и (b % x == 0) --> так как "у" - НОД по условию, для правой части; 
а "х" является делителем. 
ВЫВОД_2: (у / х == 1) - для правой части

3. Первый и второй вывод существуют в единой системе --> (x == y) --> НОД(a;b) == НОД(a -+ b;b)
"""
# @5_Доказательство алгоритма Евклида (Euq_fast):
"""
докажем что: НОД(a;b) =? НОД(r;b) [все переменные, как из @1]
1. [a/b] --> [a = b*n + r] --> [r = a - b*n]
2. сольем, то что нам нужно доказать, с пунктом 1 -->  НОД(a;b) =? НОД((a - b*n);b)
ВЫВОД: НОД(a;b) == НОД((a - b*n); b), так как мы доказали это уже в '@4' (n - просто число, которое показывает, 
сколько раз 'b' вычиталось из 'a' --> технология не поменялась) 
"""
# @6_Факты, доказательства которых в видосе:
"""
1. (a * b) == НОК[a, b] * НОД[a, b]                       (50ая минута)
2. НОД(a * m, a * n) == a * НОД(m, n)                     (69ая минута)
3. НОД(m, n) == d --> НОД(m/n, n/d) == 1                  (60ая минута)
4. Если НОД(b, c) == 1 --> НОД(a * b, c) == НОД(a, c)     (70ая минута)
"""
# @7_Факториал:
"""
Факториал - обозначается с добавлением '!' - "число!"
[n! = 1*2*3*4*...*n]
* 99! == 99 * 98! (можно выносить последний множитель из факториала) 
* 1! = 1
* 0! = 1
"""
# @8_Найти количество натуральных делителей:
"""
Основываясь на основной теореме арифметики:
    [a = (p1**l1) * (p2**l2) * ... * (pn**ln)]
    N = (l1 + 1)(l2 + 1)*...*(ln + 1)
    N - число натуральных делителей в числе - a 
"""
# @9_Хардовая для понимания задача:
"""
> a = НОК[1, 2, 3, ..., 1000] 
> b = НОК[501, 502, ..., 1000]
Что больше, а или b ?
{ответ - a == b} (80ая минута)
"""
# @10_Оч крутая задачка (олимпиадная):
"""
(a) Придумайте три натуральных числа так, чтобы никакие два не делились друг
    на друга, но произведение любых двух делилось на оставшееся число.
(b) А существует ли 10 таких чисел?

:РЕШЕНИЕ:
a = A * B
b = B * C
c = C * A
"""


##################################################################################################################

# @Алгоритм Евклида (нахождение общего НОД для двух чисел)

def Euq_fast(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return (a + b)


def Euq_slow(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a - b
        else:
            b = b - a
    return (a + b)


a = 60
b = 539
print(Euq_fast(a, b))


# @ Решето Эратосфена

def eratosthenes_upgrade(n):  # n - число, до которого хотим найти простые числа
    sieve = list(range(n + 1))
    sieve[1] = 0  # без этой строки итоговый список будет содержать единицу
    for i in sieve:
        if i > 1:
            if i == 2:
                mult = 2
            else:
                mult = i - 1
            for j in range(mult * i, len(sieve), i):
                sieve[j] = 0
    return set(sieve)


print(eratosthenes_upgrade(8063))


def eratosthenes_fast(n):
    resheto = [1] * (n + 1)
    resheto[0:2] = 0, 0
    for i in range(2, int(n ** 0.5) + 1):
        for j in range(i * i, n + 1, i):
            resheto[j] = 0
    for i in range(n + 1):
        if resheto[i]:
            resheto[i] = i
    return set(resheto)


print(eratosthenes_fast(8063))


def eler(n):
    '''Функция Эйлера (вычисляет количество чисел от 1 до n-1, которые вместе с n взаимнопростые)'''
    counter = 0
    for i in range(1, n):
        if Euq_fast(n, i) == 1:
            counter += 1
    return counter
