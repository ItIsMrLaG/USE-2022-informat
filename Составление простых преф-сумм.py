'''
Имеется набор данных, состоящий из положительных целых чисел 1 или 2.
Необходимо расположить числа в таком порядке, чтобы максимизировать число
сумм на всех префиксах последовательности, которые являются простыми числами.
Программа должна напечатать одно число — максимальное количество префиксных сумм,
которые являются простыми числами.

Входные данные:
Даны два входных файла (файл А и файл В), каждый из которых содержит в первой строке
одно целое число N (1 ≤ N ≤ 1000000) — количество чисел. Каждая из следующих N строк содержит
натуральное число 1 или 2.
Пример входного файла:
5
1
2
1
2
1
При таких исходных данных оптимально расположить числа следующим образом: 1 1 1 2 2 или 2 1 2 1 1.
Тогда префиксные суммы будут равны 1,2,3,5,7 или 2,3,5,6,7 соответственно. Ответ: 4.
В ответе укажите два числа: сначала значение для файла А, затем для файла B.
'''


def recheto(n):
    info = [1]*n
    for i in range(2, n):
        for j in range(i*2, n, i):
            info[j] = 0
    ans = []
    for i in range(2, n):
        if info[i]:
            ans.append(i)
    return ans

with open('/home/gora/PycharmProjects/USE-2022-informat/USE-2022-informat/test_sets/tester.txt', 'r') as f:

    """Идея в том, чтоб считать кол. двоек и едениц, а потом составлять из них суммы, сверяясь с решетом. 
        Причем пытаться сначала использовать все двойки, а только потом еденицы"""

    dlin = int(f.readline())
    prime = recheto(dlin*2)
    one = sum([1 for x in range(dlin) if int(f.readline()) == 1])
    two = dlin - one
    s, a = 0, 0
    counter = 0

    while (one + two) > 0:
        step_two = (prime[a] - s) // 2

        for st in range(step_two):
            if two - 1 >= 0:
                s += 2
                two -= 1
            else:
                break

        for so in range(prime[a] - s):
            if one - 1 >= 0:
                s += 1
                one -= 1
            else:
                break

        if s == prime[a]:
            counter += 1
            a += 1

print(counter)