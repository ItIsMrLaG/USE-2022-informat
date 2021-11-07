# hard

# № 1
def filin(first, second):
    if first == second:
        return 1
    elif first > second:
        return 0
    else:
        return filin(first + 1, second) + filin(first*2, second)

print('1. ', filin(1, 30))


# № 2
def focus(first, second):
    if first == second:
        return 1
    elif first > second:
        return 0
    else:
        return focus(first*3, second) + focus(first+2, second)

print('2. ', focus(1, 41))


# № 3
def twf(first, second):
    if first == second:
        return 1
    elif first > second:
        return 0
    else:
        return twf(first + 1, second) + twf(first + 2, second) + twf(first*3, second)

print('3. ', twf(1, 25))


# № 4
def Start(first, second):
    if first == second:
        return 1
    elif first > second:
        return 0
    else:
        return Start(first + 1, second) + Start(first + 3, second) + Start(first * 2, second)

print('4. ', Start(1, 23))


# № 5
def ura(first, second):
    if first == second:
        return 1
    elif first > second:
        return 0
    else:
        return ura(first + 1, second) + ura(first*3, second) + ura(first * 2, second)

print('5. ', ura(1, 30))

# № 6
def filin2(first, second, flag=True):
    Flag = flag
    if first == 8:
        Flag = False
    if first == second and flag:
        return 1
    elif first < second:
        return filin2(first + 1, second, Flag) + filin2(first*2, second, Flag)
    else:
        return 0

print('6. ', filin2(1, 30))


# № 7
def focus2(first, second, flag=True):
    Flag = flag
    if first == 15:
        Flag = False
    if first == second and flag:
        return 1
    elif first < second:
        return focus2(first + 2, second, Flag) + focus2(first*3, second, Flag)
    else:
        return 0

print('7. ', focus2(1, 41))



# № 8
def twf2(first, second, flag=False):
    Flag = flag
    if first == 15:
        Flag = True
    if first == second and flag:
        return 1
    elif first < second:
        return twf2(first + 2, second, Flag) + twf2(first*3, second, Flag) + twf2(first + 1, second, Flag)
    else:
        return 0

print('8. ', twf2(1, 25))


# № 9
def Statrt2(first, second, flag=True):
    Flag = flag
    if first == 4:
        Flag = False
    if first == second and flag:
        return 1
    elif first < second:
        return Statrt2(first + 3, second, Flag) + Statrt2(first*2, second, Flag) + Statrt2(first + 1, second, Flag)
    else:
        return 0

print('9. ', Statrt2(1, 23))


# № 10
def ura2(first, second, flag=True):
    Flag = flag
    if first == 3:
        Flag = False
    if first == second and flag:
        return 1
    elif first < second:
        return ura2(first*3, second, Flag) + ura2(first*2, second, Flag) + ura2(first + 1, second, Flag)
    else:
        return 0

print('10. ', ura2(1, 30))
