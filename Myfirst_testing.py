# -*- coding: utf-8 -*-
# import math
# # print("hello world")
# # birth = input('birth:')
# # birth = int(birth)
# # if birth < 2000:
# #     print('before 00')
# # else:
# #     print('after 00')
#
# # height = 1.72
# # weight = 72.7
# # bmi = weight/ height /height
# # print(bmi)
# #
# # if bmi > 32:
# #     print('Heavy Obesity')
# # elif bmi > 28:
# #     print('Obesity')
# # elif bmi > 25:
# #     print('Overweight')
# # elif bmi > 18.5:
# #     print('Normal')
# # else:
# #     print('Light Weight')
#
# # names = ['A','B','C']
# # for name in names:
# #     print(name)
#
# # sum_num = 0
# # for x in [1,2,3,4,5,6,7,8,9,10]:
# #     sum_num = sum_num + x
# # print(sum_num)
#
# # print(list(range(5)))
# #
# # sum_num = 0
# # for x in list(range(101)):
# #     sum_num = sum_num + x
# # print(sum_num)
# #
# # sum = 0
# # n = 99
# # while n > 0:
# #     sum = sum + n
# #     n = n - 2
# # print(sum)
# #
# # L = ['A','B','C']
# # n = 2
# # while n >= 0 :
# #     print(L[n])
# #     n = n - 1
#
# # n = 1
# # while n < 20:
# #     n = n + 1
# #     if n % 2 == 0:
# #         continue
# #     print(n)
# #
# #
# # print('End')
#
# # names = ['Michael','Bob','Tracy']
# # scores = [ 95, 75, 85 ]
#
# # d = {'A': 100, 'B': 90, 'C': 80}
# # print(d['A'])
# # d['A'] = 90
# # print(d['A'])
# # print('C' in d)
# # print(d.get('M'))
# # d.pop('B')
# # print(d)
#
# # s1 = set([1, 2, 3, 4, 3 ])
# #
# # s1.add(8)
# # print(s1)
# # s1.remove(8)
# # print(s1)
# #
# # s2 = set([4, 5, 6, 7])
# #
# # print(s1 & s2)
# # print(s1 | s2)
#
# # a = ['d','a','b','c']
# # print(a)
# # a.sort()
# # print(a)
#
# # a = 'abc'
# # print(a.replace('a','A'))
# # print(a)
# #
# # help (abs)
#
#
# # print(int(23.34))
# # print(float(34))
# # print(str(34))
# # print(bool(1))
# # pp = print
# # pp(hex(23))
#
#
#
#
# # def
# #  my_abs(x):
# #     if not isinstance(x,(int,float)):
# #         raise TypeError('Bad operand type')
# #     if x>=0:
# #         return x
# #     else:
# #         return -x
# #
# # # print(my_abs(-43))
# # my_abs('z')
#
#
#
# # def move(x, y, step, angle=0):
# #     nx = x + step * math.cos(angle)
# #     ny = y - step * math.sin(angle)
# #     return nx, ny
# #
# #
# # x, y = move(100,100, 60, math.pi/6)
# # print(x, y)
# #
#
#
#
#
# # def quadratic(a, b, c):
# #     if not isinstance(a, (int, float)):
# #         raise TypeError('Bad operand type')
# #     if not isinstance(b, (int, float)):
# #         raise TypeError('Bad operand type')
# #     if not isinstance(c, (int, float)):
# #         raise TypeError('Bad operand type')
# #     delta = b * b - 4 * a * c
# #     if delta < 0:
# #         raise TypeError('No solution')
# #     else:
# #         x_1 = (-b+math.sqrt(delta))/ (2 * a)
# #         x_2 = (-b-math.sqrt(delta))/ (2 * a)
# #         return x_1, x_2
# #
# #
# # print(quadratic(1, -2, 1))
# #
# # print('quadratic(2, 3, 1)=', quadratic(2, 3, 1))
# # print('quadratic(1, 3, -4)=', quadratic(1, 3, -4))
# #
# # if quadratic(2, 3, 1) != (-0.5, -1.0):
# #     print('Testing Failed!')
# # elif quadratic(1, 3, -4) != (1.0, -4.0):
# #     print('Testing Failed!')
# # else:
# #     print('Successful')
#
#
#
#
# # def power(x, n=2):
# #     s = 1
# #     while n > 0:
# #         s = s * x
# #         n = n - 1
# #     return s
# #
# # print(power(25))
#
#


# def add_end(L=None):
#     L.append('END')
#     return L
#
#
# print(add_end([1, 2, 3]))
# print(add_end())
# print(add_end())
#
# for i in range(0,5):
#     print(i)
#

