# №1
l = []
with open('/home/gora/PycharmProjects/USE-2022-informat/USE-2022-informat/test_sets/27_hard_a.txt', 'r') as f:
    dlin = int(f.readline())
    for el in range(dlin):
        a, b = map(int, f.readline().strip().split(' '))
        p = a*b
        if p == 0:
            continue
        if p%6 == 0:
            l.append(p)
    l.sort()
    if len(l) >= 5:
        for i in range(5):
            print(l[i], end=', ')
    elif len(l) > 0:
        for i in range(len(l)):
            print(l[i], end=', ')
        for i in range(5 - len(l)):
            print(10000000, end=', ')
    else:
        print(*['10000000, ']*5)

l.clear()

l = []
with open('/home/gora/PycharmProjects/USE-2022-informat/USE-2022-informat/test_sets/27_hard_b.txt', 'r') as f:
    dlin = int(f.readline())
    for el in range(dlin):
        a, b = map(int, f.readline().strip().split(' '))
        p = a*b
        if p == 0:
            continue
        if p%6 == 0:
            l.append(p)
    l.sort()
    # print(l)
    if len(l) >= 5:
        for i in range(5):
            print(l[i], end=', ')
    elif len(l) > 0:
        for i in range(len(l)):
            print(l[i], end=', ')
        for i in range(5 - len(l)):
            print(10000000, end=', ')
    else:
        print(*['10000000, ']*5)

# 58368, 60636, 325068, 367548, 579312, 96096, 96096, 102144, 102144, 122976

# №2
with open('/home/gora/PycharmProjects/USE-2022-informat/USE-2022-informat/test_sets/27_hard_b.txt', 'r') as f:
    dlin =int(f.readline())
    info = [0]*50
    for i in range(dlin):
        helper = [10000000000000]*50
        a, b = map(int, f.readline().strip().split(' '))
        for j in range(50):

            a_sum = info[j] + a
            a_ind = a_sum%50
            if a_sum < helper[a_ind]:
                helper[a_ind] = a_sum

            b_sum = info[j] + b
            b_ind = b_sum % 50
            if b_sum < helper[b_ind]:
                helper[b_ind] = b_sum

        info = helper
        print(info)
        print(i)
    info.pop(1)
    print(min(info))

# №3
with open('/home/gora/PycharmProjects/USE-2022-informat/USE-2022-informat/test_sets/27_hard_a.txt', 'r') as f:
    dlin = int(f.readline())
    info = [0]*100
    for i in range(dlin):
        a, b = map(int, f.readline().strip().split(' '))

        helper = [100000000000000]*100
        for j in range(100):

            a_sum = a + info[j]
            a_ind = a_sum%100
            if a_sum < helper[a_ind]:
                helper[a_ind] = a_sum

            b_sum = b + info[j]
            b_ind = b_sum%100
            if b_sum < helper[b_ind]:
                helper[b_ind] = b_sum

        info = helper
    info.pop(0)
    print(min(info))

# №4
with open('/home/gora/PycharmProjects/USE-2022-informat/USE-2022-informat/test_sets/tester.txt', 'r') as f:
    dlin = int(f.readline())
    info = [0]*3
    for i in range(dlin):
        helper = [-1000000000000000]*3
        a, b = map(int, f.readline().strip().split(' '))

        for j in range(3):

            a_sum = a + info[j]
            a_ind = a_sum%3
            if a_sum > helper[a_ind]:
                helper[a_ind] = a_sum

            b_sum = b + info[j]
            b_ind = b_sum % 3
            if b_sum > helper[b_ind]:
                helper[b_ind] = b_sum

        info = helper
    print(info[0])

# №5
with open('/home/gora/PycharmProjects/USE-2022-informat/USE-2022-informat/test_sets/27_hard_a.txt', 'r') as f:
    dlin = int(f.readline())
    info = [0]*17
    s = 0
    for i in range(dlin):
        a, b = map(int, f.readline().strip().split(' '))
        helper = [10000000000000000]*17
        for j in range(17):
            a_sum = a + info[j]
            a_ind = a_sum%17
            if a_sum < helper[a_ind]:
                helper[a_ind] = a_sum

            b_sum = b + info[j]
            b_ind = b_sum % 17
            if b_sum < helper[b_ind]:
                helper[b_ind] = b_sum

        info = helper
    print(info[0])

# №6
with open('/home/gora/PycharmProjects/USE-2022-informat/USE-2022-informat/test_sets/27_hard_b.txt', 'r') as f:
    dlin = int(f.readline())
    info = [0]*8
    for i in range(dlin):
        a, b = map(int, f.readline().strip().split(' '))
        helper = [-1000000000]*8

        for j in range(8):
            a_sum = info[j] + a
            a_ind = a_sum%8
            if a_sum > helper[a_ind]:
                helper[a_ind] = a_sum

            b_sum = info[j] + b
            b_ind = b_sum % 8
            if b_sum > helper[b_ind]:
                helper[b_ind] = b_sum
        info = helper
    l = []
    for el in range(1, 8, 2):
        l.append(info[el])
    print(max(l))

# №7
with open('/home/gora/PycharmProjects/USE-2022-informat/USE-2022-informat/test_sets/27_hard_b.txt', 'r') as f:
    dlin = int(f.readline())
    info = [0]*16
    for i in range(dlin):
        a, b = map(int, f.readline().strip().split(' '))
        helper = [-1000000000000]*16
        for j in range(16):
            a_sum = a + info[j]
            a_ind = a_sum%16
            if a_sum > helper[a_ind]:
                helper[a_ind] = a_sum

            b_sum = b + info[j]
            b_ind = b_sum % 16
            if b_sum > helper[b_ind]:
                helper[b_ind] = b_sum

        info = helper
    info.pop(10)
    info.pop(10)
    info.pop(10)
    print(max(info))