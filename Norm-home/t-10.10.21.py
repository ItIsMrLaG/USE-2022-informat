# №6

P = [25, 36]
Q = [28, 55]

def inside1(A, x):
    return (A[0] <= x <= A[1])

def func1 (A, x):
    return (not(not inside1(Q, x) or inside1(P, x)) or not(inside1(A, x)))

k = 1
maximum = 0
for a in range(80*k):
    for b in range(80*k):
        pofi = True
        A = [a/k, b/k]
        for x in range(80*k):
            if not func1(A, x):
                pofi = False
                break
        if pofi:
            maximum = max(maximum, (A[1] - A[0]))
print(maximum)
# ответ - 18

# №10

P = [25, 36]
Q = [28, 55]

def inside2(A, x):
    return (A[0] <= x <= A[1])

def func2 (A, x):
    return ((inside2(P, x) and inside2(Q, x)) <= (inside2(Q, x) and inside2(A, x)))

k = 3
minim = 100000000000000000
for a in range(80*k):
    for b in range(80*k):
        pofi = True
        A = [a/k, b/k]
        for x in range(100):
            if not func2(A, x):
                pofi = False
                break
        if pofi:
            minim = min(minim, (A[1] - A[0]))
            if A[1] - A[0] == 16:
                print(A)
            elif A[1] - A[0] == 8:
                print(A, ' - 8')
print(minim)

# ответ - 8, а в основном ответе - 16(