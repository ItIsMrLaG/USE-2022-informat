# Алгоритм Евклида (нахождение общего нод для двух чисел)

def Euq (a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return(a + b)

a = 10
b = 90
print(Euq(a, b))