
from itertools import combinations

def matrixPrinter(n, full: list, mean='*', splitter=' ', space = '#'): # n = len side of the matrix, давать отсортированный список
    print(' ', end='')
    for i in range(n-1):
        print(f' {i+1}', end='')
    print(f' {n}')
    s = '1 '
    counter = 0
    for i in range(n**2):
        if i in full:
            s += mean + splitter
            full.pop(0)
        else:
            s += space + splitter
        counter += 1
        if counter == n:
            print(s[0:-1])
            counter = 0
            s = str(i//n + 2) + ' '

counter = 0
n = 8
number = 3
for main in combinations(range(n**2), r=number):
    print('number - ', counter)
    counter += 1
    helper = list(main)
    helper.sort()
    matrixPrinter(n, full=helper)
    print(' ')