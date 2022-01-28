# Access list items
thislist = ["apple","banana"]
print(thislist[1])

#Use negative indexing to start the indexing from the las item of the list (-1)  to the second last item (-2) and so on.

print(thislist[-1]) ## prints: banana

#Range of indexes
thislist = ["apple","banana","cherry","orange","kiwi","melon","mango"]
print(thislist[2:5])

# this example returns the items from the beginning to, but NOT including "kiwi"
print(thislist[:4])

#This example returns the items from "cherry" to the end:
print(thislist[2:])

#Check if a list contain an item

if "apple" in thislist:
	print("Sim, 'apple' está na lista de frutas")
