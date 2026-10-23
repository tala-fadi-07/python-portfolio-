# Gold: Research Truth Values
# Source: https://docs.python.org/3/library/stdtypes.html#truth-value-testing
# Section: Truth Value Testing - Built-in Types
# Cite: https://docs.python.org/3/library/stdtypes.html#truth-value-testing

# I predict bool("") will be False because empty string is falsy, no characters
print(bool(""))

# I predict bool("0") will be True because non-empty strings are truthy even if the content is "0".
print(bool("0"))

# I predict bool(0) will be False because numeric zero is defined as falsy.
print(bool(0))

# I predict bool(0.0) will be False because 0.0 is also numeric zero and considered falsy.
print(bool(0.0))

# I predict bool("False") will be True because it's a non-empty string, the word False inside string doesn't make it false.
print(bool("False"))