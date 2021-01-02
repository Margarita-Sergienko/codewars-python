# 7 kyu
# The old switcheroo
# https://www.codewars.com/kata/55d410c492e6ed767000004f
# Write a function
# vowel_2_index('this is my string') == 'th3s 6s my str15ng'
# vowel_2_index('Codewars is the best site in the world') == 'C2d4w6rs 10s th15 b18st s23t25 27n th32 w35rld'
# vowel_2_index('') == ''
# Your function should be case insensitive to the vowels.

def vowel_2_index(st):
    return "".join([str(i+1) if st[i].lower() in "euioa" else st[i] for i in range(len(st))])