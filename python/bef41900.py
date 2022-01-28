#if the item to remove does not exist, remove method will throw an error
thisset = {"apple","banana","cherry"}
thisset.remove("banana")
print(thisset)

# if the item to remove does not exist, discard will not throw an error
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

#pop method will remove the last item, but, remember that sets are unordered, so you will not know what item that gets removed

#clear method empties the set

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

#del keyword will delete the set completely
thisset = {"apple", "banana", "cherry"}
print(thisset)
del thisset
print(thisset)
