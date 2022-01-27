# Slicing Strings
# Returning a range of character

b = "Hello, World!"
print(b[2:5])

## By omitting the start index, the range will start at the first character:
b = "Hello World!"
print(b[:5])

## By leaving out the end index, the range will go to the end:
b = "Hello world!"
print(b[2:])

## Negative indexing
## Negative indexes starts the slice from the end of the string.

b = "Hello, World!"
print(b[-5:-2])
# From "o" in "World!" (position -5)  to, but not icluded "d" in "World!" (position -2)
