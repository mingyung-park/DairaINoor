# Reference : https://docs.python.org/3/tutorial/datastructures.html

# Methods of list

#5: remove(x)
#   Remove the first item from the list whose value is equal to x.
#   If there is no such value, it raises a ValueError
list=[1,2,3,2,1]
list.remove(2)
print(list)
#   >> list.remove(4)
#   ValueError: list.remove(x): x not in list


#6: clear(x)
#   Remove All items from list. 
list=[1,2,3,4,5]
list.clear()
print(list)