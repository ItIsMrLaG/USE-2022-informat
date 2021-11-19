import functools
# +1
# *3
# >=36

# №5
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

# №7

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


