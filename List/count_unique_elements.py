### Count number of unique elements
elements = [1, 2, 9, 18, 89,9, 9, 9, 2, 5, 8, 7, 4, 4, 8, 1]
empty = [] ## holds unique elements
count = 0 ## count number unique elements
for i in elements:
    if i not in empty:
        empty.append(i)
        count += 1

print(empty)
print("Unique elements are : ", count)
