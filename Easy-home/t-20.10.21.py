# №6 ---------------------------------------------------

# first variant (ineffective)
nums = list(map(int, input('Ввведите последовательность для неэффективного №6: ').split()))
n = len(nums)
maximum = 0
for i in range(n):
    for j in range(i + 1, n):
        maximum = max(nums[i]*nums[j], maximum)
print(maximum)

# second variant (effective)
n = int(input('Ввведите размер последовательности для эффективного №6: '))
maximum = -1000000000000000000
pre_maximum = -1000000000000000000000000000
for i in range(n):
    num = int(input())
    if num >= maximum:
        pre_maximum = maximum
        maximum = num
print(maximum*pre_maximum)

# №9 ---------------------------------------------------
n = int(input('Ввведите размер последовательности для неэффективного №9: '))

# first variant (ineffective)
nums = [int(input()) for i in range(n)]
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        chislo = nums[i]*nums[j]
        if (chislo > ans) and (chislo%3 == 0):
            ans = chislo
print(ans)

# second variant (effective)
n = int(input('Ввведите размер последовательности для эффективного №9: '))
maximum = 0
maximum_del_3 = 0
for i in range(n):
    num = int(input())
    flag = 0
    if (num % 3 == 0):
        if maximum_del_3 < num:
            maximum_del_3 = num
            flag = 1
    if (maximum < num) and flag == 0:
        maximum = num
print(maximum*maximum_del_3)

