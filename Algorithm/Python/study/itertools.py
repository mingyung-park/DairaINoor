from itertools import permutations

# my_List = [1,2,3,4,5]
# for _,elements in enumerate(permutations(my_List,2)):
#     print(elements)
    
from itertools import product
list_2 = '45'

print([x for x in product(list_1,list_2)])

print([x for x in product(list_1,repeat = 2)])

from itertools import combinations

print([x for x in combinations(list_1, 2)])

from itertools import combinations_with_replacement
list_1 = [1,2,3] 
print([x for x in combinations_with_replacement(list_1,2)])