# Reference : https://docs.python.org/3/tutorial/datastructures.html

# Methods of list

#8: list.sort(*, key=None, reverse=False)
#   Sort the items of the list in place 
#   (the arguments can be used for sort customization, see sorted() for their explanation).
#   key

list=[3,2,4,1,5]
list.sort()
list.sort(reverse=True)
list.sort(key = lambda x:(x%2),reverse=True)#ㅏkey계산 결과를 기준으로 sorting
print(list)