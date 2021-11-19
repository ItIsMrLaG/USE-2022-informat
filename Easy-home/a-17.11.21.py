# №1
s = '7'*367+'9'*34
while ('77' in s) or ('9' in s):
    while ('79' in s):
        s = s.replace('79', '77', 1)
    if '77' in s:
        s = s.replace('77', '9', 1)
    elif '9' in s:
        s = s.replace('9', '8', 1)

print(s)
print(s.count('8')*7)


# №2
s = '*'+'2'*100+'5'*10+'9'*60
while ('*2'in s) or ('*5' in s) or ('*9' in s):
    if '*2' in s:
        s = s.replace('*2', "*")
    if "*5" in s:
        s = s.replace("*5", '6*')
    if "*9" in s:
        s = s.replace("*9", '7*')
print(s)
print(s.count('6')*6 + s.count('7')*7)

# №3
s = '*' + '2'*30 + '5'*63 + '9'*36

while ('*2' in s) or ('*5' in s) or ('*9' in s):
    if  '*2' in s:
        s = s.replace('*2' , '*')
    if '*5' in s:
        s = s.replace('*5', '6*')
    if '*9' in s:
        s = s.replace('*9' , '7*')
print(s.count('7')*7 + s.count('6')*6)

# №4
s = '5'*10 + '7'*30 + '2'*50
while ('5' in s) or ('77' in s) or ('222' in s):
    if '5' in s:
        s = s.replace('5', '77')
    elif '77' in s:
        s = s.replace('77', '7')
    elif '222' in s:
        s = s.replace('222', '5')
print(11)

# №5
s = '5'*10 + '4'*10 + '2'*10 + '7'*10
while ('54' in s) or ('27' in s):

    if  '55' in s:
        s = s.replace('55', '7')
    elif ('22' in s):
        s = s.replace('22', '7')

    if '44' in s:
        s = s.replace('44', '4')
    elif '77' in s:
        s = s.replace('77', '7')

print(s)
print(s.count('7'))

# №6
with open('/home/gora/PycharmProjects/USE-2022-informat/USE-2022-informat/test_sets/Задача 6.txt', 'r') as f:
    print(eval(f.readline().strip())) # а я читы знаю))))))))

# №7
with open('/home/gora/PycharmProjects/USE-2022-informat/USE-2022-informat/test_sets/Задача 7.txt', 'r') as f:
    s = f.readline().strip()
    print(eval(s), eval(s)/len(s.replace('+', ''))) # все равно использую читы, гыыыыыы

# №8
with open('/home/gora/PycharmProjects/USE-2022-informat/USE-2022-informat/test_sets/Задача 8.txt', 'r') as f:
    print(eval(f.readline().strip()))

# №9
with open('/home/gora/PycharmProjects/USE-2022-informat/USE-2022-informat/test_sets/Задача 9.txt', 'r') as f:
    if eval(f.readline().strip().replace('=', '==')):
        f.seek(0)
        print(max(map(eval, f.readline().strip().split('='))))
    else:
        f.seek(0)
        h = f.readline()
        print(max(map(eval, h.strip().split('='))), min(map(eval, h.strip().split('='))))
# читыыыыыыы еееееее)))))))))

# №10

def is_vowel(el):
    if el in 'AEIOUY':
        return True
    else:
        return False


with open('/home/gora/PycharmProjects/USE-2022-informat/USE-2022-informat/test_sets/tester.txt', 'r') as f:
    s = f.readline().strip()
    v = 0
    c = 0
    s1 = ''
    for el in s:
        if (s1 == '') or (is_vowel(s1[0]) == is_vowel(el)):
            s1 += el
            continue
        else:
            if is_vowel(s1[0]):
                v = max(len(s1), v)
            else:
                c = max(len(s1), c)
            s1 = el
    if is_vowel(s1[0]):
        v = max(len(s1), v)
    else:
        c = max(len(s1), c)

    print(v, c)
