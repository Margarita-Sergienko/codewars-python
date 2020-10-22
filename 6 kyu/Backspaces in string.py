# 6 kyu
# Backspaces in string
# https://www.codewars.com/kata/5727bb0fe81185ae62000ae3
# Assume "#" is like a backspace in string. This means that string "a#bc#d" actually is "bd"
#
# Your task is to process a string with "#" symbols.
#
# Examples
# "abc#d##c"      ==>  "ac"
# "abc##d######"  ==>  ""
# "#######"       ==>  ""
# ""              ==>  ""

def clean_string(s):
    st = ""
    for el in s:
        if el == "#":
            st = st[:-1]
        else:
            st += el
    return st