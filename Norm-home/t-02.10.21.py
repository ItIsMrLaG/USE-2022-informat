# №10

# 1 0 2 3
# 0 1 4 5
# 2 4 1 6
# 3 5 6 1

# данные вбивать последовательно, построчно

n = int(input())
m = int(input())
first = m - 1
second = 1
up = []
down = []
f_down = []
for i in range(0, n-1):
    line = int(input())
    for u1 in range(first):
        up.append(int(input()))
    first -= 1
    down.append([int(input()) for j in range(second)])
    second += 1
line = int(input())
counter = 0
ind = 0
while counter < len(up)+1:
    for i in down:
        counter += 1
        if ind + 1 <= (len(i)):
            f_down.append(i[ind])
    ind += 1
print((up == f_down))


# №16

# n = 2
# m = 3

# 1 2 3
# 4 5 6

# пример ввода
# 2  // n
# 3  // m
# 1
# 2
# 3
# 4
# 5
# 6

n = int(input())
m = int(input())

l = []
for i in range(n):
    l.append([int(input()) for j in range(m)])
counter = 0
for j in range(m):
    for i in l:
        print(i[counter], end=' ')
    print('\n', end='')
    counter += 1
