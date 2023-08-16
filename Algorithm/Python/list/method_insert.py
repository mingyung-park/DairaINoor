# Reference : https://docs.python.org/3/tutorial/datastructures.html

# Methods of list

#3: insert(i,x)
#   Insert an item at a given position.
#   i :  the index of the element before which to insert. 즉, i인덱스에 insert됨
list=[1,2,3,4,5,6,7]
list.insert(2,100)
print(list)

list.insert(0,"front")
print(list)

list.insert(len(list),"back")
print(list)