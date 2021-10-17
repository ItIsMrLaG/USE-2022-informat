# №2

print('x y z|f')
for x in range(2):
    for y in range(2):
        for z in range(2):
            ans = ((y or x) <= (x == z))
            if not ans:
                print(x, y, z, ans)
# Ответ на задачу  - xyz

# №10
def func(A, x, y):
    return ((2*x + 5*y <= A) or (x >= y) or (y > 11))

for A in range(200):
    pofi = True
    for x in range(200):
        for y in range(200):
            if func(A, x, y) == False:
                pofi = False
                break
    if pofi == True:
        print(A)
# Ответ на задачу  - 75, а в ответах - 15, но я даже ручками перепроверил, все сходится(
