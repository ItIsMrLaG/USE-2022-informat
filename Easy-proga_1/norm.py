# №1

print(input('Number for №1: '))

# №2

print(max(int(input('First num: ')), int(input('Second num: '))))

# №3

n = int(input('Number for №3: '))
if n > 5:
    print(n * 2)
else:
    print(n - 7)

# №4

n = int(input('Number for №4: '))
for n in range(n):
    print(1 + n, end='')
print('')

# №5

n = int(input('Number for №5: '))
for n in range(n):
    print(150 + n, end='')
print('')

# №12

print(sum([i*i for i in range(101)]))
