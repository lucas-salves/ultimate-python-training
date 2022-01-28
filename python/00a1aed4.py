#Appends a item to the end of the list:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist.append("grape")
print(thislist)

#insert an item at a specified index
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist.insert(1,"grape")
print(thislist)

#append elements from another list
tropical = ["mango","pineapple","papaya"]
thislist.extend(tropical)
print(thislist)
#The extend method can be used to add any iterable object as well (tuple, sets, dictionaries, etc)
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
