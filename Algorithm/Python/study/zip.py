numbers = [1, 2, 3]
letters = ["A", "B", "C"]
lists=[[1],[2,3],[4,5,6]]
for pair in zip(numbers, letters,lists):
    print(pair)



letters = ["A", "B", "C"]
lists=[[1],[2,3],[4,5,6]]
dict_1=dict(zip(letters,lists))

print(dict_1)