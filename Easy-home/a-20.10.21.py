# №10

n = int(input())
dlin = [int(input()) for i in range(n)]
size = 0
ans = 0
for i in range(n):
    for j in range(i, n+1):
        helper = []
        for el in range(i, j, 2):
            helper.append(dlin[el])
        hsize = len(helper)
        hans = sum(helper)
        if (hans % 12 == 0) and (hsize >= size):
            size = hsize
            ans = hans
print(ans)

# example ->
# 13
# 12
# 1
# 12
# 1
# 5
# 1
# 12
# 1
# 12
# 1
# 6
# 1
# 6