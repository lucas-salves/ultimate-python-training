#change a list item by index 
thislist = ["apple","banana","cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#Change a range of items
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant","watermelon"]
print(thislist)

#if you insert more items than you replace, the items will be inserted where you have specified, and the remaining items will be moved ahead. if the number of items replaced does not match the number of items replaced, the list length will change
thislist[1:2] = ["blackcurrant","watermelon"]
print(thislist)

#Insert items
thislist = ["apple","banana","cherry"]
thislist.insert(2, "watermelon")
print(thislist)

