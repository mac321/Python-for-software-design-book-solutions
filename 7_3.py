'''
Complete soltion of Book
"Python For Software Design by Allen B. Downey"
by Harsh Bhatia ( www.harshbhatia.net )
'''
'''
INCOMPLETE
Exercise 7.2:Encapsulate loop in a function called square_root that takes a as a parameter,
chooses a reasonable value of x, and returns an estimate of the square root of a.
'''
import math
def square_root(a):
  x = 3
  while True:
    # print x
    y = (x + a/x) / 2
    if abs(y- x )< 0.001:
      break
    x = y
  return x

def test_square_root():
  i=1
  while i<10:
    print i
    print square_root(i)
    i=i+1

# test_square_root()
print square_root(3)