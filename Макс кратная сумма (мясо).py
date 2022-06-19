"""
Шестиклассник Коля совсем недавно узнал, что такое НОД и НОК — наибольший общий делитель и наименьшее общее
кратное некоторого набора натуральных чисел. Ему так понравилась эта тема, поэтому он решил потренироваться и
в случайном порядке начал выписывать на доску от 2 до 10 натуральных чисел в строчку и попарно начал находить
для них НОКи. Его друг Ваня предложил Коле следующую задачу:
из каждой строки нужно выбрать один из НОКов, причем так, чтобы их сумма была наибольшей, а также кратна 8 или 11.
В ответе укажите два числа: сначала искомое значение для файла А, затем для файла B.

Формат входных данных:
Первая строка входных данных содержит число n — количество строк, 1 ≤ n ≤ 10^5.
Следующие n строк содержат натуральное число 2 ≤ k ≤ 10, обозначающее количество чисел в строке,
затем k натуральных чисел в этой строке.
Программа должна вывести целое число — максимальную сумму, кратную 8 или 11.

Пример:
4
2 8 6
3 2 7 8
2 6 5
4 7 3 8 6

Ответом для примера будет: 152
Рассмотрим пример из условия. Для указанных входных данных значения НОК
для первой строки — 24;
для второй строки — 14,8,56;
для третьей группы — 30;
для четвёртой группы — 6,21,24,24,42,56.
Значением искомой суммы должно быть число 152 (24+ 56+ 30+ 42).
"""


def euq(t):
    a, b = t
    while max(a, b) % min(a, b) != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return min(a, b)


def proga(f=r'/home/gora/PycharmProjects/USE-2022-informat/USE-2022-informat/test_sets/27B-32.txt'):
    with open(f, 'r') as f:
        dlin = int(f.readline())
        info = []
        meta11 = [-10000000] * 11
        meta8 = [-10000000] * 8
        meta8[0], meta11[0] = 0, 0
        for i in range(dlin):
            # преобразование входных данных в двумерный массив (строки[НОКИ])
            helper = list(map(int, f.readline().strip().split()))[1:]
            helper_s = []
            for a in range(len(helper)):
                for b in range(a + 1, len(helper)):
                    helper_s.append(helper[a] * helper[b] // euq((helper[a], helper[b])))
            info.append(list(set(helper_s)))
        for el in info:
            # для 11
            new11 = [-10000000] * 11
            for ind in range(len(el)):
                for i in range(11):
                    s_i = meta11[i] + el[ind]
                    ix_i = s_i % 11
                    new11[ix_i] = max(new11[ix_i], s_i)
            meta11 = new11
            # для 8
            new8 = [-10000000] * 8
            for ind in range(len(el)):
                for i in range(8):
                    s_i = meta8[i] + el[ind]
                    ix_i = s_i % 8
                    new8[ix_i] = max(new8[ix_i], s_i)
            meta8 = new8
        ans = max(meta8[0], meta11[0])
    return ans


print(proga())

'''
Имеется набор данных, состоящий из троек положительных целых чисел. 
Необходимо выбрать из каждой тройки ровно два числа так, 
чтобы сумма всех выбранных чисел оканчивалась либо на 3   
в семеричной записи, либо на 5   
в десятичной записи, но не оканчивалась на 3   
в семеричной записи и на 5   
в десятичной записи одновременно, и при этом была максимально возможной. 
Гарантируется, что искомую сумму получить можно.

Пример входного файла:
5
30 40 33 
22 28 38 
25 17 3 
35 9 14 
10 33 1

Ответ для данного примера: 265  
'''


def effect(fl='/home/gora/PycharmProjects/USE-2022-informat/USE-2022-informat/test_sets/tester.txt'):
    def translator(n, mult):
        t = n
        s = ''
        while t > 0:
            s = str(t % mult) + s
            t = t // mult
        return s

    with open(fl, 'r') as f:
        dlin = int(f.readline())
        ans = -100000000000000000000000
        meta7 = [0] * 7
        meta10 = [0] * 10
        for i in range(dlin):
            new = list(map(int, f.readline().strip().split()))
            helper7 = [-100000000000] * 7
            helper10 = [-100000000000] * 10
            for a in range(7):
                for el in new:
                    s = meta7[a] + sum(new) - el
                    if s < 0:
                        continue
                    s_i = int(translator(s, 7)[-1])
                    if helper7[s_i] < s:
                        helper7[s_i] = s
            meta7 = helper7

            for a in range(10):
                for el in new:
                    s = meta10[a] + sum(new) - el
                    s_i = int(s % 10)
                    if helper10[s_i] < s:
                        helper10[s_i] = s
            meta10 = helper10

    for el in meta7 + meta10:
        if (el%10 == 5) and ((translator(el, 7)[-1]) != '3'):
            ans = max(ans, el)
        if (el % 10 != 5) and ((translator(el, 7)[-1]) == '3'):
            ans = max(ans, el)
    return ans, meta10, meta7


print(effect())
