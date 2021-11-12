# HARD


# №1
l = [1, 2, 3, 4, 5, 6, 7]
ans = sum(l[i]*(-1)*(i%2) + l[i]*(1)*((i-1)%2) for i in range(len(l)))
print(ans)


# №2
def returner(t:tuple):
    helper = []
    ans = []
    for i in t:
        if (i in helper):
            if (i in ans):
                ans.pop(ans.index(i))
            continue
        helper.append(i)
        ans.append(i)
    return tuple(ans)

print(returner((2,12,2,2,3,4,5,4)))


# №10
def sorter(n):
    mean = all(str(x).isdigit() for x in n)
    if mean:
        home = list(n)
        home.sort()
        return home
    return n

print(sorter((1,4,3,2,5,8,8,6,)))

