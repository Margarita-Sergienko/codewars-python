# 6 kyu
# Sum of prime-indexed elements
# https://www.codewars.com/kata/59f38b033640ce9fc700015b
# In this Kata, you will be given an integer array and your task is to return the sum of elements occupying prime-numbered indices.
# The first element of the array is at index 0.

def isprime(num):
    if num <= 1:
        return False
    for i in range(2,num//2+1):
        if num % i == 0:
            return False
    return True
def total(arr):
    return sum([el for i, el in enumerate(arr) if isprime(i)])