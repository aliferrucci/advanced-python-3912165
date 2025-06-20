# Example file for Advanced Python by Joe Marini
# Itertools: chain, chain.from_iterable

import itertools


# chain() creates a single iterable from multiple
x = itertools.chain("ABCD", "1234")
print(list(x))

# make a prepend function
def prepend(val, iterable):
  return itertools.chain([val], iterable)
print(list(prepend("a", "bcde")))

# chain.from_iterable is an alternate usage of chain
s1 = "ABCDEFG"
s2 = [1,2,3,4,5]
s3 = ['$','%','@','&']
# lazy version from chain function 
# chaining only happens as you access the iterable and needs to chain together
results = itertools.chain.from_iterable([s1, s2, s3])
print(list(results))
