# Example file for Advanced Python by Joe Marini
# Working with basic iterators

# define a list of days in English and French
days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
daysFr = ["Dim", "Lun", "Mar", "Mer", "Jeu", "Ven", "Sam"]

# use regular interation over the days
# for d in days:
#     print(d)

# use iter() to create an iterator over a collection
# the next() function retrieves the next value from an iterator
# i = iter(days)
# print(next(i))
# print(next(i))
# print(next(i))

# iterate using a function and a sentinel
with open("testfile.txt", "r") as fp:
  # iter takes the each line the filepointer gets and
  # the '' is a sentinal which iter uses as it stop
  # so the iter will keep iterating thru each line until ''
  for line in iter(fp.readline, ''):
    print(line)

# iter() and next() are a pull model:
# where code asks for new element when the code is ready
# compared to for loop which is a push model:
# where gives each element as they are available when the code is ready
