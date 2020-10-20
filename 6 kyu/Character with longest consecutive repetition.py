# 6 kyu
# Character with longest consecutive repetition
# https://www.codewars.com/kata/586d6cefbcc21eed7a001155
# For a given string s find the character c (or C) with longest consecutive repetition and return:
# (c, l)
# where l (or L) is the length of the repetition. If there are two or more characters with the same l return the first in order of appearance.
# For empty string return:
# ('', 0)

def longest_repetition(chars):
    if chars == "":
        return "", 0
    s = chars[0]
    for i in range(1,len(chars)):
        if s[-1] == chars[i]:
            s += chars[i]
        else:
            s += " " + chars[i]
    arr = s.split(" ")
    lengths = [len(el) for el in arr]
    return arr[lengths.index(max(lengths))][0], max(lengths)