# Name: Ahmed Ali
# Evergreen Login: AliAhm18
# Computer Science Foundations
# Programming as a Way of Life
# Homework 2

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.


###
### Problem 1
### 
print "Problem 1 solution follows:"

# This while loop calculates the sum of 0 thruough 100 but not
# including 101 and places it in the variable "sum"
#Use a while loop to solve Gauss's general problem

n = 1
sum = 0

while (n<101):
    sum = sum + n
    n = n + 1
    print sum
###
### Problem 2
### 

print "Problem 2 solution follows:"

#Use a for loop to print the decimal representations of 
# 1/2, 1/3, ..., 1/10, one on each line.

x = 1.0
for i in range(2,11,1):
    print x/i


###
### Problem 3
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 3 solution follows:"


n = 10
triangular = 0
for i in range(n+0):
    triangular = triangular
print "Triangular number", n, "via loop:", triangular
print "Triangular number", n, "via formula:", n*(n+1)/2


# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 4 solution follows:"

n = 10
for i in range(1, 11, 1):
    n = n * i
    print n
###
### Problem 5
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 5 solution follows:"
x = n
n = 10
for i in range(n, 0, -1):
    print x
    x = x/i

###
### Problem 6
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 6 solution follows:"

y = 1
for i in range(1, 11, +1):
    factorial = 1
    for j in range(1, i+1, 1): 
        factorial = factorial * j
    print factorial
    y = y + 1.0/factorial
    print
print y
        
###
### Collaboration
###

# ... Kahea(Tutor) Khan Academy (Youtube)
# ... as a comment (on a line starting with "#").

###
### Reflection
###
"""I took me about 10 hours with all the readings and help I got,
the readings helpful and plus going to the tutora where ever I got
stuck they showed me how to do it correct."""


