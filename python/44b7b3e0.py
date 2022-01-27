# Variables that are created outside a function are global variables. They can be used outside and inside the functions

x = "awesome"
def myfunc():
	print("Python is " + x)

myfunc()

# if you create a local variable with the same name of a global variable, this variable can only be used inside the function, and the global with the same name will remains as it was.

x = "awesome"
def myfunc():
	x = "weird"
	print("Python is "+x)

myfunc()

# You can use the global keyword to make a global variable inside a function:
def myfunct():
	global globalVar
	globalVar = "fantastic"

myfunct()
print("Python is " + globalVar)

# Using the global keyword to change a global variable inside a function:
test = "awesome"
def myfunc4():
	global  test
	test = "fantastic"

myfunc4()
print("Python is "+test)
