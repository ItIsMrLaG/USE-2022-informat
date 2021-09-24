# №21 -------------------------------------- #

n = int(input('Number for №21: '))
l = list(map(int, input().split(' ')))
mean = 0
maximum = max(l)
l.remove(maximum)
maximum2 = max(l)
print(maximum*maximum2)

# №22 -------------------------------------- #

n = int(input('Number for №22: '))
a = 0
b = 0

for i in range(n):
    kek = int(input(f'введите число: '))
    if kek % 3 != 0:
        continue
    if kek > a and kek > b:
        b = max(a, b)
        a = kek
    elif kek > a:
        a = kek
    elif kek > b:
        b = kek

print(a*b)

# №29 -------------------------------------- #

s = int(input('Number for №29: '))
print(f'Петя и Сережа сделали по {s // 4} штук, Катя сделала - {(s // 4) * 2} штук, бог подкинул - {s % 4}')

# №30 -------------------------------------- #

coins = int(input('Number for №30 - coins: '))
num = str(input('Number for №30 - position: '))
zero = num.count('0')
one = num.count('1')
print(min(zero, one))

