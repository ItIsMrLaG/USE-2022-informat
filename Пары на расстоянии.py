# №27 егэ прототип
'''
Посчитатть количество пар элементов последовательности из файла, сумма которых делится на 7,
произведение не кратно 15 и хотя-бы одно число из пары больше 50, находящиеся на расстоянии не меньше 8 элементов.

*Первое число - кол.элементов
'''

def creator(num_index, case=50):
    '''

    :param num_index: кратно чему должно быть
    :param case: больше какого числа
    :return: пустой трехмерный массив
    структура:
        [
            [                           # индекс от деления на num_index
                {'>50': 0, '<50': 0},   # отсутствие множителей 5 и 3 (пример)
                {'>50': 0, '<50': 0},   # есть множители 3, но нет 5  (пример)
                {'>50': 0, '<50': 0}    # есть множители 5, но нет 3  (пример)
            ]
        ]
    '''
    main = []
    for i in range(num_index):
        helper = []
        for j in range(3):
            helper.append({f'>{case}':0, f'<={case}': 0})
        main.append(helper)
    return main

def counter(my_file, line_len, case):
    '''
    :param my_file: имя файла
    :param line_len: длина очереди (...пары, не менее чем через 8 цифр...)
    :param case: число
    :return: число
    '''
    FIRST = 5                   # первый делитель
    SECOND = 3                  # второй делитель
    DELE = 7                    # кратность
    more = f">{case}"           # ">50"
    other = f"<={case}"         # "<=50"
    ans = 0
    line = []                   # очередь на свалку)
    info = creator(DELE)
    with open(my_file, 'r') as f:
        dlin = int(f.readline())

        for i in range(line_len - 1):
            # создание базовой очереди
            line.append(int(f.readline()))

        for i in range(dlin - (line_len - 1)):
            # считывание значение и добавление новой инфы в ответ ответа
            number = int(f.readline())
            index = number % DELE
            plus_index = (DELE - index) % DELE

            if not(number%FIRST == 0) and not(number%SECOND == 0):
                if number > 50:
                    for el in range(3):
                        ans+= info[plus_index][el][more] + info[plus_index][el][other]
                else:
                    for el in range(3):
                        ans+= info[plus_index][el][more]

            elif (number%FIRST == 0) and not(number%SECOND == 0):
                if number > 50:
                    for el in range(0, 3, 2):
                        ans+= info[plus_index][el][more] + info[plus_index][el][other]
                else:
                    for el in range(0, 3, 2):
                        ans += info[plus_index][el][more]

            elif not(number%FIRST == 0) and (number%SECOND == 0):
                if number > 50:
                    for el in range(2):
                        ans += info[plus_index][el][more] + info[plus_index][el][other]
                else:
                    for el in range(2):
                        ans += info[plus_index][el][more]

            # сдвиг очереди на один
            last = line[0]
            line.pop(0)
            line.append(number)
            append_ind = last % DELE

            # перезапись мета-инфы
            if not (last % FIRST == 0) and not (last % SECOND == 0):
                if last > 50:
                    info[append_ind][0][more] += 1
                else:
                    info[append_ind][0][other] += 1
            elif (last % FIRST == 0) and not (last % SECOND == 0):
                if last > 50:
                    info[append_ind][2][more] += 1
                else:
                    info[append_ind][2][other] += 1
            elif not (last % FIRST == 0) and (last % SECOND == 0):
                if last > 50:
                    info[append_ind][1][more] += 1
                else:
                    info[append_ind][1][other] += 1
    return ans

f = '/home/gora/PycharmProjects/USE-2022-informat/USE-2022-informat/test_sets/1-27-hard-26.11.txt'
print(counter(f, 8, 50))

###################################################################################################3

# О - ОПТИМИЗАЦИЯ

def IA_UMNIY(file):
    with open(file, 'r') as f:
        dlin = int(f.readline())
        meta = [[[0]*15 for y in range(7)] for x in range(2)] # [0] - <=50; [1] > 50;
        line = [int(f.readline()) for i in range(7)]
        ans = 0
        for i in range(dlin - 7):
            num = int(f.readline())
            ind = (7 - num % 7) % 7
            ans += sum([meta[1][ind][x] + meta[0][ind][x]*(num > 50) for x in range(15) if (num*x)%15 != 0])

            new = i%7
            hm = line[new]
            meta[hm > 50][hm%7][hm%15] += 1
            line[new] = num
        return ans

f = '/home/gora/PycharmProjects/USE-2022-informat/USE-2022-informat/test_sets/1-27-hard-26.11.txt'
print(IA_UMNIY(f))