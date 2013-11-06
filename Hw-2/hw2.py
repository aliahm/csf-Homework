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

n = 0
sum = 0

while n<101:
    sum = sum + n
    print sum
    n = n + 1

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
for i in range(1,n+1):
    n = n * i
    print n
###
### Problem 5
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 5 solution follows:"

n = 10
for i in range(10,n-1):
    n = n/i
    print n  



###
### Problem 6
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 6 solution follows:"

# ... write your code and comments here (and remove this line)

###
### Collaboration
###

# ... List your collaborators and other sources of help here (websites, books, etc.),
# ... as a comment (on a line starting with "#").

###
### Reflection
###

# ... Write how long this assignment took you, including doing all the readings
# ... and tutorials linked to from the homework page. Did the readings, tutorials,
# ... and lecture contain everything you needed to complete this assignment?
