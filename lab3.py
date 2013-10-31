# Name: Ahmed Ali
# Evergreen Login: Aliahm18
# Computer Science Foundations
# Programming as a Way of Life
# Lab 3


n = 5
series = 'fibonacci'

if series == 'fibonacci':
    a = 0
    b = 1
    for i in range(n-1):
        fib = a + b
	(a,b) = (b,fib)
        print fib

if series == 'sum':
    total = 0
    a = 1
    for i in range(n):
        total = total + (3*a)
        a = a + 1
        print total