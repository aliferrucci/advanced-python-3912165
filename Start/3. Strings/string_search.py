# Example file for Advanced Python by Joe Marini


sample_text = "The quick brown fox jumps over the lazy dog."
tempstr= "the quick brown fox jumps over the lazy dog."

# Using find() to find the first occurrence of a substring
print("First occurrence of 'the':", sample_text.find("the"))
# to make this case insensitive set text to either upper/lower case

# Example with optional start and end parameters
print("First occurrence of 'the':", sample_text.find("the", 5, 36))


# Using index() to find the first occurrence of a substring (raises ValueError if not found)
print("First occurrence of 'fox':", sample_text.index("fox"))

try:
  print("First occurrence of 'fax':", sample_text.index("fax"))
except ValueError:
  print("Not found")

# The 'in' operator can be used for Boolean testing:
print("Is 'fox' present:", "fox" in sample_text)

# Using rfind() to find the last occurrence of a substring
print("Last occurrence of 'the':", sample_text.rfind('the'))

# Using rindex() to find the last occurrence of a substring (raises ValueError if not found)
print("Last occurrence of 'jump':", sample_text.rindex('jump'))

# The replace() function will find content in the string and replace it
result = sample_text.replace("lazy", "tired")
print(result) # string are immmutable so new strings are being created
result = tempstr.replace("the", "THE")
print(result)
