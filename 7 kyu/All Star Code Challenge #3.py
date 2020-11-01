# 7  kyu
# All Star Code Challenge #3
# https://www.codewars.com/kata/58640340b3a675d9a70000b9
# This Kata is intended as a small challenge for my students
# Create a function, called removeVowels (or remove_vowels), that takes a string argument and returns that same string with all vowels removed (vowels are "a", "e", "i", "o", "u").
# removeVowels("drake") // => "drk"
# removeVowels("aeiou") // => ""

def remove_vowels(strng):
    return "".join([el for el in strng if el.lower() not in "euioa"])