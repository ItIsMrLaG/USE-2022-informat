# №15

n = int(input())
l = 0
for i in range(n):
    num = int(input())
    num = num*(-1000 <= num<= 1000)
    l += num
print(l)

# №6

n = int(input())
max = 0
for i in range(n):
    num = int(input())
    if max < num:
        max = num
print(max)