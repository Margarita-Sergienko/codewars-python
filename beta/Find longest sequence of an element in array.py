# Beta
# Find longest sequence of an element in array
# https://www.codewars.com/kata/5f8dd79aa962b600335f7577
# Write a function longest_sequence that takes in an array and value as arguments. Return the length of the longest sequence of the value in the array as an integer.
# For example, if the array was [1, 0, 1, 1, 0, 0, 1, 1, 1] and the value to check was 1, then you would return 3.
# There does not need to be a strict longest sequence, if two sequences are tied, return one of their lengths. If the value doesn't occur in the array, return 0.

def longest_sequence(arr, elem):
    arr = "".join([str(el)+"_" if el == elem else " " for el in arr]).split()
    arrs = []
    for el in arr:
        arrs.append(el[:-1].split("_"))
    lens = [len(el) for el in arrs]
    return max(lens) if len(lens) > 0 else 0