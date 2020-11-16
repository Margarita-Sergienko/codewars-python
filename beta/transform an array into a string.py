# beta
# transform an array into a string
# https://www.codewars.com/kata/59a602dc57019008d900004e
# A simple kata, my first.
# simply tranform an array into a string, like so:
#   transform([4, -56, true, "box"]) => "4-56truebox"

def transform(s):
    return "".join([str(el) for el in s])