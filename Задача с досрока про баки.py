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
        Поставить завод в рандомное место, высчитать для этого места стоимость (sigma[0]), а потом пересчитывать 
    новую sigma для нового места, опираясь на старую sigma[0] и префиксные суммы (посчитанные заранее)  
    '''
    with open(file, 'r') as f:
        dlin = len(f.readlines())
        f.seek(0)
        P = []
        sigma = [0]
        info = []
        All = 0
        z = dlin // 2
        ans, cost = 0, 1000000000000000000000000000
        for i in range(dlin):
            num = int(f.readline())
            All += num
            P.append(All)
            info.append(num)
            if i > z:
                sigma[0] += num * (z - i % z)
            else:
                sigma[0] += num * i

        t = z
        for i in range(1, dlin):
            dop = P[t % dlin] - P[(t - z) % dlin]
            x = dop // abs(dop)
            si = sigma[-1] + x * All - 2 * (dop)
            sigma.append(si)
            if si < cost:
                cost = si
                ans = i
            t += 1
        return ans + 1, info[ans], cost

print(optima('/home/gora/PycharmProjects/USE-2022-informat/USE-2022-informat/test_sets/tester.txt'))
