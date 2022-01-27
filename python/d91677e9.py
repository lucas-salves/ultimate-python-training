# Format

#is not possible to combine strings and numbers like this:
#age = 23
#txt = "My name is Lucas, I am "+age
#print(txt)

#To make this possible, we can use format() method.
age = 23
txt = "My name is Lucas, and I am {}"
print(txt.format(age))

# Is possible to use index numbers {0} to select in which placeholder put the variables
quantity = 3
itemnumber = 567
price = 49.65
myorder = "I want to pay {2} dollars for {0} pieces of item {1}"
print( myorder.format(quantity, itemnumber, price) )
