# 7 kyu
# Unique string characters
# https://www.codewars.com/kata/5a262cfb8f27f217f700000b
# In this Kata, you will be given two strings a and b and your task will be to return the characters that are not common in the two strings.
# For example:
# solve("xyab","xzca") = "ybzc"
# --The first string has 'yb' which is not in the second string.
# --The second string has 'zc' which is not in the first string.
# Notice also that you return the characters from the first string concatenated with those from the second string.
# More examples in the tests cases.

def solve(a, b):
    part1 = "".join([el for el in list(a) if el not in b])
    part2 = "".join([el for el in list(b) if el not in a])
    return part1 + part2
