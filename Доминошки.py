# На столе выложили цепочку из N   костяшек по принципу домино. Под костяшкой понимается пара любых неотрицательных
# чисел, каждое не превышает 100. В наборе могут быть одинаковые костяшки. Переставлять местами костяшки нельзя,
# но можно поворачивать любое количество костяшек, получая, например, из костяшки 1-2 костяшку 2-1.
# Определите максимальную длину цепочки костяшек домино, которую можно получить с помощью переворачиваний.
# Под цепочкой понимается последовательность костяшек, в которой второе число первой костяшки равно первому числу второй.
#
# Входные данные
# Дан входной файл, он содержит в первой строке количество пар N(1 ≤ N ≤ 100000).
# Каждая из следующих N строк содержит два натуральных числа, не превышающих 100.
# В ответе укажите одно число: искомое значение для файла.


def domino_my(file: str = '/home/gora/PycharmProjects/USE-2022-informat/USE-2022-informat/test_sets/tester.txt'):
    '''
        Задача - на вход подается количество подряд идущих доминошек, менять местами их нельзя, но можно поворачивать
     [2|3] или [3|2]. Надо найти максимальную последовательность из связанных доминошек. ([3|2][2|3])

     ПРИМЕР:
     1 2
     2 1
     1 2
     1 3
    :return: число доминошек, которое можно составить в одну цепочку
    '''
    with open(file, 'r') as f:
        n = int(f.readline())
        first = list(map(int, f.readline().split(' ')))
        counter_with, now_counter, ans = 1, 1, 1
        for i in range(n-1):
            second = list(map(int, f.readline().split(' ')))
            if first == second:
                counter_with += 1
                now_counter += 1
                first = second[::-1]
            elif first == second[::-1]:
                counter_with += 1
                now_counter += 1
                first = second
            else:
                if first[1] == second[0]:
                    now_counter += 1
                    first = second
                elif first[1] == second[1]:
                    now_counter += 1
                    first = second[::-1]
                elif first[0] == second[0]:
                    ans = max(now_counter, ans)
                    now_counter = counter_with + 1
                    first = second
                elif first[0] == second[1]:
                    ans = max(now_counter, ans)
                    now_counter = counter_with + 1
                    first = second[::-1]
                else:
                    ans = max(now_counter, ans)
                    first = second
                    now_counter = 1
                counter_with = 1
        return max(now_counter, ans)


def domino_AR(file: str = '/home/gora/PycharmProjects/USE-2022-informat/USE-2022-informat/test_sets/tester.txt'):
    '''
            Задача - на вход подается количество подряд идущих доминошек, менять местами их нельзя, но можно поворачивать
         [2|3] или [3|2]. Надо найти максимальную последовательность из связанных доминошек. ([3|2][2|3])

         ПРИМЕР:
         1 2
         2 1
         1 2
         1 3
        :return: число доминошек, которое можно составить в одну цепочку
        '''
    with open(file, 'r') as f:
        n = int(f.readline())
        first = list(map(int, f.readline().split(' ')))
        ans, ct1, ct2 = 1, 1, 1
        for i in range(n - 1):
            second = list(map(int, f.readline().strip().split(' ')))

            last_ct1, last_ct2 = ct1, ct2
            ct1, ct2 = 1, 1

            if first[0] == second[0]:
                ct1 = last_ct2 + 1
            if first[0] == second[1]:
                ct2 = last_ct2 + 1

            if first[1] == second[0]:
                ct1 = last_ct1 + 1
            if first[1] == second[1]:
                ct2 = last_ct1 + 1

            ans = max(ans, ct1, ct2)

            first = second
    return ans