# def calc(*numbers):
#     sum_in = 0
#     for n in numbers:
#         sum_in = sum_in + n * n
#     return sum_in
#
#
# numbers_sum = (1, 2, 3, 4, 5)
# print(calc(*numbers_sum))


# def person(name, age, **kw):
#     print('Name:', name, 'Age:', age, 'Others:', kw)
#     return


# print(person('Michael', 30))
# print(person('Bob', 34, City='Singapore'))
# print(person('Adam', 45, Gender='M', Job='Engineer'))
# extra = {'City': 'Beijing', 'Job': 'Teacher'}
# print(person('Jack', 23, City=extra['City'], Job=extra['Job']))
# print(person('Jack', 54, **extra))

# def person(name, age, **kw):
#     print('Name:', name, 'Age:', age, 'Others:', kw)
#     return
#
#
# person('Adam', 45, Gender='M', Job='Engineer')


# def person(name, age, *,city='Hohhot', job):
#     print(name, age, city, job)
#     return
#
# # person('Zhang San','23',city='Hothhot',job='Teache',gender='M')
# person('Zhang San','23',city='Singapore',job='Teacher')

# def product(*numbers):
#     product_all = 1
#     for n in numbers:
#         product_all = product_all * n
#     return product_all
#
#
#
# print(product(1, 2, 3, 4, 5))


# def calc(*numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n
#     return sum
#
# print(calc(1,2,3,4))

# print('product(5) =', product(5))
# print('product(5, 6) =', product(5, 6))
# print('product(5, 6, 7) =', product(5, 6, 7))
# print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
# if product(5) != 5:
#     print('测试失败5!')
# elif product(5, 6) != 30:
#     print('测试失败6!')
# elif product(5, 6, 7) != 210:
#     print('测试失败7!')
# elif product(5, 6, 7, 9) != 1890:
#     print('测试失败9!')
# else:
#     try:
#         product()
#         print('测试失败last!')
#     except TypeError:
#         print('测试成功!')
#


# def move(n, a, b, c):
#     if n == 1:
#         print(a, '-->', c)
#     else:
#         move(n-1, a, c, b)
#         print(a, '-->', c)
#         move(n-1, b, a, c)
#
#
# move(10, 'a', 'b', 'c')


# def trim(s):
#     if s[:1] == ' ':
#         return trim(s[1:])
#     elif s[-1:] == ' ':
#         return trim(s[:-1])
#     else:
#         return s
#
#
# if trim('hello  ') != 'hello':
#     print('测试失败1!')
# elif trim('  hello') != 'hello':
#     print('测试失败2!')
# elif trim('  hello  ') != 'hello':
#     print('测试失败3!')
# elif trim('  hello  world  ') != 'hello  world':
#     print('测试失败4!')
# elif trim('') != '':
#     print('测试失败5!')
# elif trim('    ') != '':
#     print('测试失败6!')
# else:
#     print('测试成功!')
#
# print(trim('Hello   '))


#
# for ch in 'ABC':
#     print(ch)

# from collections import Iterable
# print(isinstance('abc', Iterable))

# for i, value in enumerate(['A', 'B', 'C']):
#     print(i, value)
#

# def text_save(content, filename, mode='a'):
#     # Try to save a list variable in txt file.
#     file = open(filename, mode)
#     for i in range(len(content)):
#         file.write(str(content[i]))
#     file.close()
#
#
# IQ = open("a.txt", 'r')
# n = 1
# seq_name = 2000
# line_output = ''
# for line in IQ.readlines():
#     if n == 1:
#         line_output = line
#     else:
#         line_output = line_output + line
#
#     if n % 3 == 0:
#         name_file = str(seq_name) + '.txt'
#         text_save(line_output, name_file)
#         seq_name = seq_name + 1
#         n = 0
#
#     n = n + 1
#
# IQ.close()

# d ={'a': 1, 'b': 2, 'c': 3, 'dd': 4}
# for key in d:
#     print(key)

# from collections import Iterable
#
# for ch in 'ABC':
#     print(ch)
#
# print(isinstance('abc', Iterable))
# print(isinstance([1, 2, 3], Iterable))
# print(isinstance(123, Iterable))
#
# for i, value in enumerate(['A', 'B', 'C']):
#     print(i, value)
#
# for x, y in[(1, 2), (3, 4), (5, 6)]:
#     print(x, y)

