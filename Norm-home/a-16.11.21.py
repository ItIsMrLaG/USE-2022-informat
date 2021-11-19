import functools

# +2
# *3
# 1<s<27
# >=27
#
def moves(n):
    return (n+2), (n*3)

@functools.lru_cache(None)
def game(n):
    if n >= 27:
        return 'END'
    if any((game(x)=='END') for x in moves(n)):
        return 'P1'
    if all((game(x)=='P1') for x in moves(n)):
        return 'V1'
    if any((game(x)=='V1') for x in moves(n)):
        return 'P2'
    if all(((game(x)=='P2') or (game(x)=='P1')) for x in moves(n)):
        return 'V2'

print(moves(17))

for i in range(1, 27):
    print(game(i), i)
#


# +2
# *2
# *3
# >=31

def moves(n):
    return(n+2), (n*2), (n*3)

@functools.lru_cache(None)
def game(n):
    if n >= 31:
        return 'END'
    if any((game(x)=='END') for x in moves(n)):
        return 'P1'
    if all((game(x)=='P1') for x in moves(n)):
        return 'V1'
    if any((game(x)=='V1') for x in moves(n)):
        return 'P2'
    if all(((game(x)=='P1') or (game(x)=='P2')) for x in moves(n)):
        return 'V2'

print(moves(12))
for i in range(1, 31):
    print(game(i), i)


# +2
# *2
#  >=25

def move(n):
    return(n+2), (n*2)

@functools.lru_cache(None)
def game(n):
    if n >= 25:
        return'END'
    if any(game(x)=='END' for x in move(n)):
        return'P1'
    if all(game(x) == 'P1' for x in move(n)):
        return 'V1'
    if any(game(x) == 'V1' for x in move(n)):
        return 'P2'
    if all((game(x) == 'P2') or (game(x) == 'P1') for x in move(n)):
        return 'V2'
print(move(13))

for i in range(1, 30):
    print(i, game(i))


# +1
# *2
# >= 29

def moves(n):
    return (n+1), (n*2)

@functools.lru_cache(None)
def game(n):
    if n >= 29:
        return 'END'
    if any(game(x)=='END' for x in moves(n)):
        return 'P1'
    if all(game(x) == 'P1' for x in moves(n)):
        return 'V1'
    if any(game(x) == 'V1' for x in moves(n)):
        return 'P2'
    if all((game(x) == 'P2') or (game(x) == 'P1') for x in moves(n)):
        return 'V2'
print(moves(15))
for i in range(1, 30):
    print(i, game(i))


# +1
# *3
# >=36

#
def moves(n):
    return (n + 1), (n*3)

@functools.lru_cache(None)
def game(n):
    if n >= 36:
        return 'END'
    if any(game(x)=='END' for x in moves(n)):
        return 'P1'
    if all(game(x) == 'P1' for x in moves(n)):
        return 'V1'
    if any(game(x) == 'V1' for x in moves(n)):
        return 'P2'
    if all((game(x) == 'P1') or (game(x) == 'P2') for x in moves(n)):
        return 'V2'

print(moves(10))
for i in range(1, 37):
    print(i, game(i))


# +1
# +3
# *3

# >=39
#
def moves(n):
    return(n+1), (n*3), (n+3)

@functools.lru_cache(None)
def game(n):
    if n >=39:
        return 'END'
    if any(game(x) =='END' for x in moves(n)):
        return 'P1'
    if all(game(x) =='P1' for x in moves(n)):
        return 'V1'
    if any(game(x) =='V1' for x in moves(n)):
        return 'P2'
    if all((game(x) =='P2') or (game(x) =='P1') for x in moves(n)):
        return 'V2'

# print(moves(11))

for i in range(1, 40):
    print(i, game(i))
print(game(1))


# -1
# -3

def moves(n):
    return (n-1), (n-3)

@functools.lru_cache(None)
def game(n):
    if n <= 11:
        return 'END'
    if any(game(x)=='END' for x in moves(n)):
        return'P1'
    if all(game(x)=='P1' for x in moves(n)):
        return'V1'
    if any(game(x)=='V1' for x in moves(n)):
        return'P2'
    if all((game(x)=='P2') or ((game(x)=='P1')) for x in moves(n)):
        return'V2'

print(moves(30))
for i in range(11, 40):
    print(i, game(i))


# +1
# *2

# >=66
#
def moves(n):
    a, b = n
    return (a +1, b), (a*2, b), (a, b*2), (a, b +1)

@functools.lru_cache(None)
def game(n):
    if sum(n) >= 66:
        return 'END'
    if any(game(x)=="END" for x in moves(n)):
        return 'P1'
    if all(game(x)=="P1" for x in moves(n)):
        return 'V1'
    if any(game(x)=="V1" for x in moves(n)):
        return 'P2'
    if all((game(x)=="P1") or (game(x)=="P2") for x in moves(n)):
        return 'V2'

print(moves((6, 7)))


for i in range(1, 66):
    n = (11, i)
    print(i, game(n))
#


# +2

# *3
# >=88


def moves(n):
    a, b = n
    return (a+2, b), (a*3, b), (a, b*3), (a, b+2),

@functools.lru_cache(None)
def game(n):
    if sum(n) >= 88:
        return 'END'
    if any(game(x) =='END' for x in moves(n)):
        return 'P1'
    if all(game(x) =='P1' for x in moves(n)):
        return 'V1'
    if any(game(x) =='V1' for x in moves(n)):
        return 'P2'
    if all((game(x) =='P1') or (game(x) =='P2') for x in moves(n)):
        return 'V2'

print(moves((10, 8)))

for i in range(1, 88):
    n = (9, i)
    print(i, game(n))


# +1
# *4

# >=83

def moves(n):
    a, b =n
    return(a+1, b),(a*4, b),(a, b+1),(a, b*4)

@functools.lru_cache(None)
def game(n):
    if sum(n) >=83:
        return 'END'
    if any(game(x)=='END' for x in moves(n)):
        return'P1'
    if any(game(x) == 'P1' for x in moves(n)):
        return 'V1'
    if any(game(x) == 'V1' for x in moves(n)):
        return 'P2'
    if all((game(x) == 'P1') or (game(x) == 'P2') for x in moves(n)):
        return 'V2'

print(moves((11, 9)))

for i in range(1, 83):
    n = (5, i)
    print(i, game(n))