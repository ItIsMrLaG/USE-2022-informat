'''
Идея: любую подпоследовательность подрядидущих чисел можно представить в виде -
(разности префиксных сумм)

>> префиксные суммы - суммы всех элементов от начала последовательности
'''

file_name = '/home/gora/PycharmProjects/USE-2022-informat/USE-2022-informat/test_sets/tester.txt'

def first(fl_nm=file_name):
    '''
    Задание - Найти МАКСИМАЛЬНУЮ сумму последовательности подрядидущих чисел
    Идея - чтоб получить максимальную сумму, из конечной суммы нужно вычесть минимальную префеиксную сумму
    '''
    with open(fl_nm, 'r') as f:
        dlin = int(f.readline())
        maxim = -1000000000000000000000000000000000000
        s = 0
        min_psm = 0
        for i in range(dlin):
            num = int(f.readline())
            s += num
            if (s - min_psm > maxim):
                maxim = s - min_psm
            if min_psm > s:
                min_psm = s
    return maxim

def second(fl_nm=file_name):
    '''
    Задание - Найти МИНИМАЛЬНУЮ сумму последовательности подрядидущих чисел
    Идея - чтоб получить минимальную сумму, надо найти максимальную сумму в "отзеркаленной последовательности",
    а потом записать ее со знаком минус
    '''
    with open(fl_nm, 'r') as f:
        dlin = int(f.readline())
        maxim = -1000000000000000000000000000000000000
        s = 0
        min_psm = 0
        for i in range(dlin):
            num = int(f.readline())
            num = -num
            s += num
            if (s - min_psm > maxim):
                maxim = s - min_psm
            if min_psm > s:
                min_psm = s
    return -maxim

def third(multiple=10, fl_nm=file_name):
    '''
    Задание - Найти МАКСИМАЛЬНУЮ сумму последовательности подрядидущих чисел кратную multiple
    Идея - чтоб получить максимальную кратную сумму надо вычесть минимальную префиксную сумму с таким же остатком.
    '''
    with open(fl_nm, 'r') as f:
        dlin = int(f.readline())
        min_prs = [1000000000000]*multiple
        min_prs[0] = 0
        maxim = -10000000000000000000
        s = 0

        for i in range(dlin):
            num = int(f.readline())
            s += num
            s_ind = s%multiple
            if (s - min_prs[s_ind]) > maxim:
                maxim = s - min_prs[s_ind]
            if s < min_prs[s_ind]:
                min_prs[s_ind] = s
        return maxim

def forth(multiple=10, fl_nm=file_name):
    '''
    Задание - Найти МАКСИМАЛЬНУЮ сумму последовательности подрядидущих чисел кратную multiple + посчитать длину цепочки,
    если таких цепочек несколько, выбрать самую длинную.
    Идея - использование range для подсчета кол. элементов
    '''
    with open(fl_nm, 'r') as f:
        dlin = int(f.readline())

        min_prs = [1000000000000] * multiple
        inds = [-10000] * multiple
        min_prs[0] = 0
        inds[0] = -1    #используюется из-за траблов с ренджем (идет не от еденицы, а от нуля)
        s = 0
        maxim = -10000000000000000000
        elem_dlin = 0

        for i in range(dlin):
            num = int(f.readline())
            s += num
            s_ind = s % multiple
            if (s - min_prs[s_ind]) > maxim:
                maxim = s - min_prs[s_ind]
                elem_dlin = i - inds[s_ind]

            if ((s - min_prs[s_ind]) == maxim) and (i - inds[s_ind] > elem_dlin):
                # отвечает за - "если таких цепочек несколько, выбрать самую длинную."
                elem_dlin = i - inds[s_ind]

            if s < min_prs[s_ind]:
                min_prs[s_ind] = s
                inds[s_ind] = i
        return maxim, elem_dlin

def fifth(multiple=10, fl_nm=file_name):
    '''
    Задание - Найти МАКСИМАЛЬНУЮ сумму последовательности подрядидущих чисел кратную multiple + посчитать длину цепочки,
    если таких цепочек несколько, выбрать самую короткую.
    Идея - (поменялись знаки в 131 and 135 по сравнению с forth())
    '''
    with open(fl_nm, 'r') as f:
        dlin = int(f.readline())

        min_prs = [1000000000000] * multiple
        inds = [-10000] * multiple
        min_prs[0] = 0
        inds[0] = -1    #используюется из-за траблов с ренджем (идет не от еденицы, а от нуля)
        s = 0
        maxim = -10000000000000000000
        elem_dlin = 0

        for i in range(dlin):
            num = int(f.readline())
            s += num
            s_ind = s % multiple
            if (s - min_prs[s_ind]) > maxim:
                maxim = s - min_prs[s_ind]
                elem_dlin = i - inds[s_ind]

            if ((s - min_prs[s_ind]) == maxim) and (i - inds[s_ind] < elem_dlin):
                # отвечает за - "если таких цепочек несколько, выбрать самую короткую."
                elem_dlin = i - inds[s_ind]

            if s <= min_prs[s_ind]:
                min_prs[s_ind] = s
                inds[s_ind] = i
        return maxim, elem_dlin

def sixth(count=30, fl_nm=file_name):
    '''
    Задание - Найти МАКСИМАЛЬНУЮ сумму последовательности подрядидущих чисел, кол четных, положительных элементов которой,
    кратно count
    Идея - сбор дополнительных метаданных, связанных с конкретными префиксными суммами.
    '''
    with open(fl_nm, 'r') as f:
        dlin = int(f.readline())

        min_prs = [1000000000000] * count
        min_prs[0] = 0
        s = 0
        maxim = -10000000000000000000
        kcp = 0      # кол. четных положительных элементов

        for i in range(dlin):
            num = int(f.readline())
            s += num
            if(num%2 and num>0):
                kcp += 1
            s_ind = kcp%count

            if (s - min_prs[s_ind]) > maxim:
                maxim = s - min_prs[s_ind]
            if s < min_prs[s_ind]:
                min_prs[s_ind] = s
    return maxim

def seventh(count=30, fl_nm=file_name):
    '''
    Задание - Найти МАКСИМАЛЬНУЮ сумму последовательности подрядидущих чисел, кол четных, положительных элементов которой,
    при %count == 5
    Идея - сбор дополнительных метаданных, связанных с конкретными префиксными суммами.
    '''
    with open(fl_nm, 'r') as f:
        dlin = int(f.readline())

        min_prs = [1000000000000] * count
        min_prs[0] = 0
        s = 0
        maxim = -10000000000000000000
        kcp = 0      # кол. четных положительных элементов

        for i in range(dlin):
            num = int(f.readline())
            s += num
            if(num%2 and num>0):
                kcp += 1
            s_ind = (kcp-5)%count   #####

            if (s - min_prs[s_ind]) > maxim:
                maxim = s - min_prs[s_ind]

            s_ind = kcp % count     #####
            if s < min_prs[s_ind]:
                min_prs[s_ind] = s
    return maxim

