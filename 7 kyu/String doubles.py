# 7 kyu
# String doubles
# https://www.codewars.com/kata/5a145ab08ba9148dd6000094
# In this Kata, you will write a function doubles that will remove double string characters that are adjacent to each other.
# b) The 2 b's disappear because we are removing double characters that are adjacent.
# c) Of the 3 c's, we remove two. We are only removing doubles.
# d) The 4 d's all disappear, because we first remove the first double, and again we remove the second double.
# e) There is only one 'a' at the end, so it stays.
# Two more examples: doubles('abbbzz') = 'ab' and doubles('abba') = "". In the second example, when we remove the b's in 'abba', the double a that results is then removed.

def doubles(s):
    while True:
        st = s[0]
        for i in range(1, len(s)):
            if s[i] != st[-1]:
                st += " " + s[i]
            else:
                st += s[i]
        splstr = st.split()
        doubles = []
        for el in splstr:
            if len(el) % 2 != 0:
                doubles.append(el)
        ch = "".join(doubles)
        chst = ch[0]
        for i in range(1, len(ch)):
            if ch[i] != chst[-1]:
                chst += " " + ch[i]
            else:
                chst += ch[i]
        chsplstr = chst.split()
        check = []
        for el in chsplstr:
            if len(el) % 2 != 0:
                check.append(el)
        if check == doubles:
            break
        else:
            s = "".join(doubles)
    doubles = "".join(doubles)
    f = doubles[0]
    for el in doubles:
        if el != f[-1]:
            f += el
    return f