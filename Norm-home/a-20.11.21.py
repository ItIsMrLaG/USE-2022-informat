# №1
def del_finder(n):
    l = []
    ans = 1
    counter = 0
    for de in range(2, int(n**0.5)+1):
        if len(l) == 5:
            break
        if n % de == 0:
            l.append(de)
            ans *= de
            counter += 1
    l.reverse()
    if (len(l) == 3) or (len(l) == 4):
        for el in l:
            if counter == 5:
                break
            new_del = n // el
            if new_del not in l:
                counter += 1
                l.append(new_del)
                ans *= new_del
    if counter == 5:
        return ans, max(l)
    else:
        return False, None

c = 0
start = 300000000
while c < 5:
    a = del_finder(start)
    if a[0]%100 == 31 and a[0] <= start:
        c += 1
        print(a, start)
    start += 1


# №2
def del_finder(n):
    l = []
    counter = 0
    ans = 1
    for el in range(2, int(n**0.5)):
        if len(l) >= 5:
            break
        if n%el == 0:
            l.append(el)
            ans *= el
            counter += 1
    l.reverse()
    if (len(l) == 3) or (len(l) == 4):
        for i in l:
            if counter == 5:
                break
            new_del = n//i
            if new_del not in l:
                ans *= new_del
                l.append(new_del)
                counter += 1
    if counter == 5:
        return ans, max(l)
    else:
        return False, None

c = 0
start = 400000000
while c < 5:
    ans = del_finder(start)
    if ans[0]%100==17 and ans[0] <= start:
        c += 1
        print(ans)
    start += 1

# №3
counter = 0
for a in range(1, 5001):
    for b in range(a, 5001):
        if int((a**2 + b**2)**0.5) == (a**2 + b**2)**0.5 and (a**2 + b**2)**0.5 <= 5000:
            counter += 1
print(counter)

# №4
up = 300000000
down = 100000000

for m in range(1, 30, 2):
    for n in range(0, 30, 2):
        ans = (2**m)*(7**n)
        if (down < ans) and (ans < up):
            print(ans, m+n, m, n)

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

# №6
up = 300000000
down = 100000000

for m in range(1, 30, 2):
    for n in range(0, 30, 2):
        ans = (2**m)*(5**n)
        if (down < ans) and (ans < up):
            print(ans, m+n, m, n)
# №7

def finder_prime(n):
    if (n == 1) or (n == 2) or (n==3):
        return [n]
    l = []
    for de in range(1, int(n**0.5)+1):
        if n%de == 0:
            l.append(de)
        if len(l) > 1:
            return [*finder_prime(n//de)] + [*finder_prime(de)]
    if len(l) == 1:
        return [n]

for el in range(33333, 55556):
    d = sum(finder_prime(el))
    if (el%d == 0) and (d > 250) and (el != d):
        print(el, d)

# №8
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