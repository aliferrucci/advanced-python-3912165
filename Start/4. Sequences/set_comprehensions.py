# Example file for Advanced Python by Joe Marini
# Demonstrate how to use set comprehensions

# define a list of temperature data points
ctemps = [5, 10, 12, 14, 10, 23, 41, 30, 12, 24, 12, 18, 29]

# build a set of unique Fahrenheit temperatures
# ftemps = [(9/5 * c) + 32 for c in ctemps]
# uniqueF = {(9/5 * c) + 32 for c in ctemps}
# print(ftemps)
# print(uniqueF)

# build a set from an input source
sTemp = "The quick brown fox jumped over the lazy dog"
uniqueChars = {c.upper() for c in sTemp if not c.isspace()}
print(uniqueChars)