# def findMinAndMax(l):
#     if l ==[]:
#         return (None, None)
#     else:
#         maxnum = l[0]
#         minnum = l[0]
#         for num in l:
#             if num > maxnum:
#                 maxnum = num
#
#             if num < minnum:
#                 minnum = num
#
#         return (minnum, maxnum)
#
#
# LL = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(findMinAndMax(LL))
#
# if findMinAndMax([]) != (None, None):
#     print('测试失败1!')
# elif findMinAndMax([7]) != (7, 7):
#     print('测试失败2!')
# elif findMinAndMax([7, 1]) != (1, 7):
#     print('测试失败3!')
# elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
#     print('测试失败4!')
# else:
#     print('测试成功!')

# list_name = list(range(1, 10))
# print(list_name)
#
# L = []
# for x in range(1, 11):
#     L.append(x * x)
#
# print(L)
#
# print([x*x for x in range(1, 10)])
#
# print([x*x for x in range(1, 10) if x % 2 == 0])
#
# print([m + n + p for m in 'ABC' for n in 'XYZ' for p in 'ZXC'])
#
# import os
# print([d for d in os.listdir('.')])
#
# d = {'q': 'Q', 'w': 'W', 'e': 'E'}
# for value, key in d.items():
#     print(value, '=',key)
#
# ll = [k + '=' + v for k, v in d.items()]
# print(ll)

# L1 = ['Hello', 'World', 18, 'Apple', None]
# # L2 = []
# for s in L1:
#     if isinstance(s, str):
#         L2 = L2 + [ s.lower() ]
#         L2.append(s.lower())
#
#     # else:
#     #     L2 = L2 + [s]
#
#
# # Low = [s.lower() for s in L]
# print(L2)
#
#
# if L2 == ['hello', 'world', 'apple']:
#     print('测试通过!')
# else:
#     print('测试失败!')


# L1 = ['Hello', 'World', 18, 'Apple', None]
# L2 = [s.lower() for s in L1 if isinstance(s, str)]
#
# if L2 == ['hello', 'world', 'apple']:
#     print('测试通过!')
# else:
#     print('测试失败!')


# def fib(max):
#     n, a, b, = 0, 0, 1
#     while n < max:
#         print(b)
#         a, b = b, a + b
#         n = n + 1
#     return 'done'
#
# fib(5)
#
# def fib(fin_num):
#     nn, a, b = 0, 0, 1
#
#     while nn < fin_num:
#         yield b
#         a, b = b, a + b
#         nn = nn + 1
#     return 'done'
#
#
# # for m in fib(6):
# #     print(m)
#
# g = fib(6)
# while True:
#     try:
#         x = next(g)
#         print('g', x)
#     except StopIteration as e:
#         print('Generate return value', e.value)
#         break


# def odd():
#     print('step 1')
#     yield 1
#     print('step 2')
#     yield 3
#     print('step 3')
#     yield 5
#
#
# # o = odd()
# next(odd())

# def triangle():
#     for m in
#     return

# def triangle(num_line):
#     line_loop = 0
#     L = [1]
#     while line_loop < num_line:
#         print(L)
#         r = []
#         for i in range(len(L)-1):
#             r.append(L[i]+L[i+1])
#         r.insert(0, 1)
#         r.append(1)
#         L = r
#         line_loop = line_loop + 1
#
#
# triangle(9)

#
# k = [1, 2, 3]
# k.append(4)
# print(k)
# print(k[0])
# print(len(k)-1)

# from collections import Iterable
# print(isinstance([], Iterable))
#
# print(isinstance({}, Iterable))
#
# print(isinstance('abc', Iterable))
#
# print(isinstance((x for x in range(10)), Iterable))
#
# print(isinstance(100, Iterable))

# Python的for循环本质上就是通过不断调用next()函数实现的
# 凡是可作用于for循环的对象都是Iterable类型；
# 凡是可作用于next()函数的对象都是Iterable类型，他们表示一个惰性计算的序列；
# 集合数据类型如list,dict,str等是Iterable但不是Iterator,不过可以通过iter()函数获得一个Iterator对象；

#
# def add(x, y, f):
#     return f(x) + f(y)
#
#
# print(add(3, -4, abs))

# def f(x):
#     return x*x
#
#
# r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(list(r))
#
# print(list(map(str, [1, 2, 3, 4, 5])))
#
#
#
#
# def add(x, y):
#     return x+y
#
#
# a = reduce(add, [1, 2, 3, 4, 5, 6, 7, 8, 9])
#
# print(a)


# def fn(x, y):
# #     return x*10+y
# #
# #
# # a = reduce(fn, [1, 2, 3, 4, 5, 6, 7, 8, 9])
# #

#
#
# def charm2num(s):
#     digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#     return digits[s]
#
#
# def fn(x, y):
#     return x * 10 + y
#
#
# a = reduce(fn, list(map(charm2num, '123456897')) )
# print(a)
#
# print(list(map(charm2num, '123456789')))
# # print(a)

