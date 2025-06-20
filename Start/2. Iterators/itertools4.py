# Example file for Advanced Python by Joe Marini
# Itertools: combinations and permutations

import itertools


# product() produces the cartesian product of input iterables
cards = "A23456789TJQK"
suits = "SCHD"
deck = list(itertools.product(cards, suits))
# print(len(deck), "cards")
# print(deck)

# permutations() creates tuples of a given length with no repeated elements
teams = ("A","B","C","D")
result = itertools.permutations(teams, 2)
# print(list(result))

# combinations() will create combinations of a given length with no repeats
result = itertools.combinations(teams, 3)
# print(list(result))

# combinations_with_replacement() will create combinations of a given length with repeats
result = itertools.combinations_with_replacement(teams, 3)
print(list(result))
