#!/usr/bin/python

"""
Fibonacci Prime
Write code to find the first prime
fibonacci number larger than a given minimum.  For example, the first
  prime fibonacci number larger than 10 is 13.

Compute the smallest prime fibonacci number greater than 227,000
Call this number X.

The answer is the sum of prime divisors of X + 1

  For the second portion
  of this task, note that for the number 12 we consider the sum of the prime divisors
  to be 2 + 3 = 5.  We do not include 2 twice even though it divides 12 twice.
"""

def isPrime(num):
  if num == 2: 
    return True
  elif num == 1 or num % 2 == 0:
    return False

  for i in xrange(3, num/2, 2):
    if num % i == 0:
      return False
  return True

def fibonacci(n):
  terms = [0,1]
  i = 2
  while i <= n:
    terms.append(terms[i-1]+terms[i-2]) 
    i = i + 1
  return terms[n]

def fibonacci_Prime(my_min, my_max):
  for i in xrange(3, my_max):
    num = fibonacci(i)
    if ((num > my_min) and (isPrime(num))):
      return num
    else:
      continue

def divisors_of(source):
  divisors = []
  for i in xrange(1,source):
    if source % i == 0:
      divisors.append(i)
    else:
      pass
  return divisors



answer = fibonacci_Prime(227000,500000)
my_divisors = divisors_of(answer+1)
total = 0
for x in my_divisors:
  if isPrime(x):
    print x
    total += x

print answer
print "Total: ", total
