# pyrhon
# -*- coding: utf-8 -*-
import math
def quadratic(a, b, c):
#	for y in(a, b, c):
#		if not isinstance(y, (int, float)):
#			raise TypeError('bad operand type')
	if a==0:
		raise TypeError('Not a quadratic equation')
	else:
		Delta=b*b-4*a*c
		if Delta< 0:
			raise TypeError('No solution')
		elif Delta==0:
			x=-b/a*0.5
			return x
		else:
			x_1=(-b+Delta**0.5)/a/2
			x_2=(-b-Delta**0.5)/a/2
			return x_1, x_2

a=float(input('Please input quadratic term coefficient：'))
b=float(input('Please input monomial coefficient：'))
c=float(input('Please constant term：'))
#print(quadratic(2, 3, 1))
#print(quadratic(1, 3, -4))
#print(quadratic(1, 0, 1))
#print(quadratic(1, 'x', 1))
#print(quadratic(1, -2, 1))
print('The root'r'(s)','of the quadratic equation is',quadratic(a, b, c))
