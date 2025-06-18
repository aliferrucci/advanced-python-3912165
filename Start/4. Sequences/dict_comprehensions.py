# Example file for Advanced Python by Joe Marini
# Demonstrate how to use dictionary comprehensions

# define a list of temperature values
ctemps = [0, 12, 34, 100]

# Use a comprehension to build a dictionary
tempDict = {c: (9/5 * c) + 32 for c in ctemps if c < 100}
print(tempDict)

# Merge two dictionaries with a comprehension
team1 = {"Jones": 24, "Jameson": 18, "Smith": 58, "Burns": 7}
team2 = {"White": 12, "Macke": 88, "Perce": 4}
teamDict = {k:v for team in (team1, team2) for k,v in team.items()}
print(teamDict)