# from functools import reduce
#
# DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#
#
# def str2int(s):
#     def fn(x, y):
#         return x * 10 + y
#
#     def ch2num(s):
#         return DIGITS[s]
#     return reduce(fn, map(ch2num, s))
#
#
# print(str2int('345233'))
#
#
# def char2num(s):
#     return DIGITS[s]
#
# def str2int(s):
#     return reduce(lambda x, y: x * 10 + y, map(char2num, s))
#
# print(str2int('52345'))
#
# from functools import reduce
#
# def normalize(name):
##########################################################
# def captial(L):
#     big = []
#     Low = [s.lower() for s in L]
#     for ind in range(len(Low)):
#         capital = Low[ind][0].upper()
#         for ind_sec in range(len(Low[ind])):
#             if ind_sec != 0:
#                 capital = capital + Low[ind][ind_sec]
#         big.append(capital)
#     return big
#
#
# L = ['ABc', 'B', 'C', 'aB']
# upp = captial(L)
# print(upp)
###########################################################################
# from functools import reduce
#
# def capital_word(low_word):
#     for inx in range(len(low_word)):
#         if inx == 0:
#             b = low_word[inx].upper()
#         else:
#             b = b + low_word[inx].lower()
#     return b
#
#
# b = capital_word('aPPLe')
# print(b)
#
# L = ['aPPLe', 'bANANa', 'OrAnGe']
# r = map(capital_word, L)
# # print(list(r))
#
#
# # LL = [1, 3, 5, 7, 9]
#
#
# def prod(LL):
#     def multiply(xx, yy):
#         return xx * yy
#
#     aaa = reduce(multiply, LL)
#     return aaa
#
#
# print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
# if prod([3, 5, 7, 9]) == 945:
#     print('测试成功!')
# else:
#     print('测试失败!')#


# from functools import reduce
# DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#
#
# def str2float(a):
#     def str2int(s):
#         def char2num(c):
#             return DIGITS[c]
#
#         def fn(x, y):
#             return x * 10 + y
#         return reduce(fn, map(char2num, s))
#
#     b = a[:a.find('.')]
#     c = a[a.find('.')+1:]
#     a_num = str2int(b) + str2int(c)/(10 ** (len(a) - a.find('.') - 1))
#     return a_num
#
#
# a_str = '1234.56'
# # print(len(a))
# # print(a.find('.'))
# # print(b)
# # print(c)
#
# a_float = str2float(a_str)
# print(a_float)
#
# print('str2float(\'123.456\') =', str2float('123.456'))
# if abs(str2float('123.456') - 123.456) < 0.00001:
#     print('测试成功!')
# else:
#     print('测试失败!')
#
# from functools import reduce
# #
# DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '.': ''}
#
#
# def str2float(a):
#     def str2int(s):
#         def char2num(c):
#             return DIGITS[c]
#
#         num_dot = list(map(char2num, s))
#
#         num_dot = num_dot.remove('')
#
#
#         def fn(x, y):
#             return x * 10 + y
#         return reduce(fn, num_dot)
#     a_num = str2int(a) / (10 ** (len(a) - a.find('.') - 1))
#     return a_num
#
#
# a_str = '1234.56'
# a_float = str2float(a_str)
# print(a_float)
#
# from functools import reduce
# DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '.': ''}
#
#
# def char2flout(a):
#
#     def char2num(c):
#         return DIGITS[c]
#
#     def fn(x, y):
#         return x * 10 + y
#
#     b = list(map(char2num, a))
#     dot = b.index('')
#     b.remove('')
#     aaa = reduce(fn, b)
#     aa = aaa / (10 ** (len(a) - dot - 1))
#     return aa
#
#
# a_str = '1234567890.4321'
# print(char2flout(a_str))
# print(a_str.rindex('.'))
#
# def is_odd(n):
#     return n % 2 == 1
#
#
# print(is_odd(8))
# a = list(filter(is_odd, [1, 2, 3, 4, 5, 6]))
# print(a)
#
#
#
#
# cc = [x.strip() for x in s if x != None ]
# print(cc)
# #print(not_empty('s   s'))
#
#
# a = not None
# print(a)
#
#
#
# def not_empty(s):
#     return s and s.strip()
#
#
# sss = ['', 'a', 'sd', '   d', '  g  ', 'gh             ', None]
#
# aaa = list(filter(not_empty, sss))
# bbb = [x.strip() for x in aaa]
# print(bbb)

def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)


for n in primes():
    if n < 50:
        print(n)
    else:
        break
