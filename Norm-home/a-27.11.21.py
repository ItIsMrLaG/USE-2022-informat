# №1

exemp = [
    [                           # индекс от деления на семь
        {'>50': 0, '<50': 0},   # отсутствие множителей 5 и 3
        {'>50': 0, '<50': 0},   # есть множители 3, но нет 5
        {'>50': 0, '<50': 0}    # есть множители 5, но нет 3
    ]
]


info = []
for i in range(7):
    helper = []
    for j in range(3):
        helper.append({'>50': 0, '<=50': 0})
    info.append(helper)

with open('/home/gora/PycharmProjects/USE-2022-informat/USE-2022-informat/test_sets/1-27-hard-26.11.txt', 'r') as f:
    dlin = int(f.readline())
    ans = 0
    line = []
    for i in range(7):
        line.append(int(f.readline()))
    for i in range(dlin - 7):
        print(line)
        num = int(f.readline())
        index = num % 7
        plus_index = (7 - index) % 7
        # print(num, index, plus_index)

        if not(num%5 == 0) and not(num%3 == 0):
            # print(num, '1')
            if num > 50:
                for el in range(3):
                    ans+= info[plus_index][el]['>50'] + info[plus_index][el]['<=50']
            else:
                for el in range(3):
                    ans+= info[plus_index][el]['>50']

        elif (num%5 == 0) and not(num%3 == 0):
            # print(num, '2')
            if num > 50:
                for el in range(0, 3, 2):
                    ans+= info[plus_index][el]['>50'] + info[plus_index][el]['<=50']
            else:
                for el in range(0, 3, 2):
                    ans += info[plus_index][el]['>50']

        elif not(num%5 == 0) and (num%3 == 0):
            # print(num, '3')
            if num > 50:
                for el in range(2):
                    ans += info[plus_index][el]['>50'] + info[plus_index][el]['<=50']
            else:
                for el in range(2):
                    ans += info[plus_index][el]['>50']

        last = line[0]
        line.pop(0)
        line.append(num)

        append_ind = last%7

        if not (last % 5 == 0) and not (last % 3 == 0):
            if last > 50:
                # print('none', last, '>')
                info[append_ind][0]['>50'] += 1
            else:
                # print('none', last, '<=')
                info[append_ind][0]['<=50'] += 1
        elif (last % 5 == 0) and not (last % 3 == 0):
            if last > 50:
                # print('not-3', last, '>')
                info[append_ind][2]['>50'] += 1
            else:
                # print('not-3', last, '<=')
                info[append_ind][2]['<=50'] += 1
        elif not (last % 5 == 0) and (last % 3 == 0):
            if last > 50:
                # print('not-5', last, '>')
                info[append_ind][1]['>50'] += 1
            else:
                # print('not-5', last, '<=')
                info[append_ind][1]['<=50'] += 1

print(ans)


# №2

info = []
for i in range(15):
    helper = []
    for j in range(4):
        helper.append({'>40':0, '<=40':0})
    info.append(helper)
# 0 - none all; 1 - none 3; 2 - none 2; 3 - all in

with open('/home/gora/PycharmProjects/USE-2022-informat/USE-2022-informat/test_sets/2-27-hard-26.11.txt', 'r') as f:
    dlin = int(f.readline())
    ans = 0
    line = []
    for i in range(8):
        line.append(int(f.readline()))
    for i in range(dlin - 8):
        number = int(f.readline())
        index = number%15
        none_index = (15 - index)%15

        if number%6 == 0:
            if number > 40:
                for el in range(15):
                    if el != none_index:
                        for j in range(4):
                            ans += info[el][j]['>40'] + info[el][j]['<=40']
            else:
                for el in range(15):
                    if el != none_index:
                        for j in range(4):
                            ans += info[el][j]['>40']

        elif (number%3==0) and not(number%2==0):
            if number > 40:
                for el in range(15):
                    if el != none_index:
                        for j in range(1,4,2):
                            ans += info[el][j]['>40'] + info[el][j]['<=40']
            else:
                for el in range(15):
                    if el != none_index:
                        for j in range(1, 4, 2):
                            ans += info[el][j]['>40']

        elif not(number % 3 == 0) and (number % 2 == 0):
            if number > 40:
                for el in range(15):
                    if el != none_index:
                        for j in range(2,4):
                            ans += info[el][j]['>40'] + info[el][j]['<=40']
            else:
                for el in range(15):
                    if el != none_index:
                        for j in range(2,4):
                            ans += info[el][j]['>40']

        else:
            if number > 40:
                for el in range(15):
                    if el != none_index:
                        ans += info[el][3]['>40'] + info[el][3]['<=40']
            else:
                for el in range(15):
                    if el != none_index:
                        ans += info[el][3]['>40']

        last = line[0]
        line.pop(0)
        line.append(number)
        number = last
        append_ind = last % 15

        if number%6 == 0:
            if number > 40:
                info[append_ind][3]['>40'] += 1
            else:
                info[append_ind][3]['<=40'] += 1

        elif (number%3==0) and not(number%2==0):
            if number > 40:
                info[append_ind][2]['>40'] += 1
            else:
                info[append_ind][2]['<=40'] += 1

        elif not(number % 3 == 0) and (number % 2 == 0):
            if number > 40:
                info[append_ind][1]['>40'] += 1
            else:
                info[append_ind][1]['<=40'] += 1

        else:
            if number > 40:
                info[append_ind][0]['>40'] += 1
            else:
                info[append_ind][0]['<=40'] += 1
print(ans)

# №3

info = []
for i in range(9):
    helper = []
    for j in range(2):
        helper.append({'>30': 0, '<=30': 0})
    info.append(helper)
#     0 - none, 1 - 3 here

with open('/home/gora/PycharmProjects/USE-2022-informat/USE-2022-informat/test_sets/3-27-hard-26.11.txt', 'r') as f:
    dlin = int(f.readline())
    line = []
    ans = 0
    for i in range(3):
        line.append(int(f.readline()))
    for i in range(dlin - 3):
        num = int(f.readline())
        index = num%9
        none_index = (9 - index)%9

        if (num%3 == 0) and (num%9 != 0):
            if num > 30:
                for el in range(9):
                    if el != none_index:
                        ans += info[el][0]['>30'] + info[el][0]['<=30']
            else:
                for el in range(9):
                    if el != none_index:
                        ans += info[el][0]['>30']

        elif (num%3 != 0) and (num%9 != 0):
            if num > 30:
                for el in range(9):
                    if el != none_index:
                        ans += info[el][0]['>30'] + info[el][0]['<=30']
                        ans += info[el][1]['>30'] + info[el][1]['<=30']
            else:
                for el in range(9):
                    if el != none_index:
                        ans += info[el][0]['>30']
                        ans += info[el][1]['>30']

        last = line[0]
        line.pop(0)
        line.append(num)
        append_index = last % 9
        num = last

        if (num%3 == 0) and (num%9 != 0):
            if num > 30:
                info[append_index][1]['>30'] += 1
            else:
                info[append_index][1]['<=30'] += 1

        elif (num%3 != 0) and (num%9 != 0):
            if num > 30:
                info[append_index][0]['>30'] += 1
            else:
                info[append_index][0]['<=30'] += 1
print(ans)