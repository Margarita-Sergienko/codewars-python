# 7 kyu
# Switcheroo
# https://www.codewars.com/kata/57f759bb664021a30300007d
# Given a string made up of letters a, b, and/or c, switch the position of letters a and b (change a to b and vice versa). Leave any incidence of c untouched.
# Example:
# 'acb' --> 'bca'
# 'aabacbaa' --> 'bbabcabb'

def switcheroo(st):
    return "".join(["b" if el == "a" else "a" if el == "b" else el for el in st])