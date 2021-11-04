# №5

def five(n=7, k=2):
    s = []
    for el in range(1, n+1, k):
        print(el, end=', ')
        s.append(el)
    print()
    return s
print(*five())

# №9

def F(n):
    if n <= 2:
        return n
    else:
        return F(n - 1) + F(n - 1)*3

print(F(6)) # 512
