# №5 ------------------------------------ #
y = int(input())
print((y**2)**0.5)

# №7 ------------------------------------ #
y = int(input())
print((y%2)*y + y - 3*((y+1)%2))

# №8 ------------------------------------ #
y = int(input())
a = 1
m = 0
for i in range(y):
    num = int(input())
    m = (m + num*a + ((m - num*a)**2)**0.5)//2
    a = num
print(m)

# №21 ------------------------------------ #
a = int(input())
b = int(input())
c = int(input())
ab = (a + b + ((a - b)**2)**0.5)//2
abc = (ab + c + ((ab - c)**2)**0.5)//2

min_ab = (a + b - ((a - b)**2)**0.5)//2
min_abc = (ab + c - ((ab - c)**2)**0.5)//2

print(abc - min_abc)

# №22 ------------------------------------ #
n = int(input())
mix1 = 0
mix2 = 0
l = []
for i in range(n):
    num = int(input())
    l.append(num)
    mix1 = (mix1 + num + ((mix1 - num) ** 2) ** 0.5) // 2
l.remove(mix1)

for i in l:
    mix2 = (mix2 + i + ((mix2 - i) ** 2) ** 0.5) // 2

print(mix1*mix2)

# №23 ------------------------------------ #
x = int(input())
a = 6
b = 3
c = 2
print(2 *(1 - (((x%b) + b - 1) // b)) +  (1 - (((x%c) + c - 1) // c)))