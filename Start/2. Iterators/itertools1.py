# Example file for Advanced Python by Joe Marini
# Itertools: count, cycle, accumulate


import itertools

names = ["Joe", "Jane", "Jim"]

# cycle iterator can be used to cycle over a collection infinitely
cycler = itertools.cycle(names)
# print(next(cycler))
# print(next(cycler))
# print(next(cycler))
# print(next(cycler))

# use count to create a simple counter
counter = itertools.count(100, 10)
# print(next(counter))
# print(next(counter))
# print(next(counter))

# accumulate creates an iterator that accumulates values
vals = [10,20,30,40,50,40,30]
acc = itertools.accumulate(vals)
# print(next(acc))
# print(next(acc))
# print(next(acc))
# print(list(acc))

# create custom accumulation function to find maximum in list
acc = itertools.accumulate(vals, max)

# amortize a loan over a set number of payments for a 2000 loan at 4%
payments = [100, 125, 200, 105, 100, 120, 110, 130, 150, 100, 110, 120]
update = lambda balance, payment: round(balance * 1.04) - payment
balance = itertools.accumulate(payments, update, initial=2_000)
print(list(balance))
