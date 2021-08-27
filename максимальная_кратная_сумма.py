# Один из вариантов 27ого задания на ЕГЭ #
"""
Нужно найти максимальную сумму чисел кратную чему-нибудь (2, 3, 16.....) из двойной последовательности,
причем во время каждого передвижения наужно брать только одну цифру (движемся вниз по строчкам)
<<< ПРИМЕР >>>
:сумму кратную 3:
1  2  <-- выбрал (2)
4  5  <-- выбрал (5)
3  6  <-- выбрал (6)
8  3  <-- выбрал (8)
:ответ - (8 + 5 + 6 + 8) % 3 == 0:

<https://www.youtube.com/watch?v=qscUDmueDZs> - видео урок
"""

def max_multiples(multiplies: int, first: tuple or list, second: tuple or list) -> int:
    information = [0] * multiplies
    for i in range(len(first)):
        new = [-1000000] * multiplies
        for element in information:

            local_1 = first[i] + element
            index_1 = local_1 % multiplies
            if local_1 > information[index_1]:
                new[index_1] = local_1

            local_2 = second[i] + element
            index_2 = local_2 % multiplies
            if local_2 > information[index_2]:
                new[index_2] = local_2

        information = new
    print(information)
    return information[0]

first  = [1, 3, 7, 11,41, 4]
second = [2, 4, 11, 22, 48, 11]
d = 3
print(max_multiples(d, first, second))

