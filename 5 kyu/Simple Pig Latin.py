# 5 kyu
# Simple Pig Latin
# https://www.codewars.com/kata/520b9d2ad5c005041100000f
# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
# Examples
# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !

def pig_it(text):
    return " ".join([el if el in "!?.," else el[1:] + el[0] + "ay" for el in text.split()])