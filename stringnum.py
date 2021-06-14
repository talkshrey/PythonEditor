import collections

word = str(input("enter a word: "))
# counter function calculates the number of times each letter appears in a word
print(collections.Counter(word))
help(collections)

n = int(input("Enter a number: "))
print(type(n))
x = str(n)
print(type(x))
print("the number you entered has been converted to a string")
