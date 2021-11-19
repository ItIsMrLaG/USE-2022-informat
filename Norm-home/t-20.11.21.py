# Прога - сложная
# №5
up = 300000000
down = 100000000
ansm = {}
helper = []
for m in range(0, 30, 2):
    for n in range(1, 30, 2):
        ans = (2**m)*(7**n)
        if (down < ans) and (ans < up):
            ansm[ans] = m+n
            helper.append(ans)
helper.sort()
for el in helper:
    print(el, ansm[el])

# №8
# как оптимизировать еще больше, я не придумал

def finder7(n):
    l = []
    counter = 0
    up = int(n**0.5)+1
    for de in range(up, 0, -1):
        if counter == 3 or ((up - de) > 120):
            break
        if n%de == 0:
            if (n//de - de <= 120) and (de not in l):
                counter += 1
                l.append(n//de)
                l.append(de)
    if counter >= 3:
        return max(l)
    else:
        return False

for i in range(2046330, 3000001):
    g = finder7(i)
    if g:
        print(i, g)
