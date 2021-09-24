# №2 ------------------------------ #

n1 = int(input())
n2 = int(input())
print((n1//n2)**(n2//n1))

# №11 ------------------------------ #

n = int(input())
s = 0
for i in range(n):
    num = int(input())
    s += (1 - (((num % 6) + 5) // 6)) * num
print(s)
