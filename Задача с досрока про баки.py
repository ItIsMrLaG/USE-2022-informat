# ДОСРОК 2022
"""
    В городе М расположена кольцевая дорога длинной в N километров с движением в обе стороны.
На каждом километре автодороги расположен контейнер для мусора определенного объема.
    Стоимость транспортировки мусора = расстояние от базы * массу мусора (из контейнера, который стоит прямо в точке -
бесплатно, из соседних - 1 * количество мусора, через один - 2 * количество мусора ...)
    Рядом с каким контейнером надо поставить завод, чтоб стоимость транспортировки мусора от остальных баков была
минимальной.
(кол. баков - четно)
ПРИМЕР:
8
20
5
13
7
19

ОТВЕТ: 19
"""


def optima(f: str = r"/home/gora/PycharmProjects/USE-2022-informat/USE-2022-informat/test_sets/tester.txt"):
    file = f
    '''
    Идея:
        Поставить завод в рандомное место, высчитать для этого места стоимость (sigma0), а потом пересчитывать 
    новую sigma для нового места, опираясь на старую sigma0 и префиксные суммы (посчитанные заранее)  
    '''
    with open(file, 'r') as f:
        dlin = len(f.readlines())
        f.seek(0)
        info = []
        meta, ans = 10000000000000000, 0
        P = []
        sigma = 0
        helper_s = 0
        for i in range(dlin):
            num = int(f.readline())
            helper_s += num
            P.append(helper_s)
            if i <= dlin // 2:
                sigma += num * i
            else:
                sigma += num * (dlin - i)
            info.append(num)

        ind = dlin // 2
        for i in range(dlin):
            k = P[ind % dlin] - P[i]

            if k == 0:
                print('HA LOX, DUMAI KAK PEREDELAT')

            sigma = sigma + P[-1] * (k // abs(k))
            if meta > sigma:
                meta = sigma
                ans = i
            ind += 1
        return info[ans]

print(optima())
