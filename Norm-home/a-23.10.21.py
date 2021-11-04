# изи дз

# №1

# with open('/home/gora/PycharmProjects/USE-2022-informat/USE-2022-informat/test_sets/tester.txt', 'r') as f:
#     l = f.readline().split(' ')
#     x = int(l[0])
#     n = int(l[1])
#     db = [0]*x
#     ans =[0]*(x//2 + 1)
#     even = not(x%2)
#     for i in range(n):
#         elem = int(f.readline())
#         index = elem % x
#         if even:
#             if (index == x//2) or (index == 0):
#                 ans[index] += db[index]
#                 db[index] += 1
#             else:
#                 db[index] += 1
#                 ans_index = index
#                 if (index > len(ans) - 1):
#                     ans_index = x - index
#                 helper = db[index] * db[x - index]
#                 if not (helper == 0):
#                     ans[ans_index] = helper
#         else:
#             if index == 0:
#                 ans[index] += db[index]
#                 db[index] += 1
#             else:
#                 db[index] += 1
#                 ans_index = index
#                 if (index > len(ans) - 1):
#                     ans_index = x - index
#                 helper = db[index]*db[x - index]
#                 if not(helper == 0):
#                     ans[ans_index] = helper
#     print(db)
#     print(sum(ans))

# №2

# n = 347823
# for i in range(1, 347823//2):
#     if 347823 % i == 0:
#         print(i, end=' ')
# print(347823)

# №3

# n = 47298356
# for i in range(1, int(n**0.5 + 1)):
#     if n % i == 0:
#         print(i, n // i)

# №4

# x = 9
# s = [875, 631, 713, 742, 725, 411, 470, 473, 382, 81]
# maxim9 = 0
# for i in s:
#     if i%9 == 0 and i > maxim9:
#         maxim9 = i
# maxim = max(s)
# if maxim == maxim9:
#     s.remove(maxim)
#     print(s)
#     maxim = max(s)
# print(maxim*maxim9)

# №10

# with open('/home/gora/PycharmProjects/USE-2022-informat/USE-2022-informat/test_sets/27_10_hw.txt', 'r') as f:
#     n = int(f.readline())
#     zero, one, two = 0, 0, 0
#     for i in range(n):
#         if i%3 == 0:
#             zero += 1
#         elif i%3 == 1:
#             one += 1
#         else:
#             two += 1
#     print(zero*(one + two) + 0.5*(one*(one - 1) + two*(two - 1)))
