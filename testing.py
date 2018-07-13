# -*- coding: utf-8 -*-
# import numpy
#
#
# def print_odd(a):
#     aa = 2
#     list_a =[]
#     while aa <= a:
#         n = 2
#         while n <= numpy.sqrt(aa):
#             if aa % n != 0:
#                 n = n + 1
#             else:
#                 break
#
#         if n > numpy.sqrt(aa):
#             list_a.append(aa)
#  #           print(aa)
#         aa = aa + 1
#
#     return list_a
#
#
# b = 50
# dd = print_odd(b)
# print(dd)


# def is_palindrome(x):
#     y = str(x)
#     n = 0
#     while n <= 0.5 * len(y):
#         if y[n] == y[len(y) - 1 - n]:
#             n = n + 1
#         else:
#             break
#     if n > 0.5 * len(y):
#         m = True
#     else:
#         m = False
#     return m
#
#
# output = filter(is_palindrome, range(1, 1000))
# print('1~1000:', list(output))
# if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
#     print('测试成功!')
# else:
#     print('测试失败!')


# def is_palindrome(n):
#     return str(n) == str(n)[::-1]
#
#
# output = filter(is_palindrome, range(1, 1000))
# print('1~1000:', list(output))
# if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
#     print('测试成功!')
# else:
#     print('测试失败!')

# print(sorted([36, 5, -12, 9, -21]))
# print(sorted([36, 5, -12, 9, -21], key = abs))
# p = sorted(['b', 'a', 'Z', '0', '8', 'H'])
# print(p)
# pp = sorted(['b', 'a', 'Z', '0', '8', 'H'], key=str.lower, reverse=True)
# print(pp)

def by_name(t):
    return t[0]


L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# for n in range(len(L)):
#     print(L[n][0])

p = sorted(L, key=by_name)
print(p)
print(by_name(L))
