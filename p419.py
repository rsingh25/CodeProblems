# Given a positive integer N, find the smallest number of steps it will take to reach 1.

# There are two kinds of permitted steps:

# You may decrement N to N - 1.
# If a * b = N, you may decrement N to the larger of a and b. (This does not match with example)
# For example, given 100, you can reach 1 in five steps with the following route: 100 -> 10 -> 9 -> 3 -> 2 -> 1.

import math

def exec(n):
  s = 0
  
  while( n != 1):
    n = takeNextStep(n) 
    print (n)
    s +=1

  return s
  

# error handling   
def takeNextStep(n):
  sqrt = int(math.sqrt(n))
  
  if sqrt * sqrt == n :
     return sqrt
  else:
     return n-1
  
exec(105)