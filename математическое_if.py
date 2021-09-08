# нужно вывести следующее четное число (решение должно быть в одной строке)

while True:
    value = int(input())
    print(value + (value%2) + ((value + 1)%2) * 2)
