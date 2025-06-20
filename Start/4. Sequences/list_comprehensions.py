# Example file for Advanced Python by Joe Marini
# Demonstrate how to use list comprehensions


# define two lists of numbers
evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# Perform a mapping and filter function on a list using built-in functions
evenSquared = list(map(lambda x: x ** 2, filter(lambda e:e > 4 and e < 16, evens)))
print(evenSquared)

# Derive a new list of numbers frm a given list
evenSquaredAll = [x ** 2 for x in evens]
print(evenSquaredAll)

# Limit the items operated on with a predicate condition
oddSquared = [x ** 2 for x in odds if x > 3 and x < 17]
print(oddSquared)
