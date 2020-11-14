# 7 kyu
# Tidy Number (Special Numbers Series #9)
# https://www.codewars.com/kata/5a87449ab1710171300000fd
# Given a number, Find if it is Tidy or not.

def tidyNumber(n):
    return list(str(n)) == sorted(str(n))